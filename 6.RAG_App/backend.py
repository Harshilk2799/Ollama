# ==============================
# IMPORTS
# ==============================
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda


# ==============================
# CONFIG
# ==============================
EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2:1b"


# ==============================
# STEP 1 — CREATE VECTOR STORE
# ==============================
def create_vector_store(file_path: str):

    # Load PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = splitter.split_documents(docs)

    # Create embeddings
    embedding = OllamaEmbeddings(model=EMBEDDING_MODEL)

    # Create FAISS DB
    vector_store = FAISS.from_documents(
        documents=splits,
        embedding=embedding
    )

    return vector_store


# ==============================
# HELPER FUNCTION
# ==============================
def format_docs(docs):
    """Convert retrieved documents into single context string"""
    return "\n\n".join(doc.page_content for doc in docs)


# ==============================
# STEP 2 — CREATE RAG CHAIN
# ==============================
def create_rag_chain(vector_store):

    # LLM
    llm = ChatOllama(model=LLM_MODEL)

    # Prompt
    prompt = ChatPromptTemplate.from_template("""
        Answer the following question based only on the provided context.
        Your goal is to provide a detailed and comprehensive answer.
        Extract all relevant information from the context to formulate your response.
        Think step by step and structure your answer logically.
        If the context does not contain the answer to the question, state that the information is not available in the provided document. Do not attempt to make up information.

        <context>
        {context}
        </context>

        Question: {input}
    """)

    # Retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    # ==============================
    # Runnable Pipeline (LCEL)
    # ==============================
    rag_chain = (
        RunnableParallel(
            # {
            #     "context": retriever | RunnableLambda(format_docs),
            #     "input": RunnableLambda(lambda x: x),
            # }
            {
            "context": RunnableLambda(lambda x: x["input"])
            | retriever
            | RunnableLambda(format_docs),

            "input": RunnableLambda(lambda x: x["input"]),
        }
        )
        | prompt
        | llm
    )

    return rag_chain