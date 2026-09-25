import streamlit as st
import ollama
st.title("my chatbot")
st.write("this is my chatbot using AI!")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
question = st.chat_input("Type your message here....")
if question:
    st.session_state.messages.append({"role":"user","content": question})
    with st.chat_message("user"):
        st.write(question)
    response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": question}
    ]
)
    answer = response["message"]["content"]
    st.session_state.messages.append( 
        { 
            "role": "assistent",
            "content":answer
        }
        )
    with st.chat_message("assistent"):
        st.write(answer)