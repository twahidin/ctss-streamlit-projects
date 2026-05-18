if "current_page" not in st.session_state:
    st.session_state.current_page = "customer"
if st.session_state.current_page == "customer":
    tab = st.sidebar.radio("Tabs",["Shop","Admin Login"])
    if tab == "Shop":
        searchbar = st.text_input("Search")
        col1,col2,col3=st.columns(3)
        with col1:
            with st.container(border=True):
                st.write("item 1")
                st.write("price1")
                st.write("stock1")
        with col2:
            with st.container(border=True):
                st.write("item 2")
                st.write("price2")
                st.write("stock2")
        with col3:
            with st.container(border=True):
                st.write("item 3")
                st.write("price3")
                st.write("stock3")
    if tab == "Admin Login":
        admin_user = st.text_input("")
        admin_pass = "Password123"
        if admin_user.lower() == admin_pass:
            st.write("yay correct password")

            if st.button("Go to Admin Page"):
                st.session_state.current_page = "admin_page"
                st.rerun()

        else:
            st.write("wrong password gtfo")
elif st.session_state.current_page == "admin_page":
    tab = st.sidebar.radio("Tabs",["temp","Customer Page"])
    if tab == "temp":
        searchbar = st.text_input("Search")

    if tab == "Customer Page":
        if st.button("Back to customer page"):
                st.session_state.current_page = "customer"
                st.rerun()
