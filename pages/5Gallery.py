# pages/Gallery_Page.py

import streamlit as st
import os
# --- Page configuration ---
st.set_page_config(
    page_title="Gallery",
    page_icon="🖼️",
    layout="centered"
)

# --- Page Title ---
st.title("Gallery")

current_dir = os.path.dirname(__file__)

# --- Load images from images folder ---
poster_path = os.path.join(current_dir, "..", "images", "Poster.PNG")
cricket_path = os.path.join(current_dir, "..", "images", "MyJourney.PNG")
code_path = os.path.join(current_dir, "..", "images", "MyCodeJourney.PNG")

st.image(cricket_path, caption="📸 My Cricket Journey", use_container_width=True)
st.image(code_path, caption="📸 My Coding Journey", use_container_width=True)
st.image(poster_path, caption="📸 My Project Poster", use_container_width=True)

# --- Add Public App Link ---
st.markdown("---")
st.subheader("Try the Live App!")
st.markdown(
    "[🎮 Click here to open the live app](https://pi6vdljcqs8pyfvacpp2lb.streamlit.app/) ✅",
    unsafe_allow_html=True
)
st.markdown("Have fun playing and don't forget to fill the feedback survey! 🎉")
