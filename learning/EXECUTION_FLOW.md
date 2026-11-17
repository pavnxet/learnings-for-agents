<!-- verified-at: <short-sha> · <YYYY-MM-DD> -->
# Execution Flow & Module Map

> **SEED FILE.** Fill in the project sections as code lands. The "Agent kit" section at the bottom is portable — it ships with the template and needs no edit.

## Entry Points
- `<path>`: <what starts here, what it is invoked by>

## Module Map
- `<path>/`: <one-line responsibility>

## Call Paths
- <user action> -> `<a>` -> `<b>` -> <observable result>

## Data & Config
- `.env.example`: variable **names** only, zero real values
- `<other config or schema>`

---

## Agent kit (portable — do not edit)

- `AGENTS.md`: protocol the agent reads each session; Project Profile lives in §12
- `learning/`: tiered memory — `BRIEF.md`, `learning.md`, `DECISIONS.md`, `EXECUTION_FLOW.md`, `PLAYBOOKS.md`, `TOOLS.md`, `summary.md`, `INCIDENTS.md`
- `scripts/scan_sensitive.py`: scanner CLI — `--doctor`, `--staged`, `--commit-msg`, `--pre-push`, `--all`
- `scripts/setup.sh` / `setup.ps1`: one-command bootstrap of hooks and denylist
- `scripts/init-project.py`: one-time conversion of the template into your project
- `.githooks/`: pre-commit, commit-msg, pre-push
- `.github/workflows/secret-scan.yml`: CI scan plus Gitleaks
- `docs/template-guide.md`: template documentation (deleted by `init-project.py`)

### Kit call paths
- `git commit` -> `.githooks/pre-commit` -> `python scripts/scan_sensitive.py --staged` -> PASS/FAIL
- `git commit` -> `.githooks/commit-msg` -> `python scripts/scan_sensitive.py --commit-msg "$1"` -> PASS/FAIL
- `git push` -> `.githooks/pre-push` -> `python scripts/scan_sensitive.py --pre-push` -> PASS/FAIL
- `git push` (CI) -> `.github/workflows/secret-scan.yml` -> `--all` + Gitleaks -> PASS/FAIL

### Config the kit owns
- `.git/agent-denylist.txt`: private, untracked, per-clone list of blocked terms (your name, machine username, handles)
