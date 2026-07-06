import streamlit as st
import random
from german_words_with_examples_filled import german_words

st.set_page_config(page_title="German Vocabulary Quiz", page_icon="🇩🇪")
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
    "Bro actually got one right 😭",
    "Germany is one step closer 🚀",
    "B2 Warrior unlocked ⚔️",
    "You cooked 🔥",
    "Main character energy detected ✨"
]

good_gifs = [
    "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
    "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    "https://media.giphy.com/media/ely3apij36BJhoZ234/giphy.gif",
    "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
    "https://media.giphy.com/media/3oz8xAFtqoOUUrsh7W/giphy.gif",
    "https://media.giphy.com/media/1BdIPBW9J2R4Q/giphy.gif"
]

wrong_messages = [
    "Kyu nahi ho rahe padhaye 😭",
    "Germany jaake kya bologe bhai? 😂",
    "Skill issue 🗿",
    "Mission failed successfully 😭",
    "Bro got humbled by one German word 💀",
    "The vocabulary gods are disappointed today ⚡"
]

wrong_gifs = [
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/10JhviFuU2gWD6/giphy.gif",
    "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",
    "https://media.giphy.com/media/11mwI67GLeMvgA/giphy.gif",
    "https://media.giphy.com/media/26n6WywJyh39n1pBu/giphy.gif",
    "https://media.giphy.com/media/14uQ3cOFteDaU/giphy.gif",
    "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif"
]

boss_messages = [
    "💀 Goethe Examiner Boss Fight Started!",
    "💀 Visa Officer Appeared!",
    "💀 Duolingo Owl Final Form Unlocked!"
]

legendary_rewards = [
    "🏆 +100 Aura",
    "🇩🇪 Visa Officer Approval +1",
    "⚔️ German Warrior Badge",
    "📚 Infinite Vocabulary Buff",
    "👑 Main Character Energy",
    "🦉 Duolingo Owl Friendship",
    "🍺 Free Imaginary German Beer",
    "🎓 Goethe Examiner Respect +10",
    "🚀 German Level Increased",
    "💰 Scholarship Luck +5"
]

# ---------------- PROGRESS ----------------

total_words = len(german_words)
progress = st.session_state.score / total_words
st.progress(progress)
st.write(f"Score: {st.session_state.score} / {total_words}")

# ---------------- QUIZ ----------------

word = st.session_state.word
word_info = german_words[word]

correct_answer = word_info["meanings"]
example_de = word_info["example_de"]
example_en = word_info["example_en"]

st.header(word)

if st.button("📖 Show Example Sentence"):
    if example_de:
        st.info(example_de)
        #st.info(example_en)
    else:
        st.warning("No example sentence available yet.")

with st.form("quiz_form"):
    answer = st.text_input("Enter the English meaning:")
    submitted = st.form_submit_button("Check")

if submitted:

    user_answer = answer.strip().lower()

    accepted_answers = [
        meaning.strip().lower()
        for meaning in correct_answer
    ]

if user_answer in accepted_answers:

    st.success(
        random.choice(correct_messages)
    )

    st.session_state.score += 1
    
    # SUPER RARE EVENT
    if random.randint(1, 50) == 1:
    
        st.image(
            random.choice(good_gifs),
            width=350
        )
    
        st.success(
            f"LEGENDARY DROP: {random.choice(legendary_rewards)}"
        )
    
    if st.session_state.score in [10, 50, 100]:
            pass

else:

        chance = random.randint(1, 100)

        if chance <= 70:
            st.error(random.choice(wrong_messages))
            st.write(
                "Accepted answers: "
                + ", ".join(correct_answer)
            )

        elif chance <= 90:
            text_col, gif_col = st.columns([3, 2])

            with text_col:
                st.error(random.choice(wrong_messages))
                st.write(
                    "Accepted answers: "
                    + ", ".join(correct_answer)
                )

            with gif_col:
                st.image(
                    random.choice(wrong_gifs),
                    width=250
                )

        elif chance <= 95:
            st.snow()
            st.error(random.choice(wrong_messages))

        elif chance <= 99:
            st.balloons()
            st.error(random.choice(wrong_messages))

        else:
            st.error(random.choice(boss_messages))
            st.warning(
                "The Duolingo owl has arrived at your location 💀"
            )

    st.session_state.show_next = True

# ---------------- NEXT WORD ----------------

if st.session_state.show_next:

    if st.button("Next Word ➡️"):

        if len(st.session_state.remaining_words) == 0:
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
