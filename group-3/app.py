import streamlit as st
import json
import os
#puts the skus in app.txt into session state
if os.path.exists("app.txt"):
    with open("app.txt","r") as f:
        for line in f:
            key, val = line.strip().split(" : ")
            item, price, stock = val.strip("[]").split(",")
            st.session_state[key] = [item, price,stock]
#Purchasing item store
if "customer_item" not in st.session_state:
    st.session_state.customer_item = ""
#session state for customer/admin page
if "current_page" not in st.session_state:
    st.session_state.current_page = "customer"
#For SKU
def sku_enter(item,price,stock):
    def sku(name):
        s=""
        name=name.upper()
        for i in name:
            s+=str(ord(i))
        return(s)

    if sku(item) not in st.session_state:
        st.session_state[sku(item)]=[item,price,stock]
        st.text(f"{item} has been stored under the SKU number {sku(item)} with a stock of {stock}")
        with open("app.txt","a") as f:
            f.write(f"{sku(item)} : [{item},{price},{stock}]\n")
    else:
        st.text(f"{item} is already stored under the SKU number {sku(item)}")
#use sku_enter(item name,price)
#to check items
def check(sku):
  if sku not in st.session_state:
      st.error("This SKU number does not exist. Please ensure you have typed it correctly and try again.")
  else:
      i=st.session_state[sku][0]
      p=st.session_state[sku][1]
      st.text(f"The item with the SKU number {sku} is {i} and costs ${p}")
#for the customer page
if st.session_state.current_page == "customer":
    tab = st.sidebar.radio("Tabs",["Shop","Cart","Admin Login"])
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
            container.write(f"${price}")
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

    if tab=="Cart":
        st.session_state.current_page="Cart"
        st.rerun()
    #admin login page
    if tab == "Admin Login":
        admin_user = st.text_input("Enter the admin password, website will automatically send you to admin page if password is correct")
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
    purchase_click = st.button("Add to cart")
    price_without_sign = price.strip("$")
    if purchase_click and quantity > 0:
        st.session_state[purchase_item_session_state] = [quantity, float(price_without_sign)*quantity ]
    elif purchase_click and quantity <= 0:
        st.write("Invalid Quantity")
    if st.button("Buy More"):
        st.session_state.current_page = "customer"
        st.rerun()
    if st.button("Check out"):
        st.session_state.current_page = "Cart"
        st.rerun()

#Customer Checkout
elif st.session_state.current_page == "Cart":
    purchase_list = {}
    for key in st.session_state:
        if "buy_" in key:
            purchase_list[key] = st.session_state[key]
    st.write("Current items in your cart:")
    total=0
    for key in purchase_list:
        item = key.strip("buy_")
        price = purchase_list[key][1]
        quantity=purchase_list[key][0]
        st.text(f"{quantity} {item}: ${price}")
        total+=price
    st.write(f"Total: ${total}")
    if st.button("Buy More"):
        st.session_state.current_page = "customer"
        st.rerun()
    if st.button("Reset Cart"):
        for key in st.session_state:
            if "buy_" in key:
                del st.session_state[key]
        st.rerun()
    with st.form("my_form"):
        credit_card_number = st.text_input("Enter your credit card number (XXXX-XXXX-XXXX-XXXX)")
        valid_card = True
        card_no_dash = credit_card_number.replace('-',"")
        if card_no_dash.isdigit() == False:
            valid_card = False
        if len(card_no_dash) != 16:
            valid_card == False
        if valid_card == False:
            st.write("Your card is invalid, please try again")
        submit = st.form_submit_button("Submit")
        if submit and valid_card:
            st.write("card", credit_card_number)



#Admin Page
elif st.session_state.current_page == "admin_page":
    tab = st.sidebar.radio("Tabs",["Session State","Enter SKU","Check Items","Customer Page", "Add Items"])
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
        sku_quan=st.text_input("How much stock of the item is available")
        valid_quan=False
        if sku_quan.isdigit()==True:
            sku_quan=int(sku_quan)
            if sku_quan<=0:
                st.error("Invalid quantity")
            else:
                valid_quan=True
        if st.button("Enter into SKU") and valid_price and valid_quan:
            sku_enter(sku_input,sku_price,sku_quan)
    elif tab == "Check Items":
        a=st.text_input("Enter the SKU number of the item you want to check: ")
        if a.isdigit()==True:
            check(int(a))
    #To add items
    elif tab == 'Add Items':
        data_file = "inventory.json"
        if "inventory" not in st.session_state:
            if os.path.exists(data_file):
                with open(data_file, "r") as f:
                    st.session_state.inventory = json.load(f)
            else:
                st.session_state.inventory = []
        item_name = st.text_input("Item Name")
        quantity = st.number_input("Quantity", min_value=0)
        if st.button("Add Item"):
            st.session_state.inventory.append({"name": item_name,"quantity": quantity})
            with open(data_file, "w") as f:
                json.dump(st.session_state.inventory, f, indent=4)
            st.rerun()
        st.write(st.session_state.inventory)
     #To go back to customer page
    elif tab == "Customer Page":
        if st.button("Back to customer page"):
                st.session_state.current_page = "customer"
                st.rerun()
