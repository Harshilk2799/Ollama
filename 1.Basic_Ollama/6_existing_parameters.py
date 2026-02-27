import ollama

# You can modify the model existing parameters etc.
response = ollama.generate(model="llama3.2:1b", prompt="Why is the ocean blue.", 
                           options={
                               "temperature": 0.3,
                               "top_p": 0.5,
                               "top_k": 45
                           })

print(response.response)