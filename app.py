import streamlit as st
import random
from german_words_with_examples_filled import german_words

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
    "Germany is one step closer 🚀",
    "Bhai, Goethe examiner smiled 😊",
    "The visa officer approves this answer ✅",
    "Duolingo owl is proud of you 🦉",
    "B2 Warrior unlocked ⚔️",
    "This word fears you now 😎",
    "You cooked! 🔥",
    "German proficiency +1 📈",
    "Fluent German arc has begun 🇩🇪"
]

wrong_messages = [
    "Kyu nahi ho rahe padhaye 😭",
    "Germany jaake kya bologe bhai? 😂",
    "Bhai, Goethe examiner is watching you 👀",
    "Duolingo owl has booked your flight back to India ✈️",
    "Aaj vocabulary ki vaat lag gayi 😭",
    "Bro, B2 certificate won't print itself 😭",
    "The word just filed a complaint against you 📄",
    "Your German teacher fainted after seeing this answer 💀",
    "Even Google Translate is disappointed 😔",
    "At this rate you'll order Schnitzel in English 😭",
    "The visa officer just raised an eyebrow 🤨",
    "Padh le bhai, time nahi hai!!",
    "This word will come in the exam now because you got it wrong 😈",
    "The word is laughing at you right now 😂"
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

word_info = german_words[word]

correct_answer = word_info['meanings']
example_de = word_info['example_de']
example_en = word_info['example_en']

st.header(word)

if st.button("📖 Show Example Sentence"):
    if example_de:
        st.info(example_de)
        st.info(example_en)
    else:
        st.warning(
            "No example sentence available yet."
        )
        
with st.form("quiz_form"):
    answer = st.text_input(
        "Enter the English meaning:"
    )
    submitted = st.form_submit_button(
        "Check"
    )

if submitted:

    user_answer = answer.strip().lower()

    accepted_answers = [
        meaning.lower()
        for meaning in correct_answer
    ]

    if user_answer in accepted_answers:

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
            "Accepted answers: "
            + ", ".join(correct_answer)
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
