# My Git Cheat Sheet
(Grows weekly. Add a line only after you've run the command yourself.)

## Mental model
Working directory -> (git add) -> Staging area -> (git commit) -> Local repo -> (git push) -> GitHub

## Week 1: Basics
| Command | What it does |
|---|---|
| git init | Turn this folder into a repo |
| git status | What changed, what's staged (run this constantly) |
| git add <file> | Stage a file for the next commit |
| git commit -m "msg" | Save a snapshot of staged changes |
| git log --oneline | Compact history |
| git diff | Unstaged changes |
| git diff --staged | Staged changes |
| git remote add origin <url> | Link local repo to GitHub |
| git remote -v | Show the saved GitHub address |
| git push -u origin main | First push, sets upstream |
| git push | Later pushes |
| git restore <file> | Discard uncommitted edits, go back to last commit (permanent!) |
| git check-ignore -v .env | Proves which .gitignore rule ignores a file |
| ls -a | List hidden files (.env, .git) |
| rm -rf .venv | Delete a folder without asking (check the path first) |

## .gitignore must-haves
.env
__pycache__/
.venv/
*.pyc
.DS_Store

## Golden rules
- Never commit .env or API keys.
- Run git status before every add and commit.
- Small commits, one idea each.
- Message format: "verb: what changed" (e.g. "add: log reader tool")

## Week 2: Branches (to fill)
## Week 3: PRs and conflicts (to fill)
## Week 4: Undo (to fill)
## Week 5: Rebase, tags, CI (to fill)

## My mistakes and fixes
- Pressed Ctrl+C while `python3 -m venv .venv` was installing pip, leaving a half-built .venv. Fix: `rm -rf .venv`, re-run, and wait.
- Ran a script before creating the file (Errno 2). Fix: create it in src/ and check with `ls src`.
- Typo `git staus`. Git suggested `status`.
- Empty output from explain_log.py on the first run. Re-saving the file in VS Code fixed it.