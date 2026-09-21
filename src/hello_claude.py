"""First API call: verify key, model, and token usage."""
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment variables
MODEL = os.getenv("MODEL", "claude-haiku-4-5-20251001")  # cheapest model while developing

client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

resp = client.messages.create(
    model=MODEL,
    max_tokens=200,  # cost cap on the output
    messages=[{"role": "user", "content": "In one sentence, what is an Airflow DAG?"}],
)
print(resp.content[0].text)
print(f"tokens in={resp.usage.input_tokens} out={resp.usage.output_tokens}")