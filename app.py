import streamlit as st
import random
from rapidfuzz import fuzz
from german_words_with_examples_filled import german_words

if "score" not in st.session_state:
    st.session_state.score = 0
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "remaining_words" not in st.session_state:
    st.session_state.remaining_words = list(german_words.keys())
if "word" not in st.session_state:
    st.session_state.word = random.choice(st.session_state.remaining_words)
    st.session_state.remaining_words.remove(st.session_state.word)

correct_messages = [
    "Sehr gut! 🇩🇪",
    "Bro actually got one right 😭",
    "Germany is one step closer 🚀",
    "B2 Warrior unlocked ⚔️",
    "You cooked 🔥",
    "Main character energy detected ✨",
    "Sehr gut! 🇩🇪",
    "Bro actually got one right 😭",
    "Impossible. Did you use your brain today? 🧠",
    "The German embassy is impressed... for now 🇩🇪",
    "Plot twist: You knew this word 😱",
    "The Goethe examiner shed a tear of happiness 😭",
    "Ladies and gentlemen... he can be taught 🎓",
    "Bro remembered the word instead of guessing 💀",
    "The Duolingo owl has cancelled the hitman 🦉",
    "Germany is one step closer 🚀",
    "Even I didn't expect that one 😭",
    "B2 Warrior unlocked ⚔️",
    "That answer was suspiciously correct 🤨",
    "The word fears you now 😈",
    "Big brain moment 🧠✨",
    "Bro beat the allegations 😭",
    "You cooked 🔥",
    "One small step for German, one giant step for your visa 🇩🇪",
    "The visa officer nodded approvingly 📄",
    "Damn, okay Einstein 😎",
    "You dropped this 👑",
    "Character development arc is real 📈",
    "Bro might actually survive in Germany 😂",
    "A rare moment of intelligence has been detected 🚨",
    "This answer increased your IQ by 0.5 points 📈",
    "Duolingo owl is reluctantly proud of you 😤",
    "Achievement unlocked: Not Completely Lost 🏆",
    "You remembered a German word. Miracles do happen 😭",
    "Germany just moved 1 cm closer to you 🇩🇪",
    "Main character energy detected ✨"
]

wrong_messages = [
    "Kyu nahi ho rahe padhaye 😭",
    "Germany jaake kya bologe bhai? 😂",
    "Skill issue 🗿",
    "Mission failed successfully 😭",
    "Bro got humbled by one German word 💀",
    "The vocabulary gods are disappointed today ⚡",
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
    "The word is laughing at you right now 😂",
    "Bro got humbled by one German word 💀",
    "Nah, this is actually diabolical 😭",
    "The A2 certificate is slowly disappearing... 📜",
    "Bro is fighting for his life against vocabulary 💀",
    "Skill issue 🗿",
    "September is approaching faster than your German 😭",
    "The German embassy saw this and closed your file 😭",
    "Bhai, even ChatGPT can't defend this answer 😭",
    "One more mistake and Duolingo owl is outside your house 🦉",
    "The word said 'nice try' 😂",
    "German language: 1 | You: 0 😭",
    "This wasn't even close bro 💀",
    "Wake up babe, another wrong answer just dropped 😭",
    "Achievement unlocked: Confidently Incorrect 🏆",
    "The examiner wrote 'interesting attempt' on your paper 😭",
    "Bhai, this answer belongs in a museum 🏛️",
    "Mission failed successfully 😭",
    "Your keyboard typed faster than your brain today 😂",
    "That answer had more confidence than correctness 😭",
    "Plot twist: the word had a different meaning 😈",
    "The German word just hit you with a critical attack ⚔️",
    "Your German level has left the chat 🚪",
    "Bro, even the word is confused by your answer 😭",
    "This answer deserves a standing ovation... for comedy 😂",
    "Bhai, revise this one before it revises you 😭",
    "The vocabulary gods are disappointed today ⚡"
]

good_gifs = [
    "gifs/good/good1.gif",
    "gifs/good/good2.gif",
    "gifs/good/good3.gif",
    "gifs/good/good4.gif",
    "gifs/good/good5.gif",
    "gifs/good/good6.gif",
    "gifs/good/good7.gif",
    "gifs/good/good8.gif",
    "gifs/good/good9.gif",
    "gifs/good/good10.gif",
    "gifs/good/good11.gif"
]
bad_gifs = [
    "gifs/bad/bad1.gif",
    "gifs/bad/bad2.gif",
    "gifs/bad/bad3.gif",
    "gifs/bad/bad4.gif",
    "gifs/bad/bad5.gif",
    "gifs/bad/bad6.gif",
    "gifs/bad/bad7.gif",
    "gifs/bad/bad8.gif",
    "gifs/bad/bad9.gif",
    "gifs/bad/bad10.gif",
    "gifs/bad/bad11.gif",
    "gifs/bad/bad12.gif",
    "gifs/bad/bad13.gif"
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
    "👑 Main Character Energy"
]

total_words = len(german_words)
st.progress(st.session_state.score / total_words)
st.write(f"Score: {st.session_state.score} / {total_words}")

word = st.session_state.word
word_info = german_words[word]
correct_answer = word_info["meanings"]
example_de = word_info["example_de"]
example_en = word_info["example_en"]

st.header(word)

with st.form("quiz_form"):
    answer = st.text_input("Enter the English meaning:")
    submitted = st.form_submit_button("Check")

if submitted:

    user_answer = answer.strip().lower()
    accepted_answers = [
        m.strip().lower() 
        for m in correct_answer
    ]

    correct = False

    for ans in accepted_answers:

        if (
            user_answer == ans
            or user_answer.rstrip("s") == ans
            or ans.rstrip("s") == user_answer
            or fuzz.ratio(user_answer, ans) >= 80
        ):
            correct = True
            break


    if correct:
    
            st.success(random.choice(correct_messages))
            st.session_state.score += 1
            
            if good_gifs:
                gif = random.choice(good_gifs)
                st.write("GOOD:", gif)
                st.image(gif, width=350)
                
            st.success(
                f"LEGENDARY DROP: {random.choice(legendary_rewards)}"
            )
    else:
    
        st.error(random.choice(wrong_messages))
        st.write("Accepted answers: " + ", ".join(correct_answer))
                
        if bad_gifs:
             gif = random.choice(bad_gifs)
             st.write("BAD:", gif)
             st.image(gif, width=250)
    
    st.session_state.show_next = True

if st.session_state.show_next:
    if st.button("Next Word ➡️"):
        if not st.session_state.remaining_words:
            st.success("Congratulations! You completed all the words! 🎉")
        else:
            st.session_state.word = random.choice(st.session_state.remaining_words)
            st.session_state.remaining_words.remove(st.session_state.word)
            st.session_state.show_next = False
            st.rerun()

if st.button("🔄 Restart Quiz"):
    st.session_state.clear()
    st.rerun()
