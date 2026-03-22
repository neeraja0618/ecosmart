import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="30 Day Challenge", page_icon="📅", layout="wide")

st.title("📅 30 Day Eco Challenge Tracker")
st.write("Track your daily eco friendly actions and build sustainable habits!")

st.divider()

# Initialize tracker in session state
if "completed_days" not in st.session_state:
    st.session_state.completed_days = []

if "challenges" not in st.session_state:
    st.session_state.challenges = [
        "Use public transport or walk today",
        "Eat one vegetarian meal",
        "Turn off lights when leaving room",
        "Use a reusable water bottle",
        "Avoid plastic bags while shopping",
        "Take a shorter shower",
        "Unplug devices when not in use",
        "Buy nothing new today",
        "Compost food waste",
        "Plant something or water a plant",
        "Use stairs instead of elevator",
        "Cook at home instead of ordering",
        "Recycle at least one item",
        "Read about climate change for 10 mins",
        "Share one eco tip with a friend",
        "Avoid using AC for one hour",
        "Use natural light instead of bulbs",
        "Carry your own bag to shop",
        "Reduce screen time by 1 hour",
        "Eat local seasonal food today",
        "Fix something instead of throwing it",
        "Use cold water for laundry",
        "Walk for at least 30 minutes",
        "Avoid single use plastics all day",
        "Turn off tap while brushing teeth",
        "Use both sides of paper",
        "Donate unused items instead of trashing",
        "Cook extra to avoid food waste",
        "Switch to LED bulb in one room",
        "Celebrate — you completed 30 days! 🎉"
    ]

# Show progress
completed = len(st.session_state.completed_days)
st.progress(completed / 30)
st.write(f"**{completed}/30 days completed!**")

st.divider()

# Show challenges
st.subheader("Your Daily Challenges")

for i, challenge in enumerate(st.session_state.challenges):
    day = i + 1
    col1, col2 = st.columns([4, 1])
    with col1:
        if day in st.session_state.completed_days:
            st.success(f"Day {day} ✅ — {challenge}")
        else:
            st.write(f"Day {day} — {challenge}")
    with col2:
        if day not in st.session_state.completed_days:
            if st.button(f"Done!", key=f"day_{day}"):
                st.session_state.completed_days.append(day)
                st.rerun()

st.divider()

# AI Motivation
if st.button("Get AI Motivation 💪"):
    with st.spinner("Getting your motivation..."):
        prompt = f"""
        This person has completed {completed} out of 30 eco challenges.
        Give them a short, energetic and motivational message in 3-4 lines.
        Make it specific to their progress and very encouraging.
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success(response.choices[0].message.content)