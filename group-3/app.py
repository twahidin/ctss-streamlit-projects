
import streamlit as st
import os
#puts the skus in app.txt into session state
if os.path.exists("app.txt"):
    with open("app.txt","r") as f:
        for line in f:
            key, val = line.strip().split(" : ")
            item, price = val.strip("[]").split(",")
            st.session_state[key] = [item, price]

#Purchasing item store
if "customer_item" not in st.session_state:
    st.session_state.customer_item = ""
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
    tab = st.sidebar.radio("Tabs",["Shop","Customer Purchase","Admin Login"])
    #shop page (home page for them to buy things)
    if tab == "Shop":
        searchbar = ""
        searchbar = st.text_input("Search")
        col1,col2,col3=st.columns(3)
        item_count = 0
        item_dict = {}
        for key in st.session_state:
            if key.isdigit() == True:
                session_state_value = st.session_state[key]
                if isinstance(session_state_value, list):
                    item = st.session_state[key][0]
                    if searchbar.lower() in item.lower():
                        item_count += 1
                        item_dict[item] = st.session_state[key]

        st.write(item_dict)
        def item_container(item,price,stock):
            global container
            container = st.container(border=True)
            container.write(item)
            container.write(price)
            container.write(stock)


        with col1:
            count = 0
            for key in item_dict:
                if count % 3 == 0:
                    item_container(item_dict[key][0],item_dict[key][1],"temp stock")
                    if container.button("Buy", key=count):
                        price = item_dict[key][1]
                        st.session_state.customer_item_price = price
                        st.session_state.customer_item = key
                        st.session_state.current_page = "purchase"
                        st.rerun()
                count += 1

        with col2:
            count = 0
            for key in item_dict:
                if count % 3 == 1:
                    item_container(item_dict[key][0],item_dict[key][1],"temp stock")
                    if container.button("Buy", key=count):
                        price = item_dict[key][1]
                        st.session_state.customer_item_price = price
                        st.session_state.customer_item = key
                        st.session_state.current_page = "purchase"
                        st.rerun()
                count += 1
        with col3:
            count = 0
            for key in item_dict:
                if count % 3 == 2:
                    item_container(item_dict[key][0],item_dict[key][1],"temp stock")
                    if container.button("Buy", key=count):
                        price = item_dict[key][1]
                        st.session_state.customer_item_price = price
                        st.session_state.customer_item = key
                        st.session_state.current_page = "purchase"
                        st.rerun()
                count += 1



    #admin login page
    if tab == "Admin Login":
        admin_user = st.text_input("Enter the admin password, website will automatcaly send you to admin page if password is correct")
        admin_pass = "Password123"
        if admin_user != "":
            if admin_user == admin_pass:
               st.write("yay correct password")
               st.session_state.current_page = "admin_page"
               st.rerun()
            else:
                st.write("Incorrect Password")

#buy screen when they click "buy"
elif st.session_state.current_page == "purchase":
    purchase_item = st.session_state.customer_item
    price = st.session_state.customer_item_price
    st.write("You are buying:", purchase_item, "at", price)
    quantity = st.slider("Enter the amount you would like to buy (max 100)")
    purchase_item_session_state = "buy_"+purchase_item
    purchase_click = st.button("Click to enter into cart")
    price_without_sign = price.strip("$")
    if purchase_click and quantity > 0:
        st.session_state[purchase_item_session_state] = [quantity, float(price_without_sign)*quantity ]
    elif purchase_click and quantity <= 0:
        st.write("Invalid Quantity")
    if st.button("Buy More"):
        st.session_state.current_page = "customer"
        st.rerun()
    if st.button("Check out"):
        st.session_state.current_page = "customer_buy"
        st.rerun()


#Customer Checkout
elif st.session_state.current_page == "customer_buy":
    purchase_list = {}
    for key in st.session_state:
        if "buy_" in key:
            purchase_list[key] = st.session_state[key]
    st.write("Current items in your cart:")
    for key in purchase_list:
        item = key.strip("buy_")
        price = purchase_list[key][0]
        st.write(item,":", price)
    if st.button("Buy More"):
        st.session_state.current_page = "customer"
        st.rerun()
    if st.button("Reset Cart"):
        purchase_list = {}
    with st.form("my_form"):
        credit_card_number = st.text_input("Enter your credit card number (XXXX-XXXX-XXXX-XXXX)")
        valid_card = True
        card_no_dash = credit_card_number.replace('-',"")
        if card_no_dash.isdigit() == False:
            valid_card = False
        if len(card_no_dash) != 16:
            valid_card == False
        if valid_card == False:
            st.write("Your Card is invalid, please try again")
        submit = st.form_submit_button("Submit")
        if submit and valid_card:
            st.write("card", credit_card_number)



#Admin Page
elif st.session_state.current_page == "admin_page":
    tab = st.sidebar.radio("Tabs",["Session State","Enter SKU","Customer Page"])
    if tab == "Session State":
        st.write("Session state:")
        st.write(st.session_state)
        st.write("app.txt")
        if os.path.exists("app.txt"):
            with open("app.txt", "r") as f:
                for i in f:
                    st.write(i)
        else:
            st.warning("No file found yet.")
    #Input SKU
    elif tab == "Enter SKU":
        st.write("Enter the SKU info below (click enter to submit)")
        sku_input = st.text_input("")
        sku_price = st.text_input("Enter price of item here (without $ sign)")
        #Sets price to 2 d.p.
        valid_price = False
        try:
            sku_price = "{:.2f}".format(float(sku_price))
            valid_price = True
        except ValueError:
            st.write("invalid price (or its blank and you havent entered anything yet)")
        if st.button("Enter into SKU") and valid_price:
            sku_enter(sku_input,sku_price)
    #To go back to customer page
    elif tab == "Customer Page":
        if st.button("Back to customer page"):
                st.session_state.current_page = "customer"
                st.rerun()

import streamlit as st
st.write('''
    806978677376 : [pencil,$1.50]\n
    98265836982 : [eraser,$1.00]\n
    6779778085846982 : [computer,$3.50]\n
    806978 : [pen,$2.00]\n
    ''')
