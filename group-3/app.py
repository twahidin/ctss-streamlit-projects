import streamlit as st
import os
#session state for customer/admin page
if "current_page" not in st.session_state:
    st.session_state.current_page = "customer"
#For SKU
def sku_enter(item,price):
    def sku(name):
        name=name.upper()
        s=""
        for i in name:
            s+=str(ord(i))
        return(s)

    if sku(item) not in st.session_state:
        st.session_state[sku(item)]=[item,price]
    with open("app.txt","a") as f:
        f.write(f"{sku(item)} : [{item},{price}]\n")
#use sku_enter(item name,price)

#for the customer page
if st.session_state.current_page == "customer":
    tab = st.sidebar.radio("Tabs",["Shop","Admin Login"])
    #shop page (home page for them to buy things)
    if tab == "Shop":
        searchbar = ""
        searchbar = st.text_input("Search")
        col1,col2,col3=st.columns(3)
        item_count = 0
        item_dict = {}
        for key in st.session_state:
            if key.isdigit() == True:
                item = st.session_state[key][0]
                if searchbar.lower() in item.lower():
                    item_count += 1
                    item_dict[item] = st.session_state[key]
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
        admin_user = st.text_input("Enter the admin password, website will automatcaly send you to admin page if password is correct")
        admin_pass = "Password123"
        if admin_user == admin_pass:
            st.write("yay correct password")
            st.session_state.current_page = "admin_page"
            st.rerun()

#Admin Page
elif st.session_state.current_page == "admin_page":
    tab = st.sidebar.radio("Tabs",["Session State","Enter SKU","Customer Page"])
    if tab == "Session State":
        st.write("Session state:")
        st.write(st.session_state)
        st.write("app.txt")
        if os.path.exists("app.txt"):
            with open("app.txt", "r") as f:
                content = f.read()
            st.text_area("File Content", content)
        else:
            st.warning("No file found yet.")
    #Input SKU
    elif tab == "Enter SKU":
        st.write("Enter the SKU info below (click enter to submit)")
        sku_input = st.text_input("")
        sku_price = st.text_input("Enter price of item here (without $ sign)")
        #Sets price to 2 d.p.
        try:
            sku_price = "{:.2f}".format(float(sku_price))
        except ValueError:
            st.write("invalid price (or its blank and you havent entered anything yet)")
        if st.button("Enter into SKU"):
            sku_enter(sku_input,sku_price)
    #To go back to customer page
    elif tab == "Customer Page":
        if st.button("Back to customer page"):
                st.session_state.current_page = "customer"
                st.rerun()
