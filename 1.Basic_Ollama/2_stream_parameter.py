import ollama

# When to use streaming vs non-streaming

# Streaming:
# 1. Real-time response generation
# 2. Lower perceived latency
# 3. Better for long generations


# Non-streaming:
# 1. Simpler to process
# 2. Better for short responses, or structured outputs
# 3. Easier to handle in some applications

# Streaming
stream = ollama.generate(model="llama3.2:1b", prompt="What is python", stream=True)

print(stream)

# for i in stream:
#     print(i)
#     print("**")

for i in stream:
    print(i["response"], end="")