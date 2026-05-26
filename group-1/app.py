#https://myprojects.up.railway.app/

import streamlit as st
from database import write_database

import streamlit as st

def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("database.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
    st.Page(
        "https://docs.streamlit.io",
        title="Streamlit Docs",
        icon=":material/open_in_new:"
    ),
])
pg.run()
