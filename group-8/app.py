import streamlit as st
import numpy as np
import time
import json
from functools import reduce
import operator


def WriteToJson(fp:str, value, *locations):
  with open(fp,"r+") as f:
    myFile = json.load(f)
    reduce(operator.getitem, locations[:-1], myFile)[locations[-1]] = value
    f.seek(0)
    json.dump(myFile, f, indent = 4)
    f.truncate()

movie_file = "file.json"

st.title("Silver Kampong Admin Terminal")

if "movies" not in st.session_state:
  st.session_state.movies = {}
if "show" not in st.session_state:
  st.session_state.show = False
if "download" not in st.session_state:
  st.session_state.download = False

def export(movie_dict):
  return json.dump(movie_dict, indent=4)

file = st.file_uploader("Existing JSON Movie Details File", accept_multiple_files=False, type="json")
if file and "loaded" not in st.session_state:
  st.session_state.movies = json.load(file)
  st.session_state.loaded = True
if file not in st.session_state:
  st.session_state.loaded = False

movie_count = 0
for title in st.session_state.movies:
  movie_count += 1

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
  st.metric("Movies", movie_count, border=True)
with metric_col2:
  st.metric("Revenue", "$0", border=True)

if st.button("New Movie"):
  st.session_state.show = not st.session_state.show

if st.session_state.show:
  title = st.text_input("Title: ", key="title_input")
  desc = st.text_input("Description: ", key="desc_input")
  photos = st.text_input("Image Link: ", key="photos_input")
  showtimes = st.selectbox("Showtimes: ", ("9.00 AM", "12.00 PM", "3.00 PM"))
  showtimes = str(showtimes)
  halls = st.selectbox("Halls: ", ("Cinema Hall 1", "Cinema Hall 2", "Cinema Hall 3"))
  halls = str(halls)

  col1, col2 = st.columns(2)
  with col1:
    if st.button("Save Changes"):
      if title:
        movie_details = {"desc": desc, "photos": photos, "showtimes": showtimes, "halls": halls}
        st.session_state.movies[title] = movie_details
        st.session_state.json = export(st.session_state.movies)
        st.session_state.download = True
        if st.session_state.loaded == True:
          WriteToJson(movie_file, movie_details, title)
          st.success(f"'{title}' has been saved!")
          time.sleep(1)
        else:
          st.warning("A file is not loaded. Your movie has not been saved.", icon="⚠️")
          time.sleep(3)
        st.rerun()

  with col2:
    if st.button("Preview Changes") and title:
      st.subheader(title)
      st.caption(desc)
      if photos:
        st.image(photos)
        st.write("Showtimes:")
        st.link_button(showtimes, "https://www.gv.com.sg/")
        st.write("Halls:")
        st.link_button(halls, "https://www.gv.com.sg/")


if st.session_state.download:
  st.download_button(label="Download JSON", data=st.session_state.json, file_name="movie_details.json", mime="text/json", icon=":material/download:",)
  st.divider()


st.subheader("Your Movies")
for title, details in st.session_state.movies.items():
  with st.expander(title):
    st.header(f"{title}")
    st.caption(details.get("desc"))
    image = details.get("photos")
    if image:
      st.image(image, width=200)
    st.write(f"Hall: {details.get('halls')}")
    st.write(f"Showtime: {details.get('showtimes')}")
