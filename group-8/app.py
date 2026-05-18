#checkout 14/5/2026 (Kaiser)
import streamlit as st

def ValidateType(a, myType:type):
    try:
        myType(a)
        return True
    except:
        return False

def ValidateError(a, myfunc):
    try:
        myfunc(a)
        return True
    except:
        return False

Page, Reciept = st.columns([2,1])

with Page:

    col1, col2 = st.columns(2)
    first_name = col1.text_input("", placeholder = "First name")
    last_name = col2.text_input("", placeholder = "Last name")
    email = st.text_input("Email", placeholder = "my.email@gmail.com")
    credit_card = st.text_input("credit card number", max_chars = 8)
    col3, col4 = st.columns(2)
    cvc = col3.text_input("cvc", max_chars = 3)
    expiry = col4.text_input("Expiry date", value = "mm/yy", max_chars = 5)
    promo_code = st.text_input("promo code", max_chars = 6)
    bundleContainer = st.container(border = True)
    with bundleContainer:
        st.title("Get food bundles!")
        st.markdown("*_its cheaper!_*")
        col5, col6 = st.columns(2)
        col5.markdown("hi guys")             #,text_alignment = "right", width=500)
        buttonBuy = st.button("Buy Now!", type = "primary", help = "BUYBUYBUY")

with Reciept:
    a = st.container(border = True, vertical = True)
    with a:
        st.title("Reciept")
        st.space("stretch")
        st.write("")
    a = st.button("submit")
if a:
  try:
    if not first_name:
      st.error("please enter first name!")
      raise Exception()
    if not last_name:
      st.error("please enter last name!")
      raise Exception()
    if email.strip("@.") != email or not email:
      st.error("please enter a valid e-mail address!")
      raise Exception()
    if not ValidateType(credit_card, int):
      st.error("please put in numbers for the credit card number")
      raise Exception()
    if len(credit_card) < 8:
      st.error("please input a valid credit card number!")
      raise Exception()
    if not ValidateType(cvc, int):
      st.error("please input a valid CVC number!")
      raise Exception()
    if not ValidateError(expiry, eval):
      st.error("please input a valid expiry date!")
      raise Exception()
    else:
      st.success("successful purchase!")
  except Exception:
      print("spoilage")
