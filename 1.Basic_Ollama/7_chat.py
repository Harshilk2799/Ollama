import ollama

# generate function is not multi-turn conversations
# while True:
#     user_input = input("You: ")

#     if user_input.lower() in ["quit", 'bye', "exit"]:
#         print("Assistant: Good Bye!")
#         break

#     response = ollama.generate(model="llama3.2:1b", prompt=user_input)
#     print("Assistant: ", response.response)


# The chat function is designed for multi-turn conversations
# Key Purpose
# 1. Maintains conversation context
# 2. Stores previous user and assistant messages
# 3. Produces responses based on full chat history
# 4. Enables chatbot or assistant behavior

messages = []
messages.append({"role": "system", "content": "You are a funny assistent, You tell joke in every output."})

while True:
    user_input = input("You: ")
    print("User: ", user_input)
    if user_input.lower() in ["quit", 'bye', "exit"]:
        print("Assistant: Good Bye!")
        break
    
    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(model="llama3.2:1b", messages=messages)
    print("Assistant: ", response["message"]["content"])
    messages.append({"role": "assistant", "content": response["message"]["content"]})

print("Chat History: ", messages)