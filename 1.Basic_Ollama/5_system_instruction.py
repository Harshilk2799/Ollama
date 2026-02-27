import ollama

# You can give system instruction.
response = ollama.generate(model="llama3.2:1b", prompt="Why is the ocean blue.", system="You are funny assistant. You Explain things in funny way.")

print(response.response)