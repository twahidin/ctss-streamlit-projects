streamlit

import streamlit as st

st.title("Hello World")
st.write("Hello my name is Aidan/Kaiser/Cedric")

#9/5/26
#Admin Terminal and authentication for backend

import streamlit as st

col1, col2, col3 = st.columns(3)
with col2:
    st.title("Admin Terminal")
    container = st.container(border=True)
    user_name = container.text_input("Username:")
    container.write("")
    password = container.text_input("Password:")

with col3:
    login = container.button("Login")

if user_name and password and login:
    #Connect to backend for real authentication
    if user_name == "Admin" and password == "1234": #Testing purposes only
        st.success('Successfully login!', icon="✅")
    else:
        st.error(f"Unsuccessful login", icon="🚨")
        st.error('Your Username or password is incorrect', icon="🚨")

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

#11/5/26
#json backend

#import streamlit as st

import json

myDict = {"11/05/2026":
             {1:
                  {"movie": "Night of the Day of the Dawn of the SOn of the Bride of the Return of the Revenge of the Terror of the Attack of the Evil, Mutant, Alien, Flesh Eating, Hellbound, Zombiefied Living Dead Part 2: In shocking 2D" ,
                   "seats": {"A":[0,0,0], "B": [0,0,0], "C": [0,0,0]}}
             }


         }

with open("file.json","w") as f:
    json.dump(myDict,f, indent = 4)
    #st.json(json.dumps(myDict))
#with open("file.json","r") as f:
    #st.download_button("download", f)

#12/5/26
#login for customer

import streamlit as st

col1, col2, col3 = st.columns(3)
with col2:
    st.title(":grey[Silver Kampong]")
    container = st.container(border=True)
    user_name = container.text_input("**Username:**")
    container.write("")
    password = container.text_input("**Password:**")

with col3:
    register = container.button(":red[**Register**]")

def check_valid(a:int):
    if a not in range(0,2):
        return
    else:
        tex = ["Username", "Password"][a]
        check = [user_name, password][a]
        error_tex = ""
    if len(check) < 8:
       error_tex = f"{tex} needs to have more than 8 Characters"
       return [False, error_tex]
    elif any(char.isdigit() for char in check) == False:
        error_tex = f"{tex} must contain digits"
        return [False, error_tex]
    elif any(char.isalpha() for char in check) == False:
        error_tex = f"{tex} must contain alphabets"
        return [False, error_tex]
    elif check.split()[0] != check:
        error_tex = f"{tex} cannot contain spaces"
        return [False, error_tex]
    else:
        error_tex = f"{tex} is valid"
        return [True, error_tex]


if user_name:
    check_valid(0)
if password:
    check_valid(1)

if register == True:
    if check_valid(0)[0]:
        st.success(check_valid(0)[1])
    else:
        st.error(check_valid(0)[1])
    if check_valid(1)[0]:
        st.success(check_valid(1)[1])
    else:
        st.error(check_valid(1)[1])

    st.markdown("yay")

#13/5/26
#Kosher tring this...

import streamlit as st
def page_1():
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title(":grey[Silver Kampong]")
        container = st.container(border=True)
        user_name = container.text_input("**Username:**")
        container.write("")
        password = container.text_input("**Password:**")

    with col3:
        register = container.button(":red[**Register**]")

    def check_valid(a:int):
        if a not in range(0,2):
            return
        else:
            tex = ["Username", "Password"][a]
            check = [user_name, password][a]
            error_tex = ""
        if len(check) < 8:
           error_tex = f"{tex} needs to have more than 8 Characters"
           return [False, error_tex]
        elif any(char.isdigit() for char in check) == False:
            error_tex = f"{tex} must contain digits"
            return [False, error_tex]
        elif any(char.isalpha() for char in check) == False:
            error_tex = f"{tex} must contain alphabets"
            return [False, error_tex]
        elif check.split()[0] != check:
            error_tex = f"{tex} cannot contain spaces"
            return [False, error_tex]
        else:
            error_tex = f"{tex} is valid"
            return [True, error_tex]


    if user_name:
        check_valid(0)
    if password:
        check_valid(1)

    if register == True:
        if check_valid(0)[0]:
            st.success(check_valid(0)[1])
        else:
            st.error(check_valid(0)[1])
        if check_valid(1)[0]:
            st.success(check_valid(1)[1])
        else:
            st.error(check_valid(1)[1])
        if check_valid(0)[0] and check_valid(1)[0]:
            return register
def page_2():
    st.title("Welcome")

if page_1():

    page2 = st.Page(page_2, title="Second page", icon=":material/favorite:")
    st.switch_page(page2)
