# <project-name>

> One line on what this project is and who it is for. Replace this line.

## Status

- **Stage**: setup — agent kit installed, project profile not filled in yet
- **Stack**: `<languages, frameworks, runtime, hosting>`
- **Run**: `<command>`

## Getting started

1. **Install the safety kit** — links the git hooks, creates your private denylist, runs the scanner doctor.

   ```bash
   ./scripts/setup.sh                                          # Linux / macOS
   powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1  # Windows
   ```

2. **Make the repo yours** — replaces this README with a project one, clears the seeded memory files, and deletes the template guide.

   ```bash
   python scripts/init-project.py --name "My Project"
   ```

3. **Fill in the Project Profile** — Section 12 of `AGENTS.md` (stack, install, run, test, entry points, do-not-touch).
4. **Start prompting.** Your assistant reads `AGENTS.md` and `learning/BRIEF.md` first, then maintains the memory files itself.

## Layout

| Path | What it is | Yours to edit |
|---|---|---|
| `AGENTS.md` | Agent protocol + your Project Profile (§12) | yes — §12 first |
| `learning/` | Tiered agent memory, committed to git | yes — it is project state |
| `scripts/scan_sensitive.py` | Secret / PII scanner used by hooks and CI | no |
| `scripts/setup.*`, `scripts/init-project.py` | One-time bootstrap | no |
| `.githooks/` | pre-commit, commit-msg, pre-push | no |
| `.github/workflows/secret-scan.yml` | CI scan + Gitleaks | no |
| `docs/template-guide.md` | How the kit works (template docs, not your project) | delete after reading |

## About the agent kit

This repository was created from the `learnings-for-agents` template. The memory tiers, token budgets and the seven-layer safety design are explained in `docs/template-guide.md`. That file documents the template itself, not your project — `init-project.py` removes it for you.
