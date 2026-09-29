import streamlit as st
st.title("My first streamlit app")
st.write("Welcome to my first streamlit application!")
name=st.next_input("what is your name?")
if st.button("submit"):
    st.write("Hello",name)