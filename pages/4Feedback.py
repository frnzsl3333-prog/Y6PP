# pages/Thank_You.py

import streamlit as st
from PIL import Image
import os

# --- Page configuration ---
st.set_page_config(
    page_title="Thank You!",
    page_icon="🎉",
    layout="centered"
)

# --- Page Title ---
st.title("🎉 Thank You for Playing!")

# --- Description / Reminder ---
st.markdown("""
Thank you for trying my **Year 6 Game Project**! 🏏😂  

I hope you had fun with the **Cricket Scoreboard** and **Joke Generator** apps.  

Please **remember to fill out the feedback survey** ✅""")

# --- Load and Display Image ---
# Image should be in your repo folder: 'images/Feedback.JPEG'
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "..", "images", "Feedback.JPG")  # Relative path from pages folder

try:
    feedback_img = Image.open(image_path)
    st.image(feedback_img, caption="Feedback Reminder", use_container_width=True)
except FileNotFoundError:
    st.error("Feedback image not found! Please make sure 'images/Feedback.JPEG' exists in the repo.")
