import streamlit as st
import random
from german_words_500 import german_words

st.set_page_config(
    page_title="German Vocabulary Quiz",
    page_icon="🇩🇪"
)

st.title("🇩🇪 German Vocabulary Quiz")

# ---------------- SESSION STATES ----------------

if "score" not in st.session_state:
    st.session_state.score = 0

if "show_next" not in st.session_state:
    st.session_state.show_next = False

if "remaining_words" not in st.session_state:
    st.session_state.remaining_words = list(german_words.keys())

if "word" not in st.session_state:
    st.session_state.word = random.choice(
        st.session_state.remaining_words
    )
    st.session_state.remaining_words.remove(
        st.session_state.word
    )

# ---------------- MESSAGES ----------------

correct_messages = [
    "Sehr gut! 🇩🇪",
    "Excellent! 🔥",
    "Germany is getting closer! 🚀",
    "Vocabulary unlocked! ⭐",
    "Perfect answer! 👏",
    "B2 Warrior! ⚔️",
    "Outstanding! 🎉"
]

wrong_messages = [
    "Kyu nahi ho rahe padhaye 😭",
    "Germany jaake kya bologe bhai? 😂",
    "Bro, revise this one again!",
    "Aaj padhai ka mood nahi hai kya? 😅",
    "Duolingo owl is disappointed 🦉",
    "The word is crying in the corner 😭",
    "Phone band karo aur padhai karo 😂"
]

# ---------------- PROGRESS ----------------

total_words = len(german_words)
progress = st.session_state.score / total_words

st.progress(progress)
st.write(
    f"Score: {st.session_state.score} / {total_words}"
)

# ---------------- QUIZ ----------------

word = st.session_state.word
correct_answer = german_words[word]

st.header(word)

with st.form("quiz_form"):
    answer = st.text_input(
        "Enter the English meaning:"
    )
    submitted = st.form_submit_button(
        "Check"
    )

if submitted:

    if answer.strip().lower() == correct_answer.lower():

        st.success(
            random.choice(correct_messages)
        )

        st.session_state.score += 1

        if st.session_state.score == 10:
            st.balloons()
            st.success(
                "10 correct! You're on fire! 🔥"
            )

        if st.session_state.score == 50:
            st.balloons()
            st.success(
                "50 words mastered! 🇩🇪"
            )

        if st.session_state.score == 100:
            st.balloons()
            st.success(
                "100 words mastered! Legendary! 🏆"
            )

    else:

        st.error(
            random.choice(wrong_messages)
        )

        st.write(
            f"Correct answer: **{correct_answer}**"
        )

    st.session_state.show_next = True

# ---------------- NEXT WORD ----------------

if st.session_state.show_next:

    if st.button("Next Word ➡️"):

        if len(
            st.session_state.remaining_words
        ) == 0:

            st.balloons()
            st.success(
                "Congratulations! You completed all the words! 🎉"
            )

        else:

            st.session_state.word = random.choice(
                st.session_state.remaining_words
            )

            st.session_state.remaining_words.remove(
                st.session_state.word
            )

            st.session_state.show_next = False
            st.rerun()

# ---------------- RESTART ----------------

if st.button("🔄 Restart Quiz"):

    st.session_state.clear()
    st.rerun()