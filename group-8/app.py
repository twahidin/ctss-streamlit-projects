import streamlit as st

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    N_1 = st.button("N-1", help = "N-1")
with col2:
    N_2 = st.button("N-2", help = "N-2")
with col3:
    N_3 = st.button("N-3", help = "N-3")
with col4:
    N_1 = st.button("N-4", help = "N-4")
with col5:
    N_2 = st.button("N-5", help = "N-5")
with col6:
    N_3 = st.button("N-6", help = "N-6")
