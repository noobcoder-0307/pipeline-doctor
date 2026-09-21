"""Log explainer v0: one call, no tools yet."""
import sys
from pathlib import Path

from llm import call_model

# System prompt = the agent's role and output contract.
SYSTEM = (
    "You are a senior data engineer diagnosing failed Airflow tasks. "
    "Given a log, reply with exactly three sections:\n"
    "ROOT CAUSE: one sentence.\n"
    "EVIDENCE: 2-3 quoted log lines.\n"
    "SUGGESTED FIX: concrete steps. Say if you are unsure."
)

# Approximate Haiku pricing in USD per million tokens. Verify on the pricing page.
PRICE_IN, PRICE_OUT = 1.0, 5.0


def explain(log_text: str) -> str:
    resp = call_model(
        messages=[{"role": "user", "content": f"Diagnose this log:\n\n{log_text}"}],
        system=SYSTEM,
        max_tokens=500,  # your original cap; default in llm.py is 400
    )
    u = resp.usage
    cost = (u.input_tokens * PRICE_IN + u.output_tokens * PRICE_OUT) / 1_000_000
    print(f"[tokens in={u.input_tokens} out={u.output_tokens} ~${cost:.5f}]")
    return resp.content[0].text


if __name__ == "__main__":
    path = Path(sys.argv[1])
    print(explain(path.read_text()))