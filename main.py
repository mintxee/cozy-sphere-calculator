import streamlit as st
import math
from streamlit_emoji_float import emoji_float
import plotly.graph_objects as go
import numpy as np


# ---------- Page Config ----------
st.set_page_config(
    page_title="Sphere Calculator",
    page_icon="🍥",
    layout="centered"
)

st.title("🍥 Sphere Calculator")

# ---------- Inputs ----------

if "Radius" not in st.session_state:
    st.session_state.Radius = 0.00

def reset_radius():
    st.session_state.Radius = 0.00

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

st.button("Reset ↺", on_click=reset_radius)

# ---------- Graph ----------
center = (0, 0, 0)

def create_sphere_data(radius, resolution=100):
    theta = np.linspace(0, 2*np.pi, resolution)
    phi = np.linspace(0, np.pi, resolution)
    theta, phi = np.meshgrid(theta, phi)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)
    return x, y, z

st.write("Radius =", radius)

if radius > 0:
    x_sphere, y_sphere, z_sphere = create_sphere_data(radius)

    fig = go.Figure(
        data=[go.Surface(x=x_sphere, y=y_sphere, z=z_sphere, colorscale="blues")]
    )

    fig.update_layout(
        scene=dict(aspectmode="data"),
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Enter a radius to visualize sphere.")

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