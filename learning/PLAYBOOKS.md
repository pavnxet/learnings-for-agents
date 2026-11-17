<!-- verified-at: <short-sha> · <YYYY-MM-DD> -->
# Playbooks & Task Recipes

> **SEED FILE.** Add one recipe per repeated task, in the same shape: numbered steps, then `Gotchas`. The two below are portable kit recipes.

## Setup a new clone (v:<YYYY-MM-DD> · verified-at <sha>)
1. Run `./scripts/setup.sh` (macOS/Linux) or `.\scripts\setup.ps1` (Windows).
2. Edit `.git/agent-denylist.txt` — add your real name, machine username, personal handles, sensitive terms (never committed).
3. Run `python scripts/scan_sensitive.py --doctor` until it prints `doctor: OK`.
4. Fill in §12 Project Profile in `AGENTS.md`.
5. Rewrite `learning/BRIEF.md` for this project.

Gotchas: Python must be on PATH; `git user.email` should be a GitHub noreply address.

## Run the pre-commit safety scan by hand (v:<YYYY-MM-DD> · verified-at <sha>)
1. Stage your changes explicitly: `git add <file1> <file2>`.
2. Run `python scripts/scan_sensitive.py --staged`.
3. Redact any reported value before committing.

Gotchas: never `git add -A`; confirm what is staged with `git diff --cached --stat`.

## <your recurring task> (v:<YYYY-MM-DD> · verified-at <sha>)
1. <step>
Gotchas: <the thing that bit us>
