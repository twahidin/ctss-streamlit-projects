import streamlit as st
tab = st.sidebar.radio("Tabs",["Shop","Admin Login"])
if tab == "Shop":
    searchbar = st.text_input("Search")
    col1,col2,col3=st.columns(3)
    with col1:
        with st.container(border=True):
            st.write("item 1")
            st.write("price1")
            st.write("stock1")
    with col2:
        with st.container(border=True):
            st.write("item 2")
            st.write("price2")
            st.write("stock2")
    with col3:
        with st.container(border=True):
            st.write("item 3")
            st.write("price3")
            st.write("stock3")
if tab == "Admin Login":
    st.write("ashtons doing this")
