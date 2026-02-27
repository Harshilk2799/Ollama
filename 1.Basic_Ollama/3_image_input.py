import ollama
import base64

# You can give multimodel input.

# image_path = "1.Basic_Ollama/login.jpg"

# with open(image_path, "rb") as f:
#     image_bytes = f.read()

# image_64 = base64.b64encode(image_bytes).decode("utf-8")

# # Make sure model have vision capabilities
# response = ollama.generate(model="llama3.2:1b", prompt="Describe the image in a short paragraph.", images=[image_64])

# print(response.response)


# You can give multimodel input (Pass Multiple Images as an input).

image_paths = ["1.Basic_Ollama/login.jpg", "1.Basic_Ollama/Register.jpeg"]

images_base64 = []
for image_path in image_paths:
    with open(image_path, "rb") as f:
        image_bytes = f.read()
        images_base64.append(base64.b64encode(image_bytes).decode("utf-8"))

# Make sure model have vision capabilities
response = ollama.generate(model="llama3.2:1b", prompt="Generate an story based on these images, make sure you take context from each and every image in sequential order.", images=images_base64)

print(response.response)