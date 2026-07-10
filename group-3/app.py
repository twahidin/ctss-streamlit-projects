import streamlit as st
import os


#puts the skus in app.txt into session state
if "inventory_loaded" not in st.session_state:
    if os.path.exists("app.txt"):
        with open("app.txt","r") as f:
            for line in f:
                if " : " not in line:
                    continue
                key, val = line.strip().split(" : ")
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
        st.write(67)
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



    with col1:
        count = 0
        for key in item_dict:
            if count % 3 == 0:
                item_container(item_dict[key][0],item_dict[key][1],item_dict[key][2])
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
                item_container(item_dict[key][0],item_dict[key][1],item_dict[key][2])
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
                item_container(item_dict[key][0],item_dict[key][1],item_dict[key][2])
                if container.button("Buy", key=count):
                    price = item_dict[key][1]
                    st.session_state.customer_item_price = price
                    st.session_state.customer_item = key
                    st.session_state.current_page = "purchase"
                    st.rerun()
            count += 1

#admin login page
def admin_login():
    user_input = st.text_input("Enter the admin user and")
    password_input = st.text_input("Enter the admin password, website will automatically send you to admin page if password is correct")
    admin_pass = "e"
    admin_user = "admin123"
    if password_input != "" and user_input != "":
        if password_input == admin_pass and user_input == admin_user:
            st.write("yay ur an admin")
            st.session_state.current_page = "admin_page"
            st.rerun()
        elif password_input != admin_pass and user_input != admin_user:
            st.write("Incorrect Password and user")
        elif password_input != admin_pass:
            st.write("Incorrect Password")
        elif user_input != admin_user:
            st.write("user is invalid")

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
    if st.button("Reset Cart"):
        for key in st.session_state:
            if "buy_" in key:
                del st.session_state[key]
        st.rerun()
    st.session_state
    with st.form("my_form"):
        credit_card_number_input = st.text_input("Enter your credit card number (XXXX-XXXX-XXXX-XXXX)")
        email_address_customer_input = st.text_input("Enter your email address")
        valid_card = False
        valid_email = False
        #validation yay
        if (len(credit_card_number_input) == 19 and credit_card_number_input[4] == "-" and credit_card_number_input[9] == "-" and credit_card_number_input[14] == "-" and credit_card_number_input.replace("-", "").isdigit()):
            valid_card = True
        at_pos = -1
        dot_pos = -1
        at_pos = email_address_customer_input.find("@")
        dot_pos = email_address_customer_input.find(".")
        if not at_pos < 1 and not dot_pos < 1 and dot_pos > at_pos:
            valid_email = True

        submit = st.form_submit_button("Submit")

        if submit and valid_card and valid_email:
            st.write("Thanks for the purchase! We have send you an email regarding this purchase")
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
            for key in st.session_state:
                if "buy_" in key:
                    buy_list = st.session_state[key]
                    quantity = buy_list[0]
                    sku = buy_list[2]
                    update_stock(sku,quantity,"minus")
            for key in st.session_state:
                if "buy_" in key:
                    del st.session_state[key]
            update_money("add",total)

        elif submit and not valid_card and valid_email and valid_name:
            st.write("Invalid Card, Please try again.")
        elif submit and valid_card and not valid_email and valid_name:
            st.write("Invalid email, Please try again")
        elif submit and not valid_card and not valid_email and valid_name:
            st.write("Invalid card and email, Please try again")
        elif submit and valid_card and not valid_email and not valid_name:
            st.write("Invalid email and name, Please try again")
        elif submit and not valid_card and not valid_email and not valid_name:
            st.write("Invalid email, name and card, Please try again")
        elif submit and not valid_card and valid_email and not valid_name:
            st.write("Invalid card and name, Please try again")
        elif submit and valid_card and valid_email and not valid_name:
            st.write("Invalid name, Please try again")

#Admin Page
elif st.session_state.current_page == "admin_page":
    tab = st.sidebar.radio("Tabs",["Session State","Import stocks","Enter SKU","Check Items","Customer Page", "Add Items"])
    if tab == "Session State":
        st.write("Session state:")
        st.write(st.session_state)
        if st.button("free money"):
            st.session_state["money"] = 1000
        st.write("app.txt")
        if os.path.exists("app.txt"):
            with open("app.txt", "r") as f:
                for i in f:
                    st.write(i)
        else:
            st.warning("No file found yet.")
        if os.path.exists("app.txt"):
            with open("app.txt", "r") as f:
                file_contents = f.read()
            st.download_button(
                label="Download app.txt",
                data=file_contents,
                file_name="app.txt",
                mime="text/plain"
            )
    #Input SKU
    elif tab == "Enter SKU":
        st.write("Fill in Item Info")
        sku_input = st.text_input("Name of Item", placeholder = "Name")
        sku_price = st.number_input("Price of Item", min_value = 0.01, format = "%0.2f")
        sku_quan = st.number_input("Stock", min_value = 1)
        #Sets price to 2 d.p.
        if st.button('Submit'):
            if sku_input == '' or sku_input == '0123456789':
                st.error('Invalid Name')
            else:
                sku_enter(sku_input,sku_price,sku_quan)
    elif tab == "Check Items":
        a=st.text_input("Enter the SKU number of the item you want to check: ")
        if a.isdigit()==True:
            check(a)

    #To go back to customer page
    elif tab == "Customer Page":
        if st.button("Back to customer page"):
                st.session_state.current_page = "customer"
                st.rerun()

    elif tab == "Import stocks":
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
    st.session_state
    st.write(total)
    st.write("Click the buy items(s) button twice")
    if st.button("Buy item(s)"):
        current_sku = find_sku(item)
        update_stock(current_sku,int(quantity),"add")
        update_money("minus",total)
