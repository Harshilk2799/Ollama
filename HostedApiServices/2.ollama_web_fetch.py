import ollama
from decouple import config

API_KEY = config("OLLAMA_API_KEY")
client = ollama.Client("https://ollama.com", headers={"Authorization": f"Bearer {API_KEY}"})

response = client.web_fetch(url="https://www.w3schools.com/python/python_intro.asp")
print(response)

print(response.title)
print(response.content)
print(response.links)