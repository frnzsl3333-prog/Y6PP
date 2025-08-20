import streamlit as st
import random
import time

st.title("Joke Generator")

# --- My list of jokes (question, answer) ---
jokes = [
    ("Why don’t skeletons fight each other?", "They don’t have the guts."),
    ("Why was the math book sad?", "Because it had too many problems."),
    ("Why did the computer go to the doctor?", "Because it caught a virus!"),
    ("What did 20 do when it was hungry?", "Twenty-eight."),
    ("Why is grass so dangerous?", "Because it's full of blades!"),
    ("Why are mountains so funny?", "They’re hill areas."),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
    ("Why did the student eat his homework?", "Because the teacher said it was a piece of cake!"),
    ("Why can’t you give Elsa a balloon?", "Because she’ll let it go!"),
    ("Why did the bicycle fall over?", "Because it was two-tired!"),
    ("Why can’t your nose be 12 inches long?", "Because then it would be a foot!"),
    ("Why did the golfer bring an extra pair of pants?", "In case he got a hole in one!"),
    ("Why did the cookie go to the hospital?", "Because it felt crumby!"),
    ("Why don’t eggs tell jokes?", "They might crack up!"),
    ("Why did the tomato turn red?", "Because it saw the salad dressing!"),
    ("Why did the music teacher go to jail?", "Because she got caught with the wrong notes!"),
    ("Why did the astronaut break up with his girlfriend?", "He needed space!"),
    ("Why did the broom get late?", "It overswept!"),
    ("Why did the jellybean go to school?", "Because it wanted to be a smartie!"),
    ("Why did the pirate go to school?", "To improve his arrrrrt skills!"),
    ("Why did the penguin cross the road?", "To go with the floe!"),
    ("Why did the banana go to the doctor?", "Because it wasn’t peeling well!"),
    ("Why was the stadium so cool?", "Because it was full of fans!"),
    ("Why did the book join the football team?", "Because it had a lot of pages!"),
]


# Placeholders
q_space = st.empty()
a_space = st.empty()
ans_space = st.empty()

if st.button("Tell me a joke"):
    # Clear old joke
    q_space.empty()
    a_space.empty()
    ans_space.empty()

    # Pick a random joke
    question, answer = random.choice(jokes)

    # Show the question 
    q_space.markdown(f"<h3 style='color:brown;'><b>{question}</b></h3>", unsafe_allow_html=True)

    # Show thinking animation
    for dots in ["🤔", "🤔.", "🤔..", "🤔..."]:
        a_space.write(dots + " Thinking...")
        time.sleep(1.5)

    # Show the answer
    a_space.empty()
    ans_space.markdown(f"<h2 style='color:green;'><b>{answer}</b></h2>", unsafe_allow_html=True)


