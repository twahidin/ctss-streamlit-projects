#lwk forgor when this was made
FILENAME = "insert file name here"
import json
from functools import reduce
import operator



def ReadFromJson(fp, *locations):
  try:
    getattr(fp, "read")
    myFile = json.load(fp)
  except:
    with open(fp,"r") as f:
      myFile = json.load(f)
  return reduce(operator.getitem, locations, myFile)

def WriteToJson(fp:str, value, *locations):
  with open(fp,"r+") as f:
    myFile = json.load(f)
    reduce(operator.getitem, locations[:-1], myFile)[locations[-1]] = value
    f.seek(0)
    json.dump(myFile, f, indent = 4)
    f.truncate()



#9/5/26
#Admin Terminal and authentication for backend

import streamlit as st

col1, col2, col3 = st.columns(3)
with col2:
    st.title(":grey[Silver Kampong Admin Terminal]")
    st.write("[insert slogan]")
    container = st.container(border=True)
    user_name = container.text_input("**Username:**")
    container.write("")
    password = container.text_input("**Password:**")

with col3:
    login = container.button(":red[**Login**]")
    uploaded_file = st.file_uploader("seed database")
if user_name and password and login:
    #Connect to backend for real authentication
    if user_name in ReadFromJson(uploaded_file, "ADMINS") and password == ReadFromJson(uploaded_file, "ADMINS")[user_name]: #Testing purposes only
        st.success('Successfully login!', icon="✅")
    else:
        st.error(f"Unsuccessful login", icon="🚨")
        st.error('Your Username or password is incorrect', icon="🚨")
