import streamlit as st
status = True
yes = "work"
if st.button("plane"):
    st.write(yes)
if st.button("no plane"):
    no = "plane crashe"
    st.write(no)
name = st.text_input("Name")
if name == ' ':
    st.error("please enter a valid name")

for loop in range(len(name)):
    if name[loop].isdigit():
        status = False
if status == False:
    st.warning("why is there number in your name")
if st.button("balloon"):
    for loop in range(10):
      st.balloons()



import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")

with col2:
    st.header("A dog")

with col3:
    st.header("An owl")
