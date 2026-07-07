import streamlit as st

st.set_page_config(layout="wide")

if "Seller" not in st.session_state:
    st.session_state["Seller"] = False
if "Selecting" not in st.session_state:
    st.session_state["Selecting"] = False


def is_valid_user(username, password):
    user1 = "sellersignin@gmail.com"
    passw1 = "123abc0000"
    user2 = "buyersignin@gmail.com"
    passw2 = "456def1111"

    if (username == user1 and password == passw1) or (
        username == user2 and password == passw2
    ):
        return True
    return False


@st.dialog("Are you sure?")
def sure():
    st.write("Are you sure you want to log out?")


@st.dialog("Login (For seller)")
def buyer_login():
    st.write("Enter your Login info")
    username = st.text_input("user: ")
    password = st.text_input("password: ", type="password")

    if st.button("Enter"):
        username = username.strip()
        password = password.strip()

        if is_valid_user(username, password):
            st.session_state["Seller"] = True
            st.toast("Login Successful")
            st.rerun()
        else:
            st.error("Incorrect username/password")


with st.sidebar:
    st.title("Sidebar Menu")
    option = st.selectbox("Select an option", ["seller", "buyer"])


if option == "seller":
    if not st.session_state["Seller"]:
        st.title("Welcome to the sellers page")

        if st.button("Login"):
            buyer_login()

    else:
        st.title("Add movie")

        if st.button("Logout"):
            st.session_state["Seller"] = False
            st.rerun()

else:
    if not st.session_state["Selecting"]:
        st.title("Welcome to the buyers page")

        st.write("**About us**")
        st.write(
            "Since I was a kid, I was fascinated with movies. "
            "It opened me to a whole new world."
        )
        st.write("**The world of unlimited creations. Yay**")

        movies = [
            "Gaydiens of the gaylaxia",
            "Bad",
            "GATief",
        ]

        movies_info = {
            "Gaydiens of the gaylaxia":
                "A group of space heroes protect the galaxy from evil forces.",
            "Bad":
                "A dark comedy about a man making terrible life choices.",
            "GATief":
                "An action-packed thriller about a mysterious thief.",
        }

        st.subheader("Movies")

        for movie in movies:
            if st.button(movie):

                @st.dialog(movie)
                def current_movie(movie=movie):
                    st.write(movies_info[movie])

                    if st.button("Select"):
                        st.session_state["Selecting"] = True
                        st.rerun()

                current_movie()

    if st.session_state["Selecting"] == True:
        st.title("Movie Theatre")

        st.markdown("""
        <style>
        /* Reduce spacing between columns */
        div[data-testid="stHorizontalBlock"] {
            gap: 0rem !important;
        }

        /* Remove column padding */
        div[data-testid="column"] {
            padding: 0rem !important;
            margin: 0rem !important;
        }

        /* Shrink checkbox container */
        div[data-testid="stCheckbox"] {
            margin: -6px 0 !important;
            padding: 0 !important;
        }

        /* Shrink actual checkbox box */
        div[data-testid="stCheckbox"] input {
            transform: scale(0.85);
        }
        </style>
        """, unsafe_allow_html=True)

        cols = 15
        rows = 10

        for r in range(rows):
            columns = st.columns(cols, gap="small")
            for c, col in enumerate(columns):
                with col:
                    st.checkbox(
                        "",
                        key=f"cb_{r}_{c}",
                        label_visibility="collapsed",
                    )

        if "saved_grid" not in st.session_state:
            st.session_state.saved_grid = None

        if st.button("Save"):
            st.session_state.saved_grid = [
                [
                    st.session_state.get(f"cb_{r}_{c}", False)
                    for c in range(cols)
                ]
                for r in range(rows)
            ]
            st.success("Grid saved!")
        if st.button("Cancel"):
            st.session_state["Selecting"] = False
            st.rerun()
