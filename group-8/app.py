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

if user_name and password and login:
    #Connect to backend for real authentication
    if user_name == "Admin" and password == "1234": #Testing purposes only
        st.success('Successfully login!', icon="✅")
    else:
        st.error(f"Unsuccessful login", icon="🚨")
        st.error('Your Username or password is incorrect', icon="🚨")
