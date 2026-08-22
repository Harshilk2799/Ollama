import ollama
from decouple import config

API_KEY = config("OLLAMA_API_KEY")
client = ollama.Client("https://ollama.com", headers={"Authorization": f"Bearer {API_KEY}"})

response = client.web_search(query="What is Python Programming Language?", max_results=6)
# print(response)


# for result in response.results:
#     title = result.title
#     url = result.url
#     content = result.content

#     print(f"Title: {title}")
#     print(f"URL: {url}")
#     print(f"Content: {content}")
#     print("-"*30)



all_raw_content = []
print("Combining content from all search results...")

for result in response.results:
    # Get the raw content and add it to the list 
    all_raw_content.append(result.content)

full_text_to_summarize = "\n".join(all_raw_content)

prompt_template = f"""
You are an expert summarizer. Your task is to read the provided text and give a concise summary of the 
main points. Crucially, you must ignore all links, URLs, and any navigation text like Sign in, open In App, Explore etc.

----- Text to Summarize -------
{full_text_to_summarize}
----- Concise Summary --------
"""

summary_response = ollama.generate(
    model="qwen3-coder-next:cloud",
    prompt=prompt_template
)

print(summary_response.response)