import ollama

response = ollama.generate(
    model="qwen3-coder-next:cloud",
    prompt="What is python?"
)

print(response)