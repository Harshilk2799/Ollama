import ollama

response = ollama.generate(
    model="hf.co/TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF:Q4_K_M", 
    prompt="What is python?"
)
print(response)