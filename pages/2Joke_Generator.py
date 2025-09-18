import streamlit as st
import random

st.set_page_config(page_title="😂 Joke Generator", page_icon="🤣", layout="centered")

st.title("🎉 Fun Joke Generator 🤣")

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
    ("Why did the pie go to the dentist?","It needed a filling"),
    ("What do you call a dog that floats?","Good buoy"),
    ("How do cats like to bake cakes?","From scratch"),
    ("Why do pancakes always win in baseball","Cause they have the best batter🤣 "),
    ("What does a house wear?", "Address"),
    ("Why didn't the Sun go to college?","It already had a million degrees")
]

# --- Setup session state ---
if "remaining_jokes" not in st.session_state:
    st.session_state.remaining_jokes = jokes.copy()
    st.session_state.current_joke = None
    st.session_state.show_answer = False

# --- Layout with columns for buttons ---
col1, col2 = st.columns(2)

with col1:
    if st.button("🤣 Tell me a joke", use_container_width=True):
        st.session_state.show_answer = False  # reset answer view

        # Reset if no jokes left
        if not st.session_state.remaining_jokes:
            st.session_state.remaining_jokes = jokes.copy()

        # Pick a random joke from remaining
        joke = random.choice(st.session_state.remaining_jokes)
        st.session_state.remaining_jokes.remove(joke)
        st.session_state.current_joke = joke

with col2:
    # Show Answer / Next Joke button
    if st.session_state.current_joke and not st.session_state.show_answer:
        if st.button("🤓 Show Answer", use_container_width=True, key="show_btn"):
            st.session_state.show_answer = True

    elif st.session_state.current_joke and st.session_state.show_answer:
        if st.button("➡️ Next Joke", use_container_width=True, key="next_btn"):
            st.session_state.show_answer = False

            # Reset if no jokes left
            if not st.session_state.remaining_jokes:
                st.session_state.remaining_jokes = jokes.copy()

            # Pick a new random joke
            joke = random.choice(st.session_state.remaining_jokes)
            st.session_state.remaining_jokes.remove(joke)
            st.session_state.current_joke = joke

# --- Show the current joke ---
if st.session_state.current_joke:
    question, answer = st.session_state.current_joke

    st.markdown(
        f"<h2 style='color:brown;'>🤔 {question}</h2>",
        unsafe_allow_html=True
    )

    if st.session_state.show_answer:
        st.markdown(
            f"<h2 style='color:green;'>😂 {answer}</h2>",
            unsafe_allow_html=True
        )
