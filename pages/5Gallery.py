# pages/Gallery_Page.py

import streamlit as st

# --- Page configuration ---
st.set_page_config(
    page_title="Gallery",
    page_icon="🖼️",
    layout="centered"
)

# --- Page Title ---
st.title("Gallery")

# --- Show images from local directory ---
st.image("MyJourney.PNG", caption="📸 My Cricket Journey", use_container_width=True)
st.image("MyCodeJourney.PNG", caption="📸 My Coding Journey", use_container_width=True)
st.image("Poster.PNG", caption="📸 My Project Poster", use_container_width=True)

# --- Add Public App Link ---
st.markdown("---")
st.subheader("Try the Live App!")
st.markdown(
    "[🎮 Click here to open the live app](https://pi6vdljcqs8pyfvacpp2lb.streamlit.app/) ✅",
    unsafe_allow_html=True
)
st.markdown("Have fun playing and don't forget to fill the feedback survey! 🎉")
