
import streamlit as st

st.title("Welcome {username}", text_alignment = "center")

st.html(
"""
<style>
/* Remove default Streamlit top padding */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 0rem !important;
}

/* Center container layout for the reward card */
.center-card-wrapper {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
    margin: 20px 0 40px 0 !important;
    font-family: sans-serif;
}

/* The White Card Layout */
.reward-card {
    background: white !important;
    border-radius: 16px !important;
    border: 1px solid #E0E0E0 !important; /* Added subtle border since the green background is gone */
    box-shadow: 0 8px 24px rgba(0,0,0,0.08) !important;
    width: 100% !important;
    max-width: 500px !important;
    padding: 22px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
}

.card-left {
    display: flex !important;
    align-items: center !important;
    gap: 20px !important;
}

.trophy-circle {
    background-color: #FFF3E0 !important;
    width: 75px !important;
    height: 75px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 42px !important;
}

.points-text {
    text-align: left !important;
}

.points-number {
    color: #FFB300 !important;
    font-size: 46px !important;
    font-weight: 800 !important;
    line-height: 1 !important;
}

.points-label {
    color: #444444 !important;
    font-size: 22px !important;
    font-weight: 600 !important;
}

.coin-stack {
    font-size: 55px !important;
    display: flex !important;
}
</style>
"""
)
st.html(
"""
<div class="center-card-wrapper">
<div class="reward-card">
<div class="card-left">
<div class="trophy-circle">🏆</div>
<div class="points-text">
<div class="points-number">4560</div>
<div class="points-label">Points</div>
</div>
</div>
"""
)

if "cart" not in st.session_state:
        st.session_state.cart = {}


def add_to_cart(item):
    if item not in st.session_state.cart:
        st.session_state.cart[item] = 0
    st.session_state.cart[item] += 1
def remove_from_cart(item):
    if item not in st.session_state.cart:
        st.session_state.cart[item] = 0
    st.session_state.cart[item] -= 1

st.markdown("""
<style>
.st-key-redeem_button button p {
    font-family: times-new-roman;

}

.st-key-add-PopCorn button{
    background-color: rgb(255, 75, 75)
}

.st-key-remove-PopCorn button{
    background-color: rgb(75, 75, 255)

}

.st-key-add-PopCorn button p{
    color: white;
    font-family: comic-sans;
}

.st-key-remove-PopCorn button p{
    color: white;
    font-family: comic-sans;

}



.st-key-marquee-content {
    position: absolute;
    top: 100%;
    animation: vertical-marquee 5s linear infinite;
    transition: animation-duration 0.5s ease;
}


@keyframes vertical-marquee {
    0% {
        top: 5000px;
    }
    100% {
        top: -5000px; /* Adjust based on the number of lines */
    }
}

/* Slow on Hover */
.st-key-vertical-marquee:hover .st-key-marquee-content {
    animation-duration: 15s;
}


</style>

            """, unsafe_allow_html=True)

st.markdown("""

<style>
.st-key-home_header_buttons_PopCorn {
  display: flex;
}

.st-key-home_header_buttons_PopCorn .btn_home {
  position: relative;
}

.st-key-home_header_buttons_PopCorn .add-PopCorn {

  border-right: none;
}

.st-key-home_header_buttons_PopCorn .remove-PopCorn {

  height: 90%;
  top: 50%;
  transform: translateY(-50%);
  right: 0;
  z-index: 1;
}

.st-key-home_header_buttons_PopCorn .remove-PopCorn button {


}
        </style>

            """, unsafe_allow_html=True)


st.markdown("""
<style>
/* Target the popover with key 'redeem_button' and the container keys for each item */
.st-key-redeem_button .st-key-add-PopCorn button {
        border: 2px solid rgba(0,0,0,0.12);
        border-radius: 6px;
        position: relative; /* modify position only */
        top: 0; /* adjust vertical alignment here if needed */
}

.st-key-redeem_button .st-key-remove-PopCorn button {
        border: 2px solid rgba(0,0,0,0.12);
        border-radius: 6px;
        position: relative; /* modify position only */
        top: 0; /* adjust vertical alignment here if needed */
        right: 0; /* adjust horizontal alignment if necessary */
}
</style>
""", unsafe_allow_html=True)

biggest1, biggest2 = st.columns([7,3])
with biggest1:
    a = st.popover("_REDEEM_", key = "redeem_button", help = "CLICK TO REDEEM SELECTED ITEMS", type = 'primary', use_container_width = True, width = "stretch")

    for i, k in st.session_state.cart.items():
        if k > 0:
            with a.container(horizontal = True):
                st.markdown(f"<p style='font-family: comic-sans';>{i} x{k}</p>", unsafe_allow_html=True)
                with st.container(horizontal = True, key = f"home_header_buttons_{i}"):
                    st.button("+", key = f"add {i}", on_click = lambda: add_to_cart(i))
                    st.button("-", key = f"remove {i}", on_click = lambda: remove_from_cart(i))

    with st.container(border = True):
        st.markdown("<h3>ALL REDEEMABLE ITEMS</h3>", unsafe_allow_html=True)
        row1 = st.columns(3)
        row2 = st.columns(3)
        row3 = st.columns(3)
        for col in row1 + row2 + row3:

            tile = col.container(border = True)
            tile.write("PopCorn: 100 points")
            tile.image("https://tse2.mm.bing.net/th/id/OIP.Ywp9n6YB71vskStlgD10bAHaJ8?rs=1&pid=ImgDetMain&o=7&rm=3")
            tile.button("add to cart", key = f"add_to_cart_{col}", help = "CLICK TO ADD ITEM TO CART", type = 'primary', on_click = lambda: add_to_cart("PopCorn"))

with biggest2:
    biggest_container = st.container(border = True, height = 1085, autoscroll = True, key = "Vert")
    with biggest_container:
        st.html(
        """
        <style>
        .full-width-title-container {
            width: 100% !important;
            display: block !important;
            text-align: left !important; /* Change to center if you want it in the middle */
            margin: 25px 0 15px 0 !important;
            font-family: sans-serif;
        }

        .enlarged-title {
            font-size: 36px !important;  /* Controls the visual size of the words */
            font-weight: 800 !important;  /* Makes it bold and prominent */
            color: #111111 !important;    /* Clean dark text color */
            margin: 0 !important;
            padding: 0 !important;
            line-height: 1.2 !important;
        }
        </style>
        """
        )

        # 2. Render the element (Keep it left-aligned against the code margin to avoid markdown bugs)
        st.html(
        """
        <div class="full-width-title-container">
        <h2 class="enlarged-title">Featured Items</h2>
        </div>
        """
        )
        container_items1 = st.container(border = True, key = "container_items_1")
        with container_items1:
            st.write("PopCorn: 100 points")
            st.image("https://tse2.mm.bing.net/th/id/OIP.Ywp9n6YB71vskStlgD10bAHaJ8?rs=1&pid=ImgDetMain&o=7&rm=3")
            st.button("add to cart", help = "CLICK TO ADD ITEM TO CART", type = 'primary', on_click = lambda: add_to_cart("PopCorn"), key = "qjwifvnipq")

        container_items2 = st.container(border = True, key = "container_items_2")
        with container_items2:
            st.write("PopCorn: 100 points")
            st.image("https://tse2.mm.bing.net/th/id/OIP.Ywp9n6YB71vskStlgD10bAHaJ8?rs=1&pid=ImgDetMain&o=7&rm=3")
            st.button("add to cart", help = "CLICK TO ADD ITEM TO CART", type = 'primary', on_click = lambda: add_to_cart("PopCorn"), key = "neuhfiusvboiea")

        container_items3 = st.container(border = True, key = "container_items_3")
        with container_items3:
            st.write("PopCorn: 100 points")
            st.image("https://tse2.mm.bing.net/th/id/OIP.Ywp9n6YB71vskStlgD10bAHaJ8?rs=1&pid=ImgDetMain&o=7&rm=3")
            st.button("add to cart", help = "CLICK TO ADD ITEM TO CART", type = 'primary', on_click = lambda: add_to_cart("PopCorn"), key = "ihewiovbwieo")

        container_items4 = st.container(border = True, key = "container_items_4")
        with container_items4:
            st.write("PopCorn: 100 points")
            st.image("https://tse2.mm.bing.net/th/id/OIP.Ywp9n6YB71vskStlgD10bAHaJ8?rs=1&pid=ImgDetMain&o=7&rm=3")
            st.button("add to cart", help = "CLICK TO ADD ITEM TO CART", type = 'primary', on_click = lambda: add_to_cart("PopCorn"), key = "okwengiwqhgoq")
