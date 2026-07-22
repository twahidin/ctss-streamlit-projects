import streamlit as st
import os
from datetime import date


#puts the skus in app.txt into session state


if "inventory_loaded" not in st.session_state:
    if os.path.exists("app.txt"):
        with open("app.txt","r") as f:
            for line in f:
                if " : " not in line:
                    continue

                key, val = line.strip().split(" : ")
                if key == "money":
                    st.session_state[key] = int(val)
                try:
                    int(key)
                    item, price, stock = val.strip("[]").split(",")
                    st.session_state[key] = [item, price,stock]
                except ValueError:
                    st.session_state[key] = val


    st.session_state.inventory_loaded = True
#save app.txt
def save_txt():
    with open("app.txt", "w") as f:
        for key in st.session_state:
            if key.isdigit():
                value = st.session_state[key]

                if isinstance(value, list):
                    item = value[0]
                    price = value[1]
                    stock = value[2]

                    f.write(f"{key} : [{item},{price},{stock}]\n")
            if key == "money":
                value = st.session_state[key]
                f.write(f"{key} : {value}\n")
#find sku based off of name
def find_sku(name):
    for key in st.session_state:
        if key.isdigit() == True:
            value = st.session_state[key]
            if not isinstance(value,list):
                continue

            item_name = value[0]
            if item_name == name:
                return key

#update money
def update_money(operation,change):
    current = st.session_state["money"]
    if operation == "add":
        st.session_state["money"] = current+change
    elif operation == "minus":
        st.session_state["money"] = current-change
    save_txt()

#update stock
def update_stock(sku,change,operation):
    list = st.session_state[sku]
    name = list[0]
    price = list[1]
    quantity = int(list[2])
    quantity_change = int(change)
    if operation == "minus":
        quantity -= quantity_change
    elif operation == "add":
        quantity += quantity_change
    list = [name,price,str(quantity)]
    st.session_state[sku] = list
    save_txt()

#Sends email (this was so hard LOL)
# def send_email(recipient, subject, body):
#     sender = "inventorytrackergmail@gmail.com"
#     # Use an App Password here
#     password = "only ziyi has this"


#     message = MIMEText(body)
#     message['Subject'] = subject
#     message['From'] = sender
#     message['To'] = recipient
#     try:
#         # Connect to Gmail's server
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(sender, password)
#             server.send_message(message)
#         st.success("Email sent successfully!")
#     except Exception as exception:
#         st.error(f"An error occurred: {exception}")

# send email
def email_page():
    with st.form("email_form"):
        recipient = st.text_input("To:")
        subject = st.text_input("Subject:")
        body = st.text_area("Message:")
        submitted = st.form_submit_button("Send Email")

    if submitted:
        st.success('Submitted!')
        #send_email(recipient, subject, body)
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
        st.success(f"{item} has been stored under the SKU number {sku(item)} with a stock of {stock}")
        with open("app.txt","a") as f:
            f.write(f"{sku(item)} : [{item},{price},{stock}]\n")
    else:
        st.error(f"{item} is already stored under the SKU number {sku(item)}")
#use sku_enter(item name,price)
#to check items
def check(sku):
  if sku not in st.session_state:
      st.error("This SKU number does not exist. Please ensure you have typed it correctly and try again.")
  else:
      name=st.session_state[sku][0]
      price =st.session_state[sku][1]
      stock = st.session_state[sku][2]
      st.success(f"The item with the SKU number {sku} is {name} and costs ${price}, and we have {stock} left")
#container for the customer shop format
def item_container(item,price,stock):
    global container
    container = st.container(border=True)
    container.write(item)
    container.write(f"${price}")
    container.write(stock)

#customer shop code
def customer_shop():
    searchbar = ""
    searchbar = st.text_input("Search", placeholder = 'Search Items')
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





    with col1:
        count = 0
        for key in item_dict:
            if count % 3 == 0:
                if int(item_dict[key][2]) == 0:
                    stock = "Out of stock"
                else:
                    stock = item_dict[key][2]
                item_container(item_dict[key][0],item_dict[key][1],stock)

                if container.button("Buy", key=count) and int(item_dict[key][2]) != 0:
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
                if int(item_dict[key][2]) == 0:
                    stock = "Out of stock"
                else:
                    stock = item_dict[key][2]
                item_container(item_dict[key][0],item_dict[key][1],stock)

                if container.button("Buy", key=count) and int(item_dict[key][2]) != 0:
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
                if int(item_dict[key][2]) == 0:
                    stock = "Out of stock"
                else:
                    stock = item_dict[key][2]
                item_container(item_dict[key][0],item_dict[key][1],stock)

                if container.button("Buy", key=count) and int(item_dict[key][2]) != 0:
                    price = item_dict[key][1]
                    st.session_state.customer_item_price = price
                    st.session_state.customer_item = key
                    st.session_state.current_page = "purchase"
                    st.rerun()
            count += 1

#admin login page
def admin_login():
    user_input = st.text_input("Admin Username", placeholder = 'Admin Username').lower()
    password_input = st.text_input("Password", placeholder = 'Password')
    admin_pass = "e"
    admin_user = "admin123"
    if password_input != "" and user_input != "":
        if password_input == admin_pass and user_input == admin_user:
            st.success("Admin permissions granted")
            st.session_state.current_page = "admin_page"
            st.rerun()
        elif password_input != admin_pass and user_input != admin_user:
            st.error("Incorrect Password and user")
        elif password_input != admin_pass:
            st.error("Incorrect Password")
        elif user_input != admin_user:
            st.error("Invalid User")

def customer_buy():
    purchase_item = st.session_state.customer_item
    purchase_sku = find_sku(purchase_item)
    price = st.session_state.customer_item_price
    current_stock = st.session_state[purchase_sku][2]
    st.write("You are buying:", purchase_item, "at $",price)
    quantity = st.slider("Enter the amount you would like to buy (max 100)")
    purchase_item_session_state = "buy_"+purchase_item
    previous_quantity = 0
    if purchase_item_session_state in st.session_state:
        purchase_item_list = st.session_state[purchase_item_session_state]
        previous_quantity = purchase_item_list[0]
    if not previous_quantity + quantity > int(current_stock):

        purchase_click = st.button("Add to cart")

        price_without_sign = str(price).strip("$")

        if purchase_click and quantity > 0:
            if purchase_item_session_state in st.session_state:
                purchase_item_list = st.session_state[purchase_item_session_state]
                previous_quantity = purchase_item_list[0]
                st.session_state[purchase_item_session_state] = [quantity+previous_quantity, float(price_without_sign)*(quantity+previous_quantity),purchase_sku]
            else:
                st.session_state[purchase_item_session_state] = [quantity, float(price_without_sign)*quantity,purchase_sku]
            st.write("Added to cart!")
            st.write("You currently have", quantity+previous_quantity, "amount(s) of", purchase_item,"added!")
        elif purchase_click and quantity <= 0:
            st.write("Invalid Quantity")
    else:
        st.write("You are buying more than we currently have!")
    if st.button("Buy More"):
        st.session_state.current_page = "customer"
        st.rerun()
    if st.button("Check out"):
        st.session_state.current_page = "Cart"
        st.rerun()
#for the customer page
if st.session_state.current_page == "customer":
    tab = st.sidebar.radio("Tabs",["Shop","Cart","Admin Login"])
    #shop page (home page for them to buy things)
    if tab == "Shop":
        customer_shop()

    if tab=="Cart":
        st.session_state.current_page="Cart"
        st.rerun()
    #admin login page
    if tab == "Admin Login":
        admin_login()

#buy screen when they click "buy"
elif st.session_state.current_page == "purchase":
    customer_buy()
#Customer Checkout
elif st.session_state.current_page == "Cart":
    purchase_list = {}
    for key in st.session_state:
        if "buy_" in key:
            purchase_list[key] = st.session_state[key]
    st.write("Current items in your cart:")
    total=0
    for key in purchase_list:
        item = key.replace("buy_","",1)
        price = purchase_list[key][1]
        quantity=purchase_list[key][0]
        st.text(f"{quantity} {item}: ${price}")
        total+=price
    st.write(f"Total: ${total}")
    if st.button("Buy More"):
        st.session_state.current_page = "customer"
        st.rerun()

    if st.button("Reset Cart (this also brings u back to customer page btw)"):
        for key in st.session_state:
            if "buy_" in key:
                del st.session_state[key]
            st.session_state.current_page = "customer"
            st.rerun()
        st.rerun()
    with st.form("my_form"):
        credit_card_number_input = st.text_input("Credit Card Number", placeholder = 'XXXX-XXXX-XXXX-XXXX')
        email_address_customer_input = st.text_input("Email", placeholder = 'Email')
        name_customer_input = st.text_input("Name on Card", placeholder = 'Name')
        exp_date_input = st.date_input("Expiry Date",min_value = date.today())
        cvc_input = st.text_input("CVV/CCV", placeholder = 'CVV/CCV')
        submit = st.form_submit_button("Submit")
        if submit:
            valid_name = False
            valid_card = False
            valid_email = False
            valid_expiry = False
            valid_cvc = False
            #10000 validations
            if len(cvc_input) == 3 and cvc_input.isdigit() == True:
                valid_cvc = True
            if exp_date_input >= date.today():
                valid_expiry = True
            if name_customer_input.isdigit() == False and name_customer_input != "":
                valid_name = True
            if (len(credit_card_number_input) == 19 and credit_card_number_input[4] == "-" and credit_card_number_input[9] == "-" and credit_card_number_input[14] == "-" and credit_card_number_input.replace("-", "").isdigit()):
                valid_card = True
            at_pos = -1
            dot_pos = -1
            at_pos = email_address_customer_input.find("@")
            dot_pos = email_address_customer_input.find(".")
            if not at_pos < 1 and not dot_pos < 1 and dot_pos > at_pos:
                valid_email = True


            if valid_cvc and valid_card and valid_email and valid_name and valid_expiry:
                #st.success("Thanks for the purchase! We have sent you an email regarding this purchase")
                email_address_customer = email_address_customer_input
                credit_card_number = credit_card_number_input
                sensored_credit_card_number = "****-****-****-" + credit_card_number[-4:]
                send_message = f"""
                Thank you for your purchase with the goated shop.

                Your shipment should arrive at your house in about 3 to 5 business days.

                If you encounter any enquiries, feel free to contact us at 67676767.

                The credit card number you inputted is {sensored_credit_card_number}
                """
                #send_email(email_address_customer, "Purchase with the goated shop", send_message)
                keys_to_delete = []

                for key in st.session_state:
                    if "buy_" in key:
                        buy_list = st.session_state[key]
                        quantity = buy_list[0]
                        sku = buy_list[2]
                        update_stock(sku, quantity, "minus")
                        keys_to_delete.append(key)

                for key in keys_to_delete:
                    del st.session_state[key]
                    update_money("add",total)
                st.success(f"Dear {name_customer_input} {send_message}")


            if not valid_card:
                st.write("Your card is invalid")
            if not valid_email:
                st.write("Your email is invalid")
            if not valid_name:
                st.write("Your name is invalid (numbers)")
            if not valid_expiry:
                st.write("Your expiry date is invalid")
            if not valid_cvc:
                st.write("Your cvc/ccv number is invalid")
    if st.button("Back to home page"):
            st.session_state.current_page = "customer"
            st.rerun()
#Admin Page
elif st.session_state.current_page == "admin_page":
    tab = st.sidebar.radio("Tabs",["Session State","Import stocks","Enter SKU","Remove SKU","Check Items","Customer Page","Money"])
    if tab == "Session State":
        st.write("Session state:")
        st.write(st.session_state)
        if st.button("free money"):

            if "money" in st.session_state:
                st.error('Money does not grow on trees.')
            else:
                st.session_state["money"] = 1000
                st.success('$1000 added to the account!')


    #money
    elif tab == "Money":
        st.write("We currently have:")
        st.success(f'${st.session_state["money"]}')
    #Input SKU
    elif tab == "Enter SKU":
        st.write("Fill in Item Info")
        sku_input = st.text_input("Name of Item", placeholder = "Name")
        sku_price = st.number_input("Price of Item", min_value = 0.01, format = "%0.2f", placeholder = 'Price')
        sku_quan = st.number_input("Stock", min_value = 1, placeholder = 'Stock')
        #Sets price to 2 d.p.
        sku_input_no_space = sku_input.replace(" ","")
        if st.button('Submit'):
            if sku_input == '' or not sku_input_no_space.isalnum():
                st.error('Invalid Name')
            else:
                sku_enter(sku_input,sku_price,sku_quan)
    #check SKU
    elif tab == "Check Items":
        sku=st.text_input("Enter the SKU number of the item you want to check: ", placeholder = 'SKU')
        if sku.isdigit()==True:
            check(sku)
        name = st.text_input("Enter the name of the item", placeholder = 'Item Name').lower()
        if name != "":
            st.write("sku:", find_sku(name))

    #remove sku
    elif tab == "Remove SKU":
        item_remove = st.text_input("Exact Name of Item", placeholder = 'Item Name')
        if item_remove != "":
            sku = find_sku(item_remove)
            st.session_state.pop(sku)
            st.success("Success!")
            save_txt()
    #To go back to customer page
    elif tab == "Customer Page":
        if st.button("Back to customer page"):
                st.session_state.current_page = "customer"
                st.rerun()

    elif tab == "Import stocks":
        searchbar = ""
        searchbar = st.text_input("Search", placeholder = 'Search Items')
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
                    item_container(item_dict[key][0],item_dict[key][1],item_dict[key][2])
                    if container.button("Buy more", key=count):
                        price = item_dict[key][1]
                        st.session_state.admin_item_price = float(price)/2
                        st.session_state.admin_item = key
                        st.session_state.current_page = "admin_purchase"
                        st.rerun()
                count += 1

        with col2:
            count = 0
            for key in item_dict:
                if count % 3 == 1:
                    item_container(item_dict[key][0],item_dict[key][1],item_dict[key][2])
                    if container.button("Buy more", key=count):
                        price = item_dict[key][1]
                        st.session_state.admin_item_price = float(price)/2
                        st.session_state.admin_item = key
                        st.session_state.current_page = "admin_purchase"
                        st.rerun()
                count += 1
        with col3:
            count = 0
            for key in item_dict:
                if count % 3 == 2:
                    item_container(item_dict[key][0],item_dict[key][1],item_dict[key][2])
                    if container.button("Buy more", key=count):
                        price = item_dict[key][1]
                        st.session_state.admin_item_price = float(price)/2
                        st.session_state.admin_item = key
                        st.session_state.current_page = "admin_purchase"
                        st.rerun()
                count += 1
elif st.session_state.current_page == "admin_purchase":
    purchase_item = st.session_state.admin_item
    purchase_sku = find_sku(purchase_item)
    price = st.session_state.admin_item_price
    st.write("You are buying:", purchase_item, "at $",price)
    quantity = st.text_input("Enter the amount you would like to buy")
    if quantity.isdigit() == False:
        st.write("quantity is invalid")
    else:
        quantity = int(quantity)
        purchase_item_session_state = "admin_buy_"+purchase_item
        purchase_click = st.button("Add to cart")
        price_without_sign = str(price).strip("$")
        previous_quantity = 0
        if purchase_click and int(quantity) > 0:
            if purchase_item_session_state in st.session_state:
                purchase_item_list = st.session_state[purchase_item_session_state]
                previous_quantity = int(purchase_item_list[0])
                st.session_state[purchase_item_session_state] = [quantity+previous_quantity, float(price_without_sign)*int(quantity+previous_quantity),purchase_sku]
                st.write("Added to cart!")
                st.write("You currently have", quantity+int(previous_quantity), "amount(s) of", purchase_item,"added!")
            else:
                st.session_state[purchase_item_session_state] = [quantity, float(price_without_sign)*int(quantity),purchase_sku]

        elif purchase_click and quantity <= 0:
            st.write("Invalid Quantity")
        if st.button("Buy More"):
            st.session_state.current_page = "admin_page"
            st.rerun()
        if st.button("Check out"):
            st.session_state.current_page = "admin_cart"
            st.rerun()
elif st.session_state.current_page == "admin_cart":
    admin_purchase_list = {}
    for key in st.session_state:
        if "admin_buy_" in key:
            admin_purchase_list[key] = st.session_state[key]
    st.write("Current items in your cart:")
    total=0
    for key in admin_purchase_list:
        item = key.replace("admin_buy_","",1)
        price = admin_purchase_list[key][1]
        quantity=admin_purchase_list[key][0]
        st.text(f"{quantity} {item}: ${price}")
        total+=price
    st.write(f"Total: ${total}")
    if st.button("Buy More"):
        st.session_state.current_page = "admin_page"
        st.rerun()
    if st.button("Reset Cart"):
        for key in st.session_state:
            if "admin_buy_" in key:
                del st.session_state[key]
        st.rerun()

    st.write(total)
    not_poor = True
    if st.session_state["money"] < total:
        not_poor = False
    if not_poor == False:
        st.write("You do not have enough money!")
    if st.button("Buy item(s)") and not_poor:
        current_sku = find_sku(item)
        update_stock(current_sku,int(quantity),"add")
        update_money("minus",total)
        st.rerun()
