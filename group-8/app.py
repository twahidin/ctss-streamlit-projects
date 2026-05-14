import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:
    N_1 = st.button("N-1")
with col2:
    N_2 = st.button("N-2")
with col3:
    N_3 = st.button("N-3")
