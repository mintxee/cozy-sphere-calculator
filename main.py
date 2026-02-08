import streamlit as st
import math
from streamlit_emoji_float import emoji_float

# ---------- Page Config ----------
st.set_page_config(
    page_title="Sphere Calculator",
    page_icon="🍥",
    layout="centered"
)

st.title("🍥 Sphere Calculator")

# ---------- Inputs ----------

if 'Radius' not in st.session_state:
    st.session_state.number_input = 0.00

def reset_number_input():
    st.session_state.number_input = 0

radius = st.number_input("Radius",min_value=0.00, format="%.2f", step=0.10, key="Radius")


# ---------- Buttons ----------
col1, col2= st.columns(2)

with col1:
    if st.button("Calculate Volume"):
        try:
            volume = (4/3)*math.pi*(radius**3)
            st.success(f"Volume {volume:.2f} calculated!")
            emoji_float(
                emojis=["💗", "✨", "🍥"],
                count=5
            )
        except TypeError:
            st.error("Invalid input")

with col2:
    if st.button("Calculate Surface Area"):
        try:
            surface_area = 4*math.pi*(radius**2)
            st.success(f"Surface Area {surface_area:.2f} calculated!")
            emoji_float(
                emojis=["💗","✨","🍥"],
                count=5
            )
        except TypeError:
            st.error("Invalid input")

st.button("Reset ↺", on_click=reset_number_input)

# ---------- UI Set-up ----------

st.markdown("""
<style>
.stApp {
    background-color: #fff5f7;
}
.footer {
    width: 100%;
    text-align: center;
    color: #F4ABC4;
    fontsize: 2px;
}
</style>
<div class="footer">
    Made by @mint.xee &lt;3
</div>
""", unsafe_allow_html=True)
