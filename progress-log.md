# Progress Log

Day 0: Project started.

Day 1: Set up venv, .env, .gitignore (verified with git check-ignore).
Built hello_claude.py and explain_log.py (Haiku, ~$0.0015 per run).
Learned: system prompt controls output length/cost; 30-word prompt cut out tokens 237 -> 65.
Git: 2 commits, restore, first push to github.com/noobcoder-0307/pipeline-doctor.
Next: tool use (read_log tool) + first branch.

Day 2: Moved all model calls into src/llm.py (one function, swappable later).
Built read_log_tool.py: first tool use, read-only, locked to sample_logs/, ../.env and /etc/passwd tested and blocked.
Learned: Claude picks tool arguments itself; one round is not an agent (needs a loop); prompt limits are not enforced, max_tokens is.
Git: first feature branch (feature/read-log-tool), 3 code commits, pushed. Final call ~800 in / 90 out tokens.
Next: merge branch to main, agent loop with max-steps cap, then Pydantic for tool inputs.