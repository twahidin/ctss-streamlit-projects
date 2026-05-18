import streamlit as st
#session state for customer/admin page
if "current_page" not in st.session_state:
    st.session_state.current_page = "customer"
#For SKU
def sku_enter(item,price):
    def sku(name):
        name=name.upper()
        global s
        s=""
        for i in name:
            s+=str(ord(i))
        return(s)

    if item not in st.session_state:
        st.session_state[sku(item)]=[item,price]
#use sku_enter(item name)
sku_enter("pencil","$1.50")
sku_enter("eraser","$1.00")
sku_enter("computer","$3.50")
sku_enter("pen","$2.00")
#for the customer page
if st.session_state.current_page == "customer":
    tab = st.sidebar.radio("Tabs",["Shop","Admin Login"])
    #shop page (home page for them to buy things)
    if tab == "Shop":
        searchbar = st.text_input("Search")
        col1,col2,col3=st.columns(3)
        item_count = 0
        item_dict = {}
        for key in st.session_state:
            if key.isdigit() == True:
                item_count += 1
                item_dict[key] = st.session_state[key]
        st.write(item_dict)
        def item_container(item,price,stock):
            with st.container(border=True):
                st.write(item)
                st.write(price)
                st.write(stock)
        with col1:
            count = 0
            for key in item_dict:
                if count % 3 == 0:
                    item_container(item_dict[key][0],item_dict[key][1],"temp stock")
                count += 1
        with col2:
            count = 1
            for key in item_dict:
                if count % 3 == 0:
                    item_container(item_dict[key][0],item_dict[key][1],"temp stock")
                count += 1
        with col3:
            count = 2
            for key in item_dict:
                if count % 3 == 0:
                    item_container(item_dict[key][0],item_dict[key][1],"temp stock")
                count += 1
    #admin login page
    if tab == "Admin Login":
        st.write(st.session_state)
        admin_user = st.text_input("")
        admin_pass = "Password123"
        if admin_user == admin_pass:
            st.write("yay correct password")

            if st.button("Go to Admin Page"):
                st.session_state.current_page = "admin_page"
                st.rerun()

        else:
            st.write("wrong password gtfo")
#Admin Page
elif st.session_state.current_page == "admin_page":
    tab = st.sidebar.radio("Tabs",["temp","Customer Page"])
    if tab == "temp":
        searchbar = st.text_input("Search")
    #To go back to customer page
    if tab == "Customer Page":
        if st.button("Back to customer page"):
                st.session_state.current_page = "customer"
                st.rerun()
