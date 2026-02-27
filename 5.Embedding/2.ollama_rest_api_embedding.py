import requests

text_to_embed = "Hello, How are you?"

url = "http://localhost:11434/api/embed"

payload = {
    "model": "nomic-embed-text:latest",
    "input": text_to_embed
}

response = requests.post(url, json=payload)

print(response.json()["embeddings"])