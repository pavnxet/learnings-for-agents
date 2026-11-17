# learnings-for-agents — template guide

> **How this agent kit works.** This file documents the template itself, not your project.
> Delete it (or let `python scripts/init-project.py` delete it) once you have read it.
>
> Persistent, token-efficient agent memory + fail-closed publication safety guardrails.

Compatible with **Claude Code**, **Cursor**, **Gemini Antigravity**, **Copilot**, **Windsurf**, and custom LLM agents.

---

## 🚀 Quick Start: Use This Template

### Option 1: On GitHub (Web UI)
1. Click the green **"Use this template"** button at the top of this repository.
2. Select **"Create a new repository"**.
3. Choose your repository name and visibility.

### Option 2: Using GitHub CLI (`gh`)
```bash
gh repo create my-awesome-project --template pavnxet/learnings-for-agents --public --clone
cd my-awesome-project
```

---

## ⚡ 1-Minute Project Setup

Once cloned, initialize your local safety kit and hooks with a single command:

### Windows (PowerShell):
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
```
*(Or right-click and run in PowerShell, or execute `.\scripts\setup.ps1` if execution policy is already set).*

### Linux / macOS (Bash):
```bash
./scripts/setup.sh
```

### What Setup Does:
1. Links `.githooks` via `git config core.hooksPath .githooks`.
2. Creates your private, untracked local denylist at `.git/agent-denylist.txt`.
3. Checks that your Git email is a privacy-safe GitHub noreply address.
4. Executes `python scripts/scan_sensitive.py --doctor` to verify safety gates.

---

## 🧠 Why This Template?

Most AI coding assistants suffer from two major problems:
1. **Context Amnesia**: Every new chat session restarts with a blank slate, re-discovering bugs, conventions, and architectural choices at massive token cost.
2. **Accidental Credential & PII Leaks**: LLMs frequently paste API keys, personal names, local filesystem paths, or test tokens into commit messages and tracked docs.

This template solves both through **Tiered Memory Architecture** and **Fail-Closed Git Hooks**:

```
<project-root>/
├── README.md                  <- YOUR project readme (placeholder until you fill it)
├── AGENTS.md                  <- Master protocol & Project Profile (§12)
├── docs/
│   └── template-guide.md      <- This file. Template docs, not project state.
├── learning/                  <- Committed AI memory hierarchy (seeded, empty of history)
│   ├── BRIEF.md               <- Tier A: Cold-start summary (the ONLY mandatory read)
│   ├── learning.md            <- Tier B: Categorized lessons & conventions
│   ├── DECISIONS.md           <- Tier B: Architecture Decision Records (ADRs)
│   ├── EXECUTION_FLOW.md      <- Tier B: Living module map & call graphs
│   ├── PLAYBOOKS.md           <- Tier B: Task recipes
│   ├── TOOLS.md               <- Tier B: Vetted tool catalog & scoring
│   ├── summary.md             <- Tier C: Append-only session history
│   ├── INCIDENTS.md           <- Tier C: Postmortems
│   ├── topics/                <- Overflow for deep topics
│   └── archive/               <- Compaction archive (history never deleted)
├── scripts/
│   ├── scan_sensitive.py      <- Zero-dependency sensitive content scanner
│   ├── setup.ps1              <- Windows setup helper
│   ├── setup.sh               <- Linux/macOS setup helper
│   └── init-project.py        <- Turns this copy into your project (README, seeds, cleanup)
├── .githooks/                 <- pre-commit, commit-msg, pre-push hooks
└── .github/workflows/
    └── secret-scan.yml        <- Continuous integration safety scanner
```

---

## 📊 Memory Tiers & Token Budget

| File | Tier | Read Mode | Write Mode | Token Budget |
|---|---|---|---|---|
| **`AGENTS.md`** | A | Quick Card + §12 always | Human-edited; agents propose | Quick Card ≤ 25 lines |
| **`learning/BRIEF.md`** | A | Full read on every session start | Rewritten whole when stale | ≤ 100 lines |
| **`learning/learning.md`** | B | `grep` keyword; read matched area only | Edit in place, no duplicates | ≤ 200 lines |
| **`learning/DECISIONS.md`** | B | `grep` relevant ADRs | Append; update status in place | Unlimited |
| **`learning/EXECUTION_FLOW.md`**| B | Read area being touched | Living; update `verified-at` | ≤ 150 lines |
| **`learning/TOOLS.md`** | B | Consult before adding dependencies | Append tool & score | Unlimited |
| **`learning/summary.md`** | C | `tail -40` or grep `IN-PROGRESS` | **Append-only** | Rotate at ~500 lines |

---

## 🔒 7-Layer Defense in Depth

1. **Pre-write Scanner**: Agents scan text for keys/paths prior to file persistence.
2. **Doctor Command**: `python scripts/scan_sensitive.py --doctor` ensures hooks and denylist exist.
3. **Pre-commit Hook**: Scans staged git files; blocks commit on any detection.
4. **Commit-msg Hook**: Prevents secrets in commit titles and descriptions.
5. **Pre-push Hook**: Scans outgoing commit range before pushing.
6. **Local Denylist (`.git/agent-denylist.txt`)**: Case-insensitive blocking of your real name, machine username, and custom keywords. Lives in `.git/`, never committed.
7. **CI Pipeline (`secret-scan.yml`)**: Runs scanner and Gitleaks on all PRs and pushes.

---

## 📝 Next Steps for Your Project

0. **Run `python scripts/init-project.py --name "My Project"`** — writes your project README, clears the seeded memory files and deletes this guide.

1. **Fill in Section 12 of `AGENTS.md`** (`Project Profile`):
   - Set project name, purpose, tech stack, test command, entry points, and definition of done.
2. **Add Environment Names to `.env.example`**:
   - Provide empty variable names so teammates and agents know what environment variables are needed.
3. **Commit and Build!**
   - Start prompting your AI assistant. The agent will read `AGENTS.md` and `learning/BRIEF.md`, follow the protocol, and maintain your repository's memory automatically.

---

## 📄 License

MIT. Free for commercial, personal, and open-source use.
