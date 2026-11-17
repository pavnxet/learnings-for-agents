#!/usr/bin/env python3
"""Turn a fresh copy of the template into your own project.

Run once, from the repository root, right after scripts/setup.sh:

    python scripts/init-project.py --name "My Project"
    python scripts/init-project.py --name "My Project" --dry-run

What it does:
  1. Writes a project README (replacing the template placeholder).
  2. Clears the SEED banners from learning/ so memory files read as blank state.
  3. Deletes docs/template-guide.md, which documents the template, not your project.

Zero dependencies, stdlib only, and safe to re-run: it exits without touching
anything if the README is already a project README.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
GUIDE = ROOT / "docs" / "template-guide.md"
LEARNING = ROOT / "learning"

# Marker left in README.md by the template. Its presence means "not initialised yet".
STUB_MARKER = "About the agent kit"

README_TEMPLATE = """# {name}

> One line on what this project is and who it is for.

## Status

- **Stage**: active development
- **Stack**: `<languages, frameworks, runtime, hosting>`

## Run it

```bash
<install command>
<run command>
<test command>
```

## Layout

| Path | What it is |
|---|---|
| `AGENTS.md` | Agent protocol + this project's profile (§12) |
| `learning/` | Committed agent memory — `BRIEF.md` is the cold-start read |
| `scripts/` | Safety scanner and bootstrap helpers |
| `.githooks/` | pre-commit, commit-msg, pre-push safety gates |

## Working with an AI assistant

Your assistant reads `AGENTS.md` and `learning/BRIEF.md` at the start of every
session and keeps `learning/` up to date. Fill in §12 of `AGENTS.md` first —
stack, install, run, test, entry points, do-not-touch list.
"""

SEED_BANNER = re.compile(r"^>\s*\*\*SEED FILE", re.IGNORECASE)


def clear_seed_banners(path: Path, dry_run: bool) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [ln for ln in lines if not SEED_BANNER.match(ln.strip())]
    # collapse runs of blank lines left behind
    out, prev_blank = [], False
    for ln in kept:
        blank = not ln.strip()
        if blank and prev_blank:
            continue
        out.append(ln)
        prev_blank = blank
    if len(out) == len(lines):
        return False
    if not dry_run:
        path.write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert the template into your project.")
    ap.add_argument("--name", default=ROOT.name, help="Project name for the README title")
    ap.add_argument("--dry-run", action="store_true", help="Show what would change, write nothing")
    args = ap.parse_args()

    if not README.exists():
        print(f"error: no README.md at {ROOT}", file=sys.stderr)
        return 1

    current = README.read_text(encoding="utf-8")
    if STUB_MARKER not in current:
        print("Nothing to do: README.md is already a project README.")
        print("This script is a one-time conversion. Re-run with a fresh template copy.")
        return 0

    name = args.name.strip() or ROOT.name
    print(f"{'[dry-run] ' if args.dry_run else ''}initialising '{name}' in {ROOT}\n")

    if not args.dry_run:
        README.write_text(README_TEMPLATE.format(name=name), encoding="utf-8")
    print("  README.md            -> project README written")

    if LEARNING.is_dir():
        for f in sorted(LEARNING.glob("*.md")):
            if clear_seed_banners(f, args.dry_run):
                print(f"  learning/{f.name:<12} -> seed banners cleared")

    if GUIDE.exists():
        if not args.dry_run:
            GUIDE.unlink()
            docs = GUIDE.parent
            if docs.is_dir() and not any(docs.iterdir()):
                docs.rmdir()
        print("  docs/template-guide.md -> deleted (template docs, not project docs)")

    print("\nNext:")
    print("  1. Fill in Section 12 (Project Profile) of AGENTS.md.")
    print("  2. Rewrite learning/BRIEF.md so it describes this project.")
    print("  3. Commit: git add -A && git commit -m 'chore: initialise project from template'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
