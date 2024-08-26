from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(texts):
    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_documents(texts, embeddings)
    return vector_store