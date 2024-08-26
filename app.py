import sys
import streamlit as st

from utils.document_processor import process_document
from utils.vector_store import create_vector_store
from utils.llm_interface import get_conversation_chain
from utils.logger import logger
from utils.exception import RAGException

def main():
    logger.info("Starting application...")
    st.set_page_config(page_title="Interactive Document Chat", page_icon=":books:")
    st.header("Chat with your Documents :books:")

    if "conversation" not in st.session_state:
        logger.info("Initializing conversation...")
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        logger.info("Initializing chat history...")
        st.session_state.chat_history = []

    try:
        logger.info("Uploading document...")
        # File uploader
        uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "doc"])
    except Exception as e:
        raise RAGException(e, sys)

    # Process document button
    if st.button("Process Document"):
        logger.info("Processing document...")
        if uploaded_file is not None:
            with st.spinner("Processing document..."):
                texts = process_document(uploaded_file)
                vector_store = create_vector_store(texts)
                st.session_state.conversation = get_conversation_chain(vector_store)
                logger.info("Document processed successfully!")
            st.success("Document processed successfully!")
        else:
            st.warning("Please upload a document first.")

    # Chat interface
    st.subheader("Chat")
    
    # Display chat history
    for i, (question, answer) in enumerate(st.session_state.chat_history):
        st.text_area("Human:", value=question, height=100, disabled=True, key=f"q_{i}")
        st.text_area("AI:", value=answer, height=200, disabled=True, key=f"a_{i}")
        st.markdown("---")

    # User input
    user_question = st.text_input("Ask a question about your document:")
    
    if st.button("Ask"):
        logger.info(f"Asking question: {user_question}")
        if st.session_state.conversation is None:
            logger.info("Please upload and process a document first.")
            st.warning("Please upload and process a document first.")
        elif user_question:
            with st.spinner("Thinking..."):
                response = st.session_state.conversation({"question": user_question, "chat_history": st.session_state.chat_history})
                st.session_state.chat_history.append((user_question, response["answer"]))
                logger.info(f"Generated Answer: {response['answer']}")
            
            # Display the latest question and answer
            logger.info("Displaying latest question and answer...")
            st.text_area("Human:", value=user_question, height=100, disabled=True, key="latest_question")
            st.text_area("AI:", value=response["answer"], height=200, disabled=True, key="latest_answer")
        else:
            st.warning("Please enter a question.")

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        logger.info("Chat history cleared.")
        st.success("Chat history cleared.")

if __name__ == "__main__":
    main()