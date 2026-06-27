#lwk forgor when this was made

import json
from functools import reduce
import operator
import os



def ReadFromJson(fp, *locations):
  try:
    getattr(fp, "read")
    myFile = json.load(fp)
  except:
    with open(fp,"r") as f:
      myFile = json.load(f)
  return reduce(operator.getitem, locations, myFile)


@st.cache_data
def WriteToJson(fp:str, value, *locations):
  with open(fp,"r+") as f:
    myFile = json.load(f)
    reduce(operator.getitem, locations[:-1], myFile)[locations[-1]] = value
    f.seek(0)
    json.dump(myFile, f, indent = 4)
    f.truncate()


@st.cache_data
def writingafileidontwanttobecauseicantputgithublinksintherequirementstxtwhichmakesmefrustratedtoagreatdegree():
  with open("file.json", "w", encoding="utf-8") as f:
    json.dump({
    "11/05/2026": {
        "1": {
            "1": {
                "movie": "Night of the Day of the Dawn of the SOn of the Bride of the Return of the Revenge of the Terror of the Attack of the Evil, Mutant, Alien, Flesh Eating, Hellbound, Zombiefied Living Dead Part 2: In shocking 2D",
                "seats": {
                    "A": [0, 0, 0],
                    "B": [0, 0, 0],
                    "C": [0, 0, 0]
                }
            },
            "image_link": "https://images.pexels.com/photos/28344947/pexels-photo-28344947.jpeg"
        }
    },
    "ADMINS": {
        "ADMIN": "1234",
        "KOSHER": "5678"
    },
    "MEMBERS": {
        "JOHN": {"password": "0000", "tickets": [], "birth date": "01/01/2000", "email": "NaN"},
        "DOE": {"password": "1111", "tickets": [], "birth date": "02/02/2000", "email": "NaN"}
    }
}, f, indent=4)
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
    #uploaded_file = st.file_uploader("seed database")
if user_name and password and login and uploaded_file:

    #Connect to backend for real authentication


    if user_name in ReadFromJson("file.json", "ADMINS") and password == ReadFromJson("file.json", "ADMINS", user_name): #Testing purposes only
        st.success('Successfully login!', icon="✅")
    else:
        st.error(f"Unsuccessful login", icon="🚨")
        st.error('Your Username or password is incorrect', icon="🚨")
