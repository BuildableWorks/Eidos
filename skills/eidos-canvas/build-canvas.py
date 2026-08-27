#!/usr/bin/env python3
"""
build-canvas.py — generate an Obsidian .canvas (JSON Canvas 1.0) from an Eidos definition.

A visual map of the definition, opened in Obsidian's Canvas:

  a collection declaring `Canvas: card`   -> text nodes embedding each item
  a collection declaring `Canvas: file`   -> full-file nodes (the whole document)
  directories (a collection's grouping)   -> group nodes, nested one per directory level

How a collection draws is the framework's call, declared in its `## Collections` entry in
`_eidos/Framework.md` as a `- **Canvas:**` bullet — `file`, `card`, or `card from ## Section`
to embed just that section. No collection name means anything to this script.
  `connects_to`                       -> directed edges (this -> target), the primary map
  `depends_on`  (with --include-dependencies) -> directed edges in a distinct color (purple)

Each collection gets a distinct color (its group box and its item cards). The eidos-canvas skill
proposes a schema from the definition, confirms it, and passes it as `--color NAME:N`; unset collections
fall back to a palette in order. Regenerating an existing canvas reuses its colors, so a chosen schema
sticks. Top-level documents are NOT mapped (they frame the product; the canvas maps the collections).
The generated `.canvas` is itself a top-level document — register it in `_eidos/Framework.md`
(## Top-Level) after building.

Stdlib only — runs wherever Python 3 and a shell are available (Claude Code / IDE),
matching its sibling `eidos-index/build-index.py`. On a sandboxed host the skill falls
back to emitting the canvas JSON by hand.

Usage:
  build-canvas.py [FRAMEWORK_ROOT] [--collection NAME ...] [--color NAME:N ...]
                  [--include-dependencies] [--dependency-color N]
                  [--vault PATH] [--out FILE] [--list]

  DEFINITION_ROOT         folder containing `_eidos/` (usually the definition root, e.g. Blueprint/).
  --collection           include this collection; repeatable. Default: all declared collections.
  --color NAME:N         color a collection (Obsidian preset 1-6); repeatable. Overrides the palette
                         and any existing canvas colors.
  --include-dependencies also draw `depends_on` edges (off by default).
  --dependency-color N   Obsidian preset color for dependency edges (default 6 = purple).
  --vault                vault root that embed/file paths are relative to. Default: FRAMEWORK_ROOT.
  --out                  output .canvas path. Default: <vault>/Framework Map.canvas.
  --list                 print the framework's declared collections, then exit.

Exit codes: 0 = wrote (or --list); 1 = nothing to map / bad selection; 2 = not a definition.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

# ---- layout constants -----------------------------------------------------
CARD_W, CARD_H = 320, 220
GAP_X, GAP_Y = 40, 40
GROUP_PAD = 40      # inner padding inside a group box
GROUP_TOP = 70      # extra top room for the group label
GROUP_GAP = 60      # gap between stacked siblings (item grid / sub-groups / collections)
MAX_COLS = 4

# Obsidian canvas preset colors (1 red, 2 orange, 3 yellow, 4 green, 5 cyan, 6 purple).
# Each collection gets a distinct color. The eidos-canvas skill proposes a schema from the definition,
# confirms it with the owner, and passes it as --color NAME:N overrides; unset collections fall back
# to this palette in order. Regenerating reuses an existing canvas's colors, so a chosen schema sticks.
PALETTE = ["4", "5", "6", "2", "3", "1"]


# ---- frontmatter ----------------------------------------------------------
def read_frontmatter(text):
    """Parse leading frontmatter into {id, title, connects_to:[...], depends_on:[...]}."""
    front = {"connects_to": [], "depends_on": []}
    if not text.startswith("---"):
        return front
    end = text.find("\n---", 3)
    if end == -1:
        return front
    lines = text[3:end].split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if key in ("connects_to", "depends_on"):
            if val.startswith("[") and val.endswith("]"):
                front[key] = split_inline(val[1:-1])
            elif val in ("", "[]"):
                j = i + 1
                while j < len(lines):
                    item = re.match(r"^\s*-\s+(.*)$", lines[j])
                    if not item:
                        break
                    front[key].append(strip_quotes(item.group(1).strip()))
                    j += 1
                i = j - 1
        elif key in ("id", "title"):
            front[key] = strip_quotes(val)
        i += 1
    return front


def split_inline(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return [strip_quotes(x) for x in out]


def strip_quotes(s):
    return re.sub(r'^["\']|["\']$', "", s.strip()).strip()


def link_target(entry):
    """A connects_to/depends_on entry is a markdown link `[Title](path.md)`; return path or None."""
    m = re.search(r"\]\(([^)]+)\)", entry)
    return unquote(m.group(1).strip()) if m else None


# ---- framework parsing -----------------------------------------------------
# A collection's canvas style, declared by the framework. Absent means a plain card
# embedding the whole item — the neutral default, since the script knows no collection
# by name and cannot guess which section of a shape is the summary one.
DEFAULT_CANVAS = {"node": "card", "section": None}


def parse_canvas(block):
    """Read a collection's `- **Canvas:**` bullet: `file`, `card`, or `card from ## Section`."""
    m = re.search(r"^\s*-\s*\*\*Canvas:\*\*\s*(.+?)\s*$", block, re.MULTILINE)
    if not m:
        return dict(DEFAULT_CANVAS)
    value = m.group(1).strip().strip("`")
    if re.match(r"^file\b", value, re.I):
        return {"node": "file", "section": None}
    sec = re.search(r"\bfrom\s+`?#*\s*(.+?)`?\s*$", value, re.I)
    return {"node": "card", "section": sec.group(1).strip() if sec else None}


def declared_collections(framework_md):
    """Ordered [(name, canvas)] from the `## Collections` section of Framework.md."""
    text = framework_md.read_text(encoding="utf-8")
    m = re.search(r"^##\s+Collections\s*$", text, re.MULTILINE)
    if not m:
        return []
    rest = text[m.end():]
    nxt = re.search(r"^##\s+\S", rest, re.MULTILINE)
    if nxt:
        rest = rest[:nxt.start()]
    heads = list(re.finditer(r"^###\s+(.+?)\s*$", rest, re.MULTILINE))
    out = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(rest)
        out.append((h.group(1).strip(), parse_canvas(rest[h.end():end])))
    return out


# ---- items ----------------------------------------------------------------
def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "item"


def rel_forward(path, vault_root):
    try:
        return path.resolve().relative_to(vault_root).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def item_files(folder):
    return sorted(
        p for p in folder.glob("*.md")
        if p.name.lower() != "index.md" and not p.name.startswith(".")
    )


def read_item(path, vault_root, section=None):
    text = path.read_text(encoding="utf-8")
    fm = read_frontmatter(text)
    title = fm.get("title") or path.stem
    return {
        "id": fm.get("id") or slug(title),
        "title": title,
        "connects_to": fm["connects_to"],
        "depends_on": fm["depends_on"],
        "abs": path.resolve(),
        "vault": rel_forward(path, vault_root),
        "section": section,
        "has_section": bool(
            section and re.search(r"^#{1,6}\s+%s\s*$" % re.escape(section), text, re.M)
        ),
    }


def item_text(it):
    """Text-node body: a wikilink title over an embed of the collection's declared
    section (the whole note when none is declared, or the item lacks it)."""
    ref = it["vault"][:-3] if it["vault"].endswith(".md") else it["vault"]
    title_link = f"**[[{ref}|{it['title']}]]**"
    embed = f"![[{ref}#{it['section']}]]" if it["has_section"] else f"![[{ref}]]"
    return f"{title_link}\n\n{embed}"


def make_item_node(it, x, y, as_file, color):
    node = {"id": it["node_id"], "x": x, "y": y, "width": CARD_W, "height": CARD_H}
    if as_file:
        node["type"] = "file"
        node["file"] = it["vault"]
    else:
        node["type"] = "text"
        node["text"] = item_text(it)
    if color:
        node["color"] = color
    return node


def ceil_div(a, b):
    return (a + b - 1) // b


def ceil_sqrt(n):
    return max(1, int(n ** 0.5 + 0.999999))


# ---- recursive directory -> nested groups ---------------------------------
def build_dir(dir_path, label, group_id, x, y, canvas, color, ctx):
    """Lay out one directory as a group box: a grid of its item cards, then each
    sub-directory as a nested group stacked below. Returns (nodes, width, height)
    or (None, 0, 0) if the directory (recursively) has no items."""
    inner_x = x + GROUP_PAD
    cursor = y + GROUP_TOP
    child_nodes = []
    max_right = inner_x
    produced = False

    # direct item cards, in a grid
    items = [read_item(p, ctx["vault"], canvas["section"]) for p in item_files(dir_path)]
    if items:
        cols = min(MAX_COLS, ceil_sqrt(len(items)))
        for i, it in enumerate(items):
            it["node_id"] = ctx["node_id"](it["id"])
            col, row = i % cols, i // cols
            nx = inner_x + col * (CARD_W + GAP_X)
            ny = cursor + row * (CARD_H + GAP_Y)
            node = make_item_node(it, nx, ny, canvas["node"] == "file", color)
            child_nodes.append(node)
            ctx["items"].append(it)
            max_right = max(max_right, nx + CARD_W)
        rows = ceil_div(len(items), cols)
        cursor += rows * CARD_H + (rows - 1) * GAP_Y
        produced = True

    # nested sub-directories, each its own group, stacked below
    subdirs = sorted(p for p in dir_path.iterdir() if p.is_dir() and not p.name.startswith("."))
    for d in subdirs:
        if produced:
            cursor += GROUP_GAP
        sub_id = f"{group_id}/{d.name}"
        sub_nodes, sw, sh = build_dir(d, d.name, sub_id, inner_x, cursor, canvas, color, ctx)
        if sub_nodes:
            child_nodes += sub_nodes
            cursor += sh
            max_right = max(max_right, inner_x + sw)
            produced = True

    if not produced:
        return None, 0, 0

    width = (max_right - x) + GROUP_PAD
    height = (cursor - y) + GROUP_PAD
    group = {
        "id": f"group:{group_id}",
        "type": "group",
        "x": x, "y": y, "width": width, "height": height,
        "label": label,
    }
    if color:
        group["color"] = color
    return [group] + child_nodes, width, height


def prior_collection_colors(out_file, collections):
    """Reuse an existing canvas's per-collection colors so a chosen schema sticks on regenerate.
    Reads the top-level `group:<Collection>` node colors from the current .canvas, if any."""
    prior = {}
    if not out_file.is_file():
        return prior
    try:
        data = json.loads(out_file.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return prior
    want = {f"group:{c}": c for c in collections}
    for node in data.get("nodes", []):
        if node.get("type") == "group" and node.get("id") in want and node.get("color"):
            prior[want[node["id"]]] = node["color"]
    return prior


def resolve_colors(collections, overrides, prior):
    """Final color per collection: --color override > prior canvas > palette (in order)."""
    chosen, used, pi = {}, set(), 0
    for name in collections:
        if name in overrides:
            chosen[name] = overrides[name]
        elif name in prior:
            chosen[name] = prior[name]
        else:
            while PALETTE[pi % len(PALETTE)] in used and len(used) < len(PALETTE):
                pi += 1
            chosen[name] = PALETTE[pi % len(PALETTE)]
            pi += 1
        used.add(chosen[name])
    return chosen


# ---- canvas assembly ------------------------------------------------------
def build(root, vault_root, collections, include_deps, dep_color, colors, warnings):
    seen = {}

    def next_node_id(base):
        n = seen.get(base, 0)
        seen[base] = n + 1
        return base if n == 0 else f"{base}-{n}"

    ctx = {"vault": vault_root, "items": [], "node_id": next_node_id}

    nodes = []
    cursor_y = 0
    for name, canvas in collections:
        folder = root / name
        if not folder.is_dir():
            warnings.append(f"collection '{name}': folder not found ({folder})")
            continue
        col_nodes, _, ch = build_dir(folder, name, name, 0, cursor_y, canvas, colors.get(name), ctx)
        if col_nodes:
            nodes += col_nodes
            cursor_y += ch + GROUP_GAP

    # resolution indexes over everything included
    path_to_id = {it["abs"]: it["node_id"] for it in ctx["items"]}
    id_to_node = {it["id"]: it["node_id"] for it in ctx["items"]}
    title_to_id = {it["title"].lower(): it["node_id"] for it in ctx["items"]}

    def resolve(it, entry):
        rel = link_target(entry)
        if rel:
            return path_to_id.get((it["abs"].parent / rel).resolve())
        bare = strip_quotes(entry).lower()
        return id_to_node.get(bare) or title_to_id.get(bare)

    edges, made = [], set()

    def add_edges(field, color, kind):
        for it in ctx["items"]:
            for entry in it[field]:
                target = resolve(it, entry)
                if not target:
                    warnings.append(f"{it['id']}: unresolved {field} -> {entry}")
                    continue
                key = (kind, it["node_id"], target)
                if key in made or target == it["node_id"]:
                    continue
                made.add(key)
                edge = {
                    "id": f"{kind}:{it['node_id']}->{target}",
                    "fromNode": it["node_id"],
                    "toNode": target,
                    "toEnd": "arrow",
                }
                if color:
                    edge["color"] = color
                edges.append(edge)

    add_edges("connects_to", None, "conn")
    if include_deps:
        add_edges("depends_on", dep_color, "dep")

    return nodes, edges, len(ctx["items"])


# ---- cli ------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Generate an Obsidian .canvas map of an Eidos definition.")
    ap.add_argument("root", nargs="?", default=".", help="definition root (contains _eidos/)")
    ap.add_argument("--collection", action="append", default=[], help="include this collection (repeatable)")
    ap.add_argument("--include-dependencies", action="store_true", help="also draw depends_on edges")
    ap.add_argument("--dependency-color", default="6", help="Obsidian preset color for dependency edges (default 6=purple)")
    ap.add_argument("--color", action="append", default=[], metavar="NAME:N",
                    help="color a collection: NAME:N (Obsidian preset 1-6). Repeatable. Overrides the palette and any existing canvas colors.")
    ap.add_argument("--vault", help="vault root for embed/file paths (default: definition root)")
    ap.add_argument("--out", help="output .canvas path (default: <vault>/Framework Map.canvas)")
    ap.add_argument("--list", action="store_true", help="list declared collections, then exit")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    framework_md = root / "_eidos" / "Framework.md"
    if not framework_md.is_file():
        print(f"error: no _eidos/Framework.md under {root} — not an Eidos definition", file=sys.stderr)
        return 2

    declared = declared_collections(framework_md)
    names = [n for n, _ in declared]

    if args.list:
        print("Collections (mappable):")
        for name, canvas in declared:
            if canvas["node"] == "file":
                tag = "  (full files)"
            elif canvas["section"]:
                tag = f"  (cards from ## {canvas['section']})"
            else:
                tag = "  (cards)"
            print(f"  - {name}{tag}")
        print("Top-level documents are not mapped (they frame the product).")
        return 0

    if args.collection:
        wanted = set(args.collection)
        selected = [(n, c) for n, c in declared if n in wanted]
        for miss in sorted(wanted - set(names)):
            print(f"error: collection '{miss}' not declared in Framework.md", file=sys.stderr)
        if wanted - set(names):
            return 1
    else:
        selected = list(declared)
    if not selected:
        print("error: no collections to map", file=sys.stderr)
        return 1

    vault_root = Path(args.vault).resolve() if args.vault else root
    out_file = Path(args.out).resolve() if args.out else (vault_root / "Framework Map.canvas")

    # colors: --color overrides > existing canvas (so a chosen schema sticks on regenerate) > palette
    overrides = {}
    for spec in args.color:
        if ":" not in spec:
            print(f"error: --color expects NAME:N, got '{spec}'", file=sys.stderr)
            return 1
        name, _, val = spec.rpartition(":")
        overrides[name] = val.strip()
    chosen = [n for n, _ in selected]
    bad = [n for n in overrides if n not in chosen]
    for n in sorted(bad):
        print(f"error: --color names collection '{n}', which isn't being mapped", file=sys.stderr)
    if bad:
        return 1
    colors = resolve_colors(chosen, overrides, prior_collection_colors(out_file, chosen))

    warnings = []
    nodes, edges, n_items = build(
        root, vault_root, selected, args.include_dependencies, args.dependency_color, colors, warnings
    )
    if n_items == 0:
        print("error: nothing to map — selected collections have no items", file=sys.stderr)
        for w in warnings:
            print(f"  - {w}", file=sys.stderr)
        return 1

    out_file.write_text(json.dumps({"nodes": nodes, "edges": edges}, indent=2) + "\n", encoding="utf-8")

    print(f"  ✓ wrote {out_file}")
    print(f"    {n_items} items, {len(edges)} edges, collections: {', '.join(chosen)}")
    print(f"    colors: {', '.join(f'{c}={colors[c]}' for c in chosen)}")
    try:
        rel_out = out_file.relative_to(vault_root).as_posix()
    except ValueError:
        rel_out = out_file.name
    print(f"    ↳ register it as a top-level document in _eidos/Framework.md (## Top-Level): [{out_file.stem}]({rel_out})")
    if warnings:
        print(f"\n  {len(warnings)} warning(s):", file=sys.stderr)
        for w in warnings:
            print(f"    - {w}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
