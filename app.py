import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from backend import Processing
from dotenv import load_dotenv

def main():

    load_dotenv()

    st.set_page_config(page_title="SheetGPT", page_icon=":chart:")
    st.title("Ask SheetGPT :chart:")

    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)
        else:
            with st.chat_message("AI"):
                st.markdown(message.content)


    if user_csv is not None:
        user_question = st.chat_input("Ask a question about your CSV")

        if user_question is not None and user_question != "":
            st.session_state.chat_history.append(HumanMessage(content=user_question))
            with st.chat_message("Human"):
                st.markdown(user_question)

            response = Processing().get_answer(user_csv, user_question)
            with st.chat_message("AI"):
                st.markdown(response)
            
            st.session_state.chat_history.append(AIMessage(content=response))

if __name__ == "__main__":
    main()