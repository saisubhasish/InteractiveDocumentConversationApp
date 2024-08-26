import streamlit as st

def handle_user_input(user_question):
    if st.session_state.conversation is None:
        st.warning("Please upload a document first.")
    else:
        with st.spinner("Thinking..."):
            response = st.session_state.conversation({"question": user_question, "chat_history": st.session_state.chat_history})
            st.session_state.chat_history.append((user_question, response["answer"]))
        
        for question, answer in st.session_state.chat_history:
            st.subheader(f"Human: {question}")
            st.write(f"AI: {answer}")