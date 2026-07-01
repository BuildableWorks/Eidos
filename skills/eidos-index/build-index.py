#!/usr/bin/env python3
"""
build-index.py — regenerate a collection's index.md from its items.

The eidos-index skill is mostly mechanical: walk a collection's folder, read each
item's `title` and `summary`, and rebuild `<Collection>/index.md` as a grouped (or
flat) list of links. Since 4.1.0 the one-line summary is a real frontmatter property
(`summary`), not a paraphrase distilled from Intent — so the whole index is
deterministic and this script can own it end to end. The agent only writes a
`summary` on an item that's missing one; the script flags those.

Runs anywhere Python 3 (stdlib only) and a shell are available — i.e. Claude Code /
IDE. On a sandboxed platform (Claude Desktop) the skill falls back to doing the walk
by hand; this script is an accelerator and correctness guarantee, never a dependency.

Usage:
  build-index.py [REGISTRY_ROOT] [--collection NAME ...] [--check]

  REGISTRY_ROOT   the folder containing `_eidos/` (default: current directory).
  --collection    re-index only the named collection(s); repeatable. Default: all
                  collections declared in `_eidos/Registry.md`.
  --check         don't write; exit non-zero if any index is stale (CI / pre-commit).

Exit codes: 0 = wrote (or, with --check, all current); 1 = stale (--check); 2 = error.
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import quote

MARKER = "<!-- eidos-index: {name} (regenerated) -->"
MISSING = "⚠️ TODO: add a `summary` property"


def parse_frontmatter(text):
    """Return a dict of the leading YAML-ish frontmatter (flat scalar keys only)."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line:
            continue
        # only top-level keys (no indentation — skips list items / nested maps)
        if line[0] in " \t-":
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if len(val) >= 2 and val[0] in "\"'" and val[-1] == val[0]:
            val = val[1:-1]
        out[key.strip()] = val
    return out


def declared_collections(registry_md):
    """Collection names = the `### ` headings under `## Collections` in Registry.md."""
    text = registry_md.read_text(encoding="utf-8")
    m = re.search(r"^##\s+Collections\s*$", text, re.MULTILINE)
    if not m:
        return []
    rest = text[m.end():]
    nxt = re.search(r"^##\s+\S", rest, re.MULTILINE)
    if nxt:
        rest = rest[:nxt.start()]
    return [h.strip() for h in re.findall(r"^###\s+(.+?)\s*$", rest, re.MULTILINE)]


def item_files(folder):
    """Markdown items directly in `folder` (excludes index.md and dotfiles)."""
    return sorted(
        p for p in folder.glob("*.md")
        if p.name.lower() != "index.md" and not p.name.startswith(".")
    )


def link(rel_path):
    """A collection-relative link, URL-encoding spaces (Title Case) but not slashes."""
    return quote(rel_path.replace("\\", "/"), safe="/")


def render(name, groups, flat):
    """Build the index.md text. `groups`: list of (heading, [(title, rel, summary)])."""
    lines = [f"# {name}", "", MARKER.format(name=name)]

    def bullets(items):
        for title, rel, summary in sorted(items, key=lambda t: t[0].lower()):
            lines.append(f"- [{title}]({link(rel)}) — {summary or MISSING}")

    if flat:
        lines.append("")
        bullets(groups[0][1])
    else:
        for heading, items in sorted(groups, key=lambda g: g[0].lower()):
            lines.append("")
            lines.append(f"## {heading}")
            bullets(items)
    return "\n".join(lines).rstrip() + "\n"


def collect(folder):
    """Return (groups, flat) for a collection folder."""
    subdirs = sorted(p for p in folder.iterdir() if p.is_dir() and not p.name.startswith("."))
    warnings = []

    def read_item(p):
        fm = parse_frontmatter(p.read_text(encoding="utf-8"))
        title = fm.get("title") or p.stem
        summary = fm.get("summary", "").strip()
        if not summary:
            warnings.append(f"  · missing summary: {p}")
        return title, summary

    if subdirs:
        groups = []
        for d in subdirs:
            items = [(t, f"{d.name}/{p.name}", s)
                     for p in item_files(d) for (t, s) in [read_item(p)]]
            if items:
                groups.append((d.name, items))
        return groups, False, warnings

    items = [(t, p.name, s) for p in item_files(folder) for (t, s) in [read_item(p)]]
    return [("", items)], True, warnings


def main():
    ap = argparse.ArgumentParser(description="Regenerate Eidos collection index.md files.")
    ap.add_argument("root", nargs="?", default=".", help="registry root (contains _eidos/)")
    ap.add_argument("--collection", action="append", default=[], help="limit to this collection (repeatable)")
    ap.add_argument("--check", action="store_true", help="verify only; non-zero if stale")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    registry_md = root / "_eidos" / "Registry.md"
    if not registry_md.is_file():
        print(f"error: no _eidos/Registry.md under {root} — not an Eidos registry", file=sys.stderr)
        return 2

    collections = declared_collections(registry_md)
    if args.collection:
        wanted = set(args.collection)
        collections = [c for c in collections if c in wanted]
        missing = wanted - set(collections)
        for m in sorted(missing):
            print(f"error: collection '{m}' not declared in Registry.md", file=sys.stderr)
        if missing:
            return 2
    if not collections:
        print("error: no collections declared in _eidos/Registry.md (## Collections)", file=sys.stderr)
        return 2

    stale = 0
    all_warnings = []
    for name in collections:
        folder = root / name
        if not folder.is_dir():
            print(f"  ✗ {name}: folder not found ({folder})", file=sys.stderr)
            continue
        groups, flat, warnings = collect(folder)
        all_warnings += warnings
        content = render(name, groups, flat)
        index_path = folder / "index.md"
        current = index_path.read_text(encoding="utf-8") if index_path.is_file() else None
        n_items = sum(len(items) for _, items in groups)

        if args.check:
            if current != content:
                print(f"  ✗ stale: {index_path}")
                stale = 1
            else:
                print(f"  ✓ current: {name} ({n_items} items)")
        else:
            index_path.write_text(content, encoding="utf-8")
            print(f"  ✓ {name}: {n_items} items → {index_path}")

    if all_warnings:
        print("\nitems needing a summary (the agent should write one):", file=sys.stderr)
        print("\n".join(all_warnings), file=sys.stderr)

    if args.check and stale:
        print("\n✗ indexes are stale — run: build-index.py", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
