# import streamlit as st
# from document_processor import process_document
# from vector_store import create_vector_store
# from llm_interface import get_conversation_chain

# def main():
#     st.set_page_config(page_title="Interactive Document Chat", page_icon=":books:")
#     st.header("Chat with your Documents :books:")

#     if "conversation" not in st.session_state:
#         st.session_state.conversation = None
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "doc"])
#     if uploaded_file is not None:
#         with st.spinner("Processing document..."):
#             texts = process_document(uploaded_file)
#             vector_store = create_vector_store(texts)
#             st.session_state.conversation = get_conversation_chain(vector_store)
#         st.success("Document processed successfully!")

#     user_question = st.text_input("Ask a question about your document:")
#     if user_question:
#         if st.session_state.conversation is None:
#             st.warning("Please upload a document first.")
#         else:
#             with st.spinner("Thinking..."):
#                 response = st.session_state.conversation({"question": user_question, "chat_history": st.session_state.chat_history})
#                 st.session_state.chat_history.append((user_question, response["answer"]))
            
#             for question, answer in st.session_state.chat_history:
#                 st.subheader(f"Human: {question}")
#                 st.write(f"AI: {answer}")

# if __name__ == "__main__":
#     main()

import streamlit as st
from document_processor import process_document
from vector_store import create_vector_store
from llm_interface import get_conversation_chain

def main():
    st.set_page_config(page_title="Interactive Document Chat", page_icon=":books:")
    st.header("Chat with your Documents :books:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # File uploader
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "doc"])
    
    # Process document button
    if st.button("Process Document"):
        if uploaded_file is not None:
            with st.spinner("Processing document..."):
                texts = process_document(uploaded_file)
                vector_store = create_vector_store(texts)
                st.session_state.conversation = get_conversation_chain(vector_store)
            st.success("Document processed successfully!")
        else:
            st.warning("Please upload a document first.")

    # Chat interface
    st.subheader("Chat")
    
    # Display chat history
    for question, answer in st.session_state.chat_history:
        st.text_area("Human:", value=question, height=100, disabled=True)
        st.text_area("AI:", value=answer, height=200, disabled=True)
        st.markdown("---")

    # User input
    user_question = st.text_input("Ask a question about your document:")
    
    if st.button("Ask"):
        if st.session_state.conversation is None:
            st.warning("Please upload and process a document first.")
        elif user_question:
            with st.spinner("Thinking..."):
                response = st.session_state.conversation({"question": user_question, "chat_history": st.session_state.chat_history})
                st.session_state.chat_history.append((user_question, response["answer"]))
            
            # Display the latest question and answer
            st.text_area("Human:", value=user_question, height=100, disabled=True)
            st.text_area("AI:", value=response["answer"], height=200, disabled=True)
        else:
            st.warning("Please enter a question.")

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared.")

if __name__ == "__main__":
    main()