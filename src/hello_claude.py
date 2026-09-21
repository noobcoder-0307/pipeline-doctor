"""First API call: verify key, model, and token usage."""
from llm import call_model

resp = call_model(
    messages=[{"role": "user", "content": "In one sentence, what is an Airflow DAG?"}],
    max_tokens=200,  # cost cap on the output
)
print(resp.content[0].text)
print(f"tokens in={resp.usage.input_tokens} out={resp.usage.output_tokens}")