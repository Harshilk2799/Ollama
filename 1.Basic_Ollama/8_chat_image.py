import ollama
import base64

image_path = "1.Basic_Ollama/login.jpg"

with open(image_path, "rb") as f:
    image_bytes = f.read()

image_64 = base64.b64encode(image_bytes).decode("utf-8")

messages = []
messages.append({"role": "system", "content": "You are a funny assistent, You tell joke in every output."})

messages.append({"role": "user", "content": "Here is the image, I want to talk about.", "images": [image_64]})

while True:
    user_input = input("You: ")
    print("User: ", user_input)
    if user_input.lower() in ["quit", 'bye', "exit"]:
        print("Assistant: Good Bye!")
        break
    
    messages.append({"role": "user", "content": user_input})

    # Make sure model have vision capabilities
    response = ollama.chat(model="llama3.2:1b", messages=messages)
    print("Assistant: ", response["message"]["content"])
    messages.append({"role": "assistant", "content": response["message"]["content"]})

print("Chat History: ", messages)