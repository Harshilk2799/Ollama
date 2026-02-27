import ollama

# Without thinking capabilities
response = ollama.generate(model="llama3.2:1b", prompt="What is python")

print(response)
# print(type(response))
# print(response.model_dump_json())
# print(response.model_dump().keys())

print(response.response)




# With thinking capabilities 
response = ollama.generate(model="qwen3:8b", prompt="What is python")
print(response)

import re
response_text = response.response
actual_response = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()
print(actual_response)