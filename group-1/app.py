#https://myprojects.up.railway.app/

import streamlit as st
from database import write_database

st.write("Hello World I am group 1")
if write_database():
  st.write("It returns True")
else:
  st.write("Nothing is returned")
