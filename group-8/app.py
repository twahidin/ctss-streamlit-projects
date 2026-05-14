import streamlit as st

big1,big2,big3= st.columns([4,6,4])
col1,col2,_,_ = big1.columns(4)
_, col3, col4, col5, col6, _ = big2.columns(6)
_, _, col7, col8 = big3.columns(4)

with col1:
    N_1 = st.button("_", help = "N-1")
with col2:
    N_2 = st.button("_", help = "N-2")
with col3:
    N_3 = st.button("_", help = "N-3")
with col4:
    N_4 = st.button("_", help = "N-4")
with col5:
    N_5 = st.button("_", help = "N-5")
with col6:
    N_6 = st.button("_", help = "N-6")
with col7:
    N_7 = st.button("_", help = "N-7")
with col8:
    N_8 = st.button("_", help = "N-8")
