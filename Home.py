# --- Import required libraries ---
import streamlit as st

# --- HOME PAGE ---
st.title("Welcome to My Year 6 Passion Project!")

# Short introduction
st.write("""
Hello! My name is **  ** and this is my **Cricket Simulator App**.  

This app is my **Year 6 passion project**, where I learned how to:
- Code in **Python**
- Use **Streamlit** to make interactive web apps
- Work with **data** like runs, wickets, and scores
- Make fun **charts and graphs** to visualize cricket matches
""")

# Personal journey section
st.subheader("My Learning Journey")
st.write("""
When I started this project, I had never made a game or chart before.  
I learned step by step:
1. How to **take input** from the user using Streamlit.
2. How to **simulate cricket matches** with random runs and wickets.
3. How to **display scores and match results** in a fun way.
4. How to create **graphs** like Runs per Ball and Highest Scoring Over.
5. How to **experiment with colors** and make the app look lively.
""")

# Motivation / reflection
st.subheader("Why I Chose This Project")
st.write("""
I love cricket and wanted to combine it with coding.  
This project taught me that **coding can be fun and creative**.  
I can see how math, logic, and technology work together to make games and simulations.
""")

# Thank you note
st.subheader("Thank You")
st.write(""" TYPE HERE ...................""")

st.subheader("Gallery")
# Show personal image from local directory
st.image("MyJourney.PNG", caption="📸 My Cricket Journey", use_container_width =True)

# Show personal image from local directory

st.image("MyCodeJourney.PNG", caption="📸 My Coding Journey", use_container_width =True)
