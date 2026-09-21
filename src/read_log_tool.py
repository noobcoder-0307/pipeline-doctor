import json
from pathlib import Path

from llm import call_model

LOG_DIR = Path("sample_logs").resolve()

# AGENT-SPECIFIC: the "tool menu". Claude reads the description
# to decide when to call the tool, so write it clearly.
TOOLS = [{
    "name": "read_log",
    "description": "Read a failed Airflow task log file from the sample_logs/ folder.",
    "input_schema": {
        "type": "object",
        "properties": {"filename": {"type": "string",
                                    "description": "e.g. sample_failed_task.log"}},
        "required": ["filename"],
    },
}]

SYSTEM = "You are an Airflow expert. Be concise: root cause and fix in under 60 words."


def read_log(filename: str) -> str:
    """Read-only, restricted to sample_logs/. Blocks ../ path tricks."""
    path = (LOG_DIR / filename).resolve()
    if LOG_DIR not in path.parents:
        return "ERROR: access outside sample_logs/ is not allowed"
    if not path.is_file():
        return f"ERROR: {filename} not found"
    return path.read_text()[:5000]  # cap size to control cost


def main() -> None:
    messages = [{"role": "user",
                 "content": "Task load_orders failed. Diagnose using sample_failed_task.log."}]

    resp = call_model(messages, SYSTEM, TOOLS)
    print("stop_reason:", resp.stop_reason)

    if resp.stop_reason == "tool_use":
        block = next(b for b in resp.content if b.type == "tool_use")
        print("TOOL CALL:", block.name, json.dumps(block.input))  # log every call
        result = read_log(**block.input)

        # AGENT-SPECIFIC: send back Claude's own turn plus our tool_result,
        # linked by tool_use_id.
        messages.append({"role": "assistant", "content": resp.content})
        messages.append({"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": block.id, "content": result}]})
        resp = call_model(messages, SYSTEM, TOOLS)

    print(next(b.text for b in resp.content if b.type == "text"))
    print("tokens in/out:", resp.usage.input_tokens, resp.usage.output_tokens)


if __name__ == "__main__":
    main()