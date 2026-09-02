#!/usr/bin/env python3
"""
install-seed.py — install a seed framework into a new root.

Once the owner has answered the four questions install asks — which seed, which
root folder, which naming convention, which starting groups — the rest of the install
is mechanical: copy the seed into `_eidos/`, set `naming`, scaffold a folder and an
empty `index.md` per declared collection, drop a blank item per flavor the framing
collection declares, and record the groups in the Framework. This script does exactly
that and stops. It writes no prose: intent, scope, and description are the owner's.

It also solves a transfer problem. The seed ships inside the skill, which may sit on a
different machine than the folder; a script the host runs beside the repo copies
the bytes with no round trip and no re-typing.

Runs anywhere Python 3 (stdlib only) and a shell are available — i.e. Claude Code /
IDE. On a sandboxed host the skill falls back to installing by hand; this script is an
accelerator and correctness guarantee, never a dependency.

Usage:
  install-seed.py --list [--seeds SEEDS]
  install-seed.py SEED ROOT [--naming CONVENTION] [--group NAME ...] [--product NAME]
                            [--seeds SEEDS] [--date YYYY-MM-DD] [--dry-run]

  SEED        the seed to install — a folder name under SEEDS (e.g. `software`).
  ROOT        the root to create (e.g. `Blueprints`). It must not already
              hold an `_eidos/`; an existing one is a migrate, not an install.
  --list      print every seed's version, collections, flavors, and grouping; exit.
  --naming    kebab-case (default) | TitleCase | Title Case. Governs every human-facing
              name: collection folders, item filenames, and the links that reach them.
  --group     a starting group under the grouped collection; repeatable. None = flat.
  --product   fills the README's {{Product}} placeholder; left in place if omitted.
  --seeds     where the seeds live (default: `seeds/` beside this script).
  --date      the date written into date_created / date_modified (default: today).
  --dry-run   print what would be written and touch nothing.

Exit codes: 0 = installed; 2 = error (unknown seed, occupied root, unreadable seed).
"""

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

NAMINGS = ("kebab-case", "TitleCase", "Title Case")
DECLARED_BULLETS = ("leaf", "flavors", "canvas")  # every other bullet label is the grouping
INDEX_MARKER = "<!-- index: {name} (regenerated) -->"
GROUP_PROMPT = "_(one line on what belongs here)_"


# --- naming -----------------------------------------------------------------

def titleize(label):
    """A declared flavor label as a human name: `prior work` → `Prior Work`."""
    return " ".join(w[:1].upper() + w[1:] for w in label.split())


def convert(display, naming):
    """A Title Case display name in the framework's convention."""
    if naming == "TitleCase":
        return "".join(display.split())
    if naming == "kebab-case":
        return kebab(display)
    return display


def kebab(label):
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


# --- reading the seed's Framework.md ----------------------------------------

def section(text, heading):
    """The body of a `## <heading>` section, up to the next `## `."""
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = re.search(r"^##\s+\S", rest, re.MULTILINE)
    return rest[:nxt.start()] if nxt else rest


def first_paragraph(block):
    """The prose under a `### ` heading — the collection's own description of itself."""
    lines = []
    for line in block.splitlines():
        if line.strip().startswith(("-", "#")):
            break
        if not line.strip():
            if lines:
                break
            continue
        lines.append(line.strip())
    return " ".join(lines)


def parse_collections(text):
    """Each `### ` under `## Collections`, with its flavors and grouping label.

    The framing collection is the one declared first (EIDOS.md, Layout)."""
    parts = re.split(r"^###\s+(.+?)\s*$", section(text, "Collections"), flags=re.MULTILINE)
    out = []
    for i in range(1, len(parts), 2):
        block = parts[i + 1]
        flavors, grouping, in_flavors = [], None, False
        for line in block.splitlines():
            bullet = re.match(r"^-\s+\*\*(.+?):\*\*", line)
            if bullet:
                label = bullet.group(1).strip()
                in_flavors = label.lower() == "flavors"
                if label.lower() not in DECLARED_BULLETS:
                    grouping = label
                continue
            flavor = re.match(r"^\s+-\s+\[(.+?)\]\((.+?)\)\s*(?:—\s*(.*))?$", line)
            if in_flavors and flavor:
                flavors.append((flavor.group(1).strip(), flavor.group(2).strip(),
                                (flavor.group(3) or "").strip()))
        out.append({
            "name": parts[i].strip(),
            "prose": first_paragraph(block),
            "flavors": flavors,
            "grouping": grouping,
            "framing": not out,
        })
    return out


def parse_schema(text):
    """The Schema's properties as (name, type, applies-to), core first."""
    props = []
    for line in section(text, "Schema").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() == "name" or set(cells[0]) <= set("-: "):
            continue
        props.append((cells[0], cells[1], cells[2] if len(cells) >= 4 else "all"))
    return props


def applies_to(field, collection):
    value = field.strip().lower()
    if value in ("", "all"):
        return True
    return collection.lower() in [p.strip().lower() for p in re.split(r"[,/]", value)]


def frontmatter_version(text):
    m = re.search(r"^eidos_version:\s*(\S+)", text, re.MULTILINE)
    return m.group(1) if m else "?"


# --- writing ----------------------------------------------------------------

class Fs:
    """Every write goes through here so --dry-run is honest and the report is exact."""

    def __init__(self, dry_run):
        self.dry_run = dry_run
        self.log = []

    def copytree(self, src, dest):
        self.log.append(f"copy   {src}/ → {dest}/")
        if not self.dry_run:
            shutil.copytree(src, dest)

    def remove(self, path):
        self.log.append(f"rm     {path}")
        if not self.dry_run:
            path.unlink()

    def mkdir(self, path):
        self.log.append(f"mkdir  {path}/")
        if not self.dry_run:
            path.mkdir(parents=True, exist_ok=True)

    def write(self, path, text):
        self.log.append(f"write  {path}")
        if not self.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")


def set_naming(text, naming):
    if re.search(r"^naming:.*$", text, re.MULTILINE):
        return re.sub(r"^naming:.*$", f"naming: {naming}", text, count=1, flags=re.MULTILINE)
    return re.sub(r"^---\n", f"---\nnaming: {naming}\n", text, count=1)


def set_groups(text, grouping, groups):
    """Replace the grouping bullet's placeholder with one bullet per starting group.

    The groups are written in the framework's convention, because a grouping property's
    value has to match its folder exactly for an item to validate against it."""
    pattern = rf"^-\s+\*\*{re.escape(grouping)}:\*\*.*$"
    bullets = "\n".join(f"  - **{g}** — {GROUP_PROMPT}" for g in groups)
    return re.sub(pattern, f"- **{grouping}:**\n{bullets}", text, count=1, flags=re.MULTILINE)


def rename_collection(text, old, new):
    """Rename a collection everywhere it is written — heading, links, prose, applies-to."""
    return re.sub(rf"(?<![\w-]){re.escape(old)}(?!\w)", new, text)


def index_stub(name):
    """Byte-identical to what build-index.py writes for an empty collection."""
    return f"# {name}\n\n{INDEX_MARKER.format(name=name)}\n"


def blank_item(props, collection, values, shape_text, title):
    lines = ["---"]
    for name, ptype, applies in props:
        if not applies_to(applies, collection):
            continue
        value = values.get(name, "")
        if not value and ptype.strip().lower() == "list":
            value = "[]"
        lines.append(f"{name}: {value}".rstrip())
    lines.append("---")
    return "\n".join(lines) + "\n\n" + shape_text.replace("{{title}}", title).lstrip("\n")


# --- commands ---------------------------------------------------------------

def list_seeds(seeds_dir):
    found = sorted(p for p in seeds_dir.iterdir() if (p / "Framework.md").is_file())
    if not found:
        print(f"error: no seeds under {seeds_dir}", file=sys.stderr)
        return 2
    for seed in found:
        text = (seed / "Framework.md").read_text(encoding="utf-8")
        print(f"\n{seed.name}  (Eidos {frontmatter_version(text)})")
        for c in parse_collections(text):
            role = "framing" if c["framing"] else (f"grouped by {c['grouping']}" if c["grouping"] else "flat")
            print(f"  {c['name']} — {role}")
            print(f"    {c['prose']}")
            for label, _, desc in c["flavors"]:
                print(f"    · {label} — {desc}" if desc else f"    · {label}")
    return 0


def install(args):
    seed = args.seeds / args.seed
    framework_src = seed / "Framework.md"
    if not framework_src.is_file():
        print(f"error: no seed '{args.seed}' under {args.seeds} (needs a Framework.md)", file=sys.stderr)
        return 2

    root = Path(args.root).resolve()
    if (root / "_eidos").exists():
        print(f"error: {root}/_eidos already exists — that's a root; use migrate", file=sys.stderr)
        return 2

    naming = args.naming
    text = framework_src.read_text(encoding="utf-8")
    collections = parse_collections(text)
    if not collections:
        print(f"error: {framework_src} declares no collections", file=sys.stderr)
        return 2
    props = parse_schema(text)
    fs = Fs(args.dry_run)

    # 1. the framework itself. The seed's own README is the root's visible door,
    #    so it moves to the root; roles/README.md and the rest travel as they are.
    fs.copytree(seed, root / "_eidos")
    if (root / "_eidos" / "README.md").exists() or args.dry_run:
        fs.remove(root / "_eidos" / "README.md")

    # 2. the Framework: naming, starting groups, and the collection names in convention.
    text = set_naming(text, naming)
    grouped = next((c for c in collections if c["grouping"] and not c["framing"]), None)
    if args.group:
        if not grouped:
            print(f"error: no collection in '{args.seed}' declares a grouping", file=sys.stderr)
            return 2
        text = set_groups(text, grouped["grouping"], [convert(g, naming) for g in args.group])

    readme = (seed / "README.md").read_text(encoding="utf-8") if (seed / "README.md").is_file() else None
    if readme and args.product:
        readme = readme.replace("{{Product}}", args.product)

    for c in collections:
        c["folder"] = convert(c["name"], naming)
        if c["folder"] != c["name"]:
            text = rename_collection(text, c["name"], c["folder"])
            if readme:
                readme = rename_collection(readme, c["name"], c["folder"])

    fs.write(root / "_eidos" / "Framework.md", text)
    if readme:
        fs.write(root / "README.md", readme)

    # 3. a folder and an empty leaf per collection; blank items for the framing one.
    scaffolded = []
    for c in collections:
        folder = root / c["folder"]
        fs.mkdir(folder)
        fs.write(folder / "index.md", index_stub(c["folder"]))
        if c is grouped:
            for group in args.group:
                fs.mkdir(folder / convert(group, naming))
        if not c["framing"]:
            continue
        for label, shape_rel, _ in c["flavors"]:
            shape = seed / shape_rel
            if not shape.is_file():
                print(f"  ! {c['name']}/{label}: no shape at {shape_rel}", file=sys.stderr)
                continue
            title = titleize(label)
            values = {
                "id": kebab(label),
                "title": title,
                "flavor": label,
                "status": "Draft",
                "date_created": args.date,
                "date_modified": args.date,
            }
            body = blank_item(props, c["name"], values,
                              shape.read_text(encoding="utf-8"), title)
            fs.write(folder / f"{convert(title, naming)}.md", body)
            scaffolded.append(f"{c['folder']}/{convert(title, naming)}.md")

    print("\n".join(fs.log))
    print(f"\n{'would install' if args.dry_run else 'installed'}: seed '{args.seed}' "
          f"(Eidos {frontmatter_version(text)}) → {root}, naming {naming}")
    print(f"  collections: {', '.join(c['folder'] for c in collections)}"
          + (f"; groups under {grouped['folder']}: "
             f"{', '.join(convert(g, naming) for g in args.group)}" if args.group and grouped else ""))
    if scaffolded:
        print(f"  blank frames: {', '.join(scaffolded)}")
        print("  next: run index's build-index.py to list them in the leaf")
    print("  still yours: the README's one-liner, each group's description in Framework.md,"
          " and every scaffolded blueprint's summary and body.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Install an Eidos seed framework into a new folder.")
    here = Path(__file__).resolve().parent
    ap.add_argument("seed", nargs="?", help="seed to install (folder under --seeds)")
    ap.add_argument("root", nargs="?", help="root to create (e.g. Blueprints)")
    ap.add_argument("--list", action="store_true", help="list the available seeds and exit")
    ap.add_argument("--naming", choices=NAMINGS, default="kebab-case", help="naming convention")
    ap.add_argument("--group", action="append", default=[], help="starting group (repeatable)")
    ap.add_argument("--product", help="fills the README's {{Product}} placeholder")
    ap.add_argument("--seeds", type=Path, default=here / "seeds", help="seeds folder")
    ap.add_argument("--date", default=date.today().isoformat(), help="date_created / date_modified")
    ap.add_argument("--dry-run", action="store_true", help="print the writes; change nothing")
    args = ap.parse_args()

    if not args.seeds.is_dir():
        print(f"error: no seeds folder at {args.seeds}", file=sys.stderr)
        return 2
    if args.list:
        return list_seeds(args.seeds)
    if not args.seed or not args.root:
        ap.error("SEED and ROOT are required (or pass --list)")
    return install(args)


if __name__ == "__main__":
    sys.exit(main())
