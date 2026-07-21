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
        col5.image("https://rrojin.tistory.com/m/77")
        col6.image("data:image/png;base64,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")
        buttonBuy = st.button("Buy Now!", type = "primary", help = "BUYBUYBUY")

with Reciept:
    a = st.container(border = True)
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


