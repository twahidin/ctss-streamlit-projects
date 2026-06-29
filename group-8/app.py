#27/6/26 (Cedric)
import streamlit as st
from datetime import datetime


st.title("Movie Seating", text_alignment="center")
st.space(size = "xxsmall")

bigger1,bigger2,bigger3 = st.columns(3)

with bigger1:
    location = str(st.selectbox("Select your location", ["Dummy_location_1", "Dummy_location_2"]))


with bigger2:
    date = str(st.date_input("Select your date"))

if 'date_false' not in st.session_state:
    st.session_state.date_false = False
current_date = datetime.now().strftime("%Y-%m-%d")
if date < current_date:
    st.toast("Current date is unavaliable", icon = "🚨")
    st.session_state.date_false = True

with bigger3:
    time = str(st.time_input("Select your time"))

if 'time_false' not in st.session_state:
    st.session_state.time_false = False
current_time = datetime.now().strftime("%H:%M")
if time < current_time:
    st.toast("Current timing is unavaliable", icon = "🚨")
    st.session_state.time_false = True

big1,big2,big3= st.columns([3,6,3])
col1,col2,_ = big1.columns(3)
_, col3, col4, col5, col6, _ = big2.columns(6)
_, col7, col8 = big3.columns(3)

for i in range(1,49):
    if f'N{i}' not in st.session_state:
        st.session_state[f"N{i}"] = False


def update_button(seat_number):
  st.session_state[seat_number] = not st.session_state[seat_number]


#def json_read():
    # json reading to get which seats are unavaliable

#json_read()


with col1:
    global N_1
    N_1 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-1",
                     type = "primary" if st.session_state.N1 else "secondary",
                     on_click = lambda: update_button('N1'))

    global N_9
    N_9 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-9",
                     type = "primary" if st.session_state.N9 else "secondary",
                     on_click = lambda: update_button('N9'))


    global N_17
    N_17 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-17",
                      type = "primary" if st.session_state.N17 else "secondary",
                      on_click = lambda: update_button('N17'))


    global N_25
    N_25 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-25",
                      type = "primary" if st.session_state.N25 else "secondary",
                      on_click = lambda: update_button('N25'))


    global N_33
    N_33 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-33",
                      type = "primary" if st.session_state.N33 else "secondary",
                      on_click = lambda: update_button('N33'))


    global N_41
    N_41 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-41",
                      type = "primary" if st.session_state.N41 else "secondary",
                      on_click = lambda: update_button('N41'))

with col2:
    global N_2
    N_2 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-2",
                     type = "primary" if st.session_state.N2 else "secondary",
                     on_click = lambda: update_button('N2'))


    global N_10
    N_10 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-10",
                      type = "primary" if st.session_state.N10 else "secondary",
                      on_click = lambda: update_button('N10'))


    global N_18
    N_18 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-18",
                      type = "primary" if st.session_state.N18 else "secondary",
                      on_click = lambda: update_button('N18'))


    global N_26
    N_26 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-26",
                      type = "primary" if st.session_state.N26 else "secondary",
                      on_click = lambda: update_button('N26'))


    global N_34
    N_34 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-34",
                      type = "primary" if st.session_state.N34 else "secondary",
                      on_click = lambda: update_button('N34'))


    global N_42
    N_42 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-42",
                      type = "primary" if st.session_state.N42 else "secondary",
                      on_click = lambda: update_button('N42'))

with col3:
    global N_3
    N_3 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-3",
                     type = "primary" if st.session_state.N3 else "secondary",
                     on_click = lambda: update_button('N3'))


    global N_11
    N_11 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-11",
                      type = "primary" if st.session_state.N11 else "secondary",
                      on_click = lambda: update_button('N11'))


    global N_19
    N_19 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-19",
                      type = "primary" if st.session_state.N19 else "secondary",
                      on_click = lambda: update_button('N19'))


    global N_27
    N_27 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-27",
                      type = "primary" if st.session_state.N27 else "secondary",
                      on_click = lambda: update_button('N27'))


    global N_35
    N_35 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-35",
                      type = "primary" if st.session_state.N35 else "secondary",
                      on_click = lambda: update_button('N35'))


    global N_43
    N_43 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-43",
                      type = "primary" if st.session_state.N43 else "secondary",
                      on_click = lambda: update_button('N43'))

with col4:
    global N_4
    N_4 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-4",
                     type = "primary" if st.session_state.N4 else "secondary",
                     on_click = lambda: update_button('N4'))


    global N_12
    N_12 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-12",
                      type = "primary" if st.session_state.N12 else "secondary",
                      on_click = lambda: update_button('N12'))

    global N_20
    N_20 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-20",
                      type = "primary" if st.session_state.N20 else "secondary",
                      on_click = lambda: update_button('N20'))

    global N_28
    N_28 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-28",
                      type = "primary" if st.session_state.N28 else "secondary",
                      on_click = lambda: update_button('N28'))


    global N_36
    N_36 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-36",
                      type = "primary" if st.session_state.N36 else "secondary",
                      on_click = lambda: update_button('N36'))


    global N_44
    N_44 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-44",
                      type = "primary" if st.session_state.N44 else "secondary",
                      on_click = lambda: update_button('N44'))

with col5:
    global N_5
    N_5 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-5",
                     type = "primary" if st.session_state.N5 else "secondary",
                     on_click = lambda: update_button('N5'))


    global N_13
    N_13 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-13",
                      type = "primary" if st.session_state.N13 else "secondary",
                      on_click = lambda: update_button('N13'))


    global N_21
    N_21 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-21",
                      type = "primary" if st.session_state.N21 else "secondary",
                      on_click = lambda: update_button('N21'))


    global N_29
    N_29 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-29",
                      type = "primary" if st.session_state.N29 else "secondary",
                      on_click = lambda: update_button('N29'))


    global N_37
    N_37 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-37",
                      type = "primary" if st.session_state.N37 else "secondary",
                      on_click = lambda: update_button('N37'))


    global N_45
    N_45 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-45",
                      type = "primary" if st.session_state.N45 else "secondary",
                      on_click = lambda: update_button('N45'))

with col6:
    global N_6
    N_6 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-6",
                     type = "primary" if st.session_state.N6 else "secondary",
                     on_click = lambda: update_button('N6'))

    global N_14
    N_14 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-14",
                      type = "primary" if st.session_state.N14 else "secondary",
                      on_click = lambda: update_button('N14'))

    global N_22
    N_22 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-22",
                      type = "primary" if st.session_state.N22 else "secondary",
                      on_click = lambda: update_button('N22'))

    global N_30
    N_30 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-30",
                      type = "primary" if st.session_state.N30 else "secondary",
                      on_click = lambda: update_button('N30'))


    global N_38
    N_38 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-38",
                      type = "primary" if st.session_state.N38 else "secondary",
                      on_click = lambda: update_button('N38'))


    global N_46
    N_46 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-46",
                      type = "primary" if st.session_state.N46 else "secondary",
                      on_click = lambda: update_button('N46'))

with col7:
    global N_7
    N_7 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-7",
                     type = "primary" if st.session_state.N7 else "secondary",
                     on_click = lambda: update_button('N7'))


    global N_15
    N_15 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-15",
                      type = "primary" if st.session_state.N15 else "secondary",
                      on_click = lambda: update_button('N15'))


    global N_23
    N_23 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-23",
                      type = "primary" if st.session_state.N23 else "secondary",
                      on_click = lambda: update_button('N23'))


    global N_31
    N_31 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-31",
                      type = "primary" if st.session_state.N31 else "secondary",
                      on_click = lambda: update_button('N31'))


    global N_39
    N_39 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-39",
                      type = "primary" if st.session_state.N39 else "secondary",
                      on_click = lambda: update_button('N39'))


    global N_47
    N_47 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-47",
                      type = "primary" if st.session_state.N47 else "secondary",
                      on_click = lambda: update_button('N47'))

with col8:
    global N_8
    N_8 = st.button("‎ ‎ ‎ ‎ ‎ ",
                     help = "N-8",
                     type = "primary" if st.session_state.N8 else "secondary",
                     on_click = lambda: update_button('N8'))


    global N_16
    N_16 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-16",
                      type = "primary" if st.session_state.N16 else "secondary",
                      on_click = lambda: update_button('N16'))


    global N_24
    N_24 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-24",
                      type = "primary" if st.session_state.N24 else "secondary",
                      on_click = lambda: update_button('N24'))

    global N_32
    N_32 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-32",
                      type = "primary" if st.session_state.N32 else "secondary",
                      on_click = lambda: update_button('N32'))


    global N_40
    N_40 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-40",
                      type = "primary" if st.session_state.N40 else "secondary",
                      on_click = lambda: update_button('N40'))

    global N_48
    N_48 = st.button("‎ ‎ ‎ ‎ ‎ ",
                      help = "N-48",
                      type = "primary" if st.session_state.N48 else "secondary",
                      on_click = lambda: update_button('N48'))


N_0 = False
checking= [N_0, N_1, N_2, N_3, N_4, N_5, N_6, N_7, N_8, N_9, N_10, N_11, N_12, N_13, N_14, N_15, N_16, N_17, N_18, N_19, N_20, N_21, N_22, N_23, N_24, N_25, N_26, N_27, N_28, N_29, N_30, N_31, N_32, N_33, N_34, N_35, N_36, N_37, N_38, N_39, N_40, N_41, N_42, N_43, N_44, N_45, N_46, N_47, N_48, N_0]

for i in range(1,49):
    if st.session_state[f"N{i}"] == True and checking[i] == True:
        st.toast("Seat is Unavailable or has already been selected", icon = "🚨")


with st.container(horizontal_alignment="right"):
    checkout = st.button(r"$\textsf{\large Checkout}$", type = "primary")
    if checkout == True and st.session_state.date_false == True:
        st.toast("Date is Unavailable. Please change your selected date", icon = "🚨")
    if checkout == True and st.session_state.time_false == True:
        st.toast("Time is Unavaliable. Please change your selected time", icon = "🚨")
st.caption("Red Seats Are Seats That Have Already Been Booked.")



def conclusion():
    # to be written to json later
    st.markdown(f"{location} {date} {time}")
    counter = 0
    for i in range(1,49):
        if st.session_state[f"N{i}"] == True:
            st.markdown(f"N{i}")
            counter += 1
    st.markdown(f"Number of Seats selected = {counter}")

st.markdown("For Debugging and Json related content")
st.markdown(":red[Remove After Debugging Phase]")

st.write(st.session_state)
conclusion()
