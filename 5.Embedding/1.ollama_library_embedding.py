import ollama

text_to_embed = "Hello, How are you?"

response = ollama.embeddings(model="nomic-embed-text:latest", prompt=text_to_embed)

print(response.embedding)

print(len(response.embedding)) # 768 dimension