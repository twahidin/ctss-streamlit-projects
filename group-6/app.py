
# —------------------HOME PAGE—-----------------#
import streamlit as st

if "Seller" not in st.session_state:
    st.session_state["Seller"] = False
if "Selecting" not in st.session_state:
    st.session_state["Selecting"] = False
if "movies" not in st.session_state:
    st.session_state.movies = []

st.set_page_config(layout="wide")

def is_valid_user(username, password):
    user1 = "sellersignin@gmail.com"
    passw1 = "123abc0000"
    user2 = "buyersignin@gmail.com"
    passw2 = "456def1111"
    if (username == user1 and password == passw1) or (username == user2 and password == passw2):
        return True

@st.dialog("Are you sure?")
def sure():
    st.write("Are you sure you want to log out?")

@st.dialog("Login (For seller)")
def buyer_login():
    st.write("Enter your Login info")
    username = st.text_input("user: ")
    password = st.text_input("password: ")
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
    if st.session_state["Seller"] == False:
        st.title("welcome to the sellers page")
        if st.button("Login"):
            buyer_login()
    else:
        st.title("Add movie")
        if st.button("Logout"):
            st.session_state["Seller"] = False
            st.rerun()

else:
    if st.session_state["Selecting"] == False:
        st.title("welcome to the buyers page")
        st.write("**about us**")
        st.write("Since I was a kid, I was fascinated with movies. It opened me to a whole new world\n")
        st.write("**The world of unlimited creations. Yay**")

        movies = ["Gaydiens of the gaylaxia", "Bad", "GATief"]

        movies_info = {
            "Gaydiens of the gaylaxia": "A group of space heroes protect the galaxy from evil forces.",
            "Bad": "A dark comedy about a man making terrible life choices.",
            "GATief": "An action-packed thriller about a mysterious thief."
        }

        st.subheader("Movies")
        for i in range(len(movies)):
            if st.button(movies[i]):
                @st.dialog(movies[i])
                def current_movie():
                    st.write(movies_info[movies[i]])
                    if st.button("select"):
                        st.session_state["Selecting"] = True
                        st.rerun()
                current_movie()

    if st.session_state["Selecting"] == True:
        st.title("Movie theatre")

        st.set_page_config(layout="wide")

        rows = 3
        cols = 2

# ---------------------------
# Session State
# ---------------------------
        if "booked" not in st.session_state:
            st.session_state.booked = set()

# ---------------------------
# Seat Selection
# ---------------------------
        st.header("Select Your Seats")

        selected = []

        for r in range(rows):
            columns = st.columns(cols)
            for c, col in enumerate(columns):
                seat = (r, c)

                with col:
                    checked = st.checkbox("", key=f"cb_{r}_{c}",
                    disabled=seat in st.session_state.booked,
                    )

                    if checked:
                        selected.append(seat)

# ---------------------------
# Validation Functions
# ---------------------------
        def valid_name(name):
            return name != "" and name.isalpha()

        def valid_email(email):
            return (
                email != ""
                and "@" in email
                and "." in email
                and not any(ch.isdigit() for ch in email)
                and email[0] != "@"
                and email[-1] != "@"
            )

        def valid_phone(phone_no):
            return len(phone_no) == 8 and phone_no.isdigit()

        def valid_credit_card(card):
            return len(card) == 16 and card.isdigit()

# ---------------------------
# Payment Dialog
# ---------------------------
        @st.dialog("Payment")
        def pay():
            name = st.text_input("Enter name")
            email = st.text_input("Enter your email")
            phone_no = st.text_input("Phone no.")
            credit_card = st.text_input("Credit card number", type="password")

            if st.button("Confirm, give me tickets"):

                if len(selected) == 0:
                  st.error("Please select at least one seat.")

                elif not valid_name(name):
                  st.error("Fill in a valid name.")

                elif not valid_email(email):
                  st.error("Invalid email.")

                elif not valid_phone(phone_no):
                  st.error("Phone number should contain exactly 8 digits.")

                elif not valid_credit_card(credit_card):
                  st.error("Credit card number should contain exactly 16 digits.")

                else:
            # Mark selected seats as booked
                  st.session_state.booked.update(selected)

            # Uncheck booked seats
                for r, c in selected:
                    st.session_state[f"cb_{r}_{c}"] = False
                    st.success("Thank you for your purchase!")
                st.rerun()

# ---------------------------
# Pay Button
# ---------------------------
        if st.button("To Pay"):
            pay()
