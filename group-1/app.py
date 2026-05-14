import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, CTSS! 👋")

name = st.text_input("What is your name?")
if name:
    st.success(f"Welcome, {name}!")

age = st.slider("How old are you?", 10, 20, 15)
st.write(f"You are {age} years old.")

if st.button("Surprise me"):
    st.balloons()
