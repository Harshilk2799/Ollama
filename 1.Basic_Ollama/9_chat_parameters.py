import ollama

messages = [{"role": "user", "content": "Tell me short story about python."}]

response = ollama.chat(
    model="llama3.2:1b", 
    messages=messages, 
    options={
        "temperature": 1.0,
        "top_p": 0.9,
        "num_predict": 100,
    })

print("Assistant: ", response["message"]["content"])