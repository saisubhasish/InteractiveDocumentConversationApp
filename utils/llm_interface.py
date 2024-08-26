from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def get_conversation_chain(vector_store):
    # groq_api_key = os.getenv("GROQ_API_KEY")
    llm = ChatGroq()
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)