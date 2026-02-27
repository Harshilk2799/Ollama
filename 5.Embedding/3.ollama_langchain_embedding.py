from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

# Simple Query
# text = "What is python programming language?"
# result = embeddings.embed_query(text)
# print(result)
# print(len(result))


documents = ["Hello, How are you?", "My name is Harshil Khatri"]

result = embeddings.embed_documents(documents)
print(result)
print(len(result))
print(len(result[0]))