import ollama

# List local model
# local_models = ollama.list()
# print(local_models)

# for local_model in local_models["models"]:
#     print(local_model["model"], " ", local_model["size"])


# pull a new model
# model_name = "llama3.2:1b"
# progress = ollama.pull(model=model_name, stream=True)

# for i in progress:
#     print(i)


# Show model information
# model_details = ollama.show(model="llama3.2:1b")
# print(model_details)
# print(model_details.model_dump())


# Remove model
ollama.delete('llama3.2:1b')