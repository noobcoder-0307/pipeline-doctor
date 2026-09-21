# My Git Cheat Sheet
(Grows weekly. Add a line only after you've run the command yourself.)

## Mental model
Working directory -> (git add) -> Staging area -> (git commit) -> Local repo -> (git push) -> GitHub
A branch is just a movable pointer to a commit. Committing on a branch moves only that pointer, so main stays untouched.

## Week 1: Basics
| Command | What it does |
|---|---|
| git init | Turn this folder into a repo |
| git status | What changed, what's staged (run this constantly) |
| git add <file> | Stage a file for the next commit |
| git commit -m "msg" | Save a snapshot of staged changes |
| git log --oneline | Compact history |
| git --no-pager log --oneline | Print history straight to the terminal, no pager |
| git diff | Unstaged changes |
| git diff --staged | Staged changes (long output opens a pager, press q to quit) |
| git remote add origin <url> | Link local repo to GitHub |
| git remote -v | Show the saved GitHub address |
| git push -u origin main | First push, sets upstream |
| git push | Later pushes |
| git restore <file> | Discard uncommitted edits, go back to last commit (permanent!) |
| git check-ignore -v .env | Proves which .gitignore rule ignores a file |
| git ls-files | List every file Git tracks (.env and .venv must not appear) |
| ls -a | List hidden files (.env, .git) |
| rm -rf .venv | Delete a folder without asking (check the path first) |

## Terminal basics
| Command | What it does |
|---|---|
| pwd | Shows the folder you are in (run it when a path fails) |
| cd ~/projects/pipeline-doctor | Go back to the repo. A bare `cd` sends you home |
| mkdir -p <folder> | Create a folder, no error if it exists |
| mv <old> <new> | Move a file (fine for untracked files) |
| rmdir <folder> | Delete an empty folder only |
| grep -n "text" <file> | Find a line in a file, with its line number |
| PYTHONPATH=src python3 -c "..." | Test one function without running the whole script |
| q | Quit the pager (less) when output shows `:` or `(END)` |
| setopt interactive_comments | Lets zsh ignore `# comments` typed on a command line |

## Week 2: Branches
| Command | What it does |
|---|---|
| git switch -c <branch> | Create a new branch and move to it |
| git branch -a | List local and remote branches, `*` marks the current one |
| git push -u origin <branch> | Push a new branch and link it to GitHub |

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
- Run commands with long output (diff, log) on their own, never pasted in a batch.
- No inline `# comments` in pasted commands.
- Run `ls` before creating a folder, to see what the repo already has.

## Week 3: PRs and conflicts (to fill)
## Week 4: Undo (to fill)
## Week 5: Rebase, tags, CI (to fill)

## My mistakes and fixes
- Pressed Ctrl+C while `python3 -m venv .venv` was installing pip, leaving a half-built .venv. Fix: `rm -rf .venv`, re-run, and wait.
- Ran a script before creating the file (Errno 2). Fix: create it in src/ and check with `ls src`.
- Typo `git staus`. Git suggested `status`.
- Empty output from explain_log.py on the first run. Re-saving the file in VS Code fixed it.
- Typed a bare `cd`, which went to home, so relative paths broke. Fix: `cd ~/projects/pipeline-doctor`, then `pwd`.
- Pasted commands with inline `# comments` into zsh, so Git got the comment words as arguments. Fix: no comments in pasted commands.
- Created a second `logs/` folder when the repo already had `sample_logs/`. Fix: run `ls` first, then `mv` the file.
- `git diff --staged` opened a pager that swallowed the pasted commands. Fix: press `q`, check `git status`, run long-output commands alone.