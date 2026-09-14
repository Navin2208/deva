
import streamlit as st

st.title("Hello, World! 🌍")

st.write("Welcome to my first Streamlit app!")

# Display a world image
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
    caption="Earth — Our World",
    use_container_width=True
)