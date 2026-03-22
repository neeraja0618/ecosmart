import streamlit as st

st.set_page_config(
    page_title="EcoSmart",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 EcoSmart — Your Personal AI Sustainability Assistant")
st.write("Welcome! EcoSmart helps you understand your carbon footprint and live more sustainably.")

st.divider()

st.subheader("Tell us about yourself")

name = st.text_input("Your Name")
age = st.selectbox("Age Group", ["Teen (13-17)", "Student (18-25)", "Working Professional (25-45)", "Family (45+)"])
city = st.text_input("Your City")
lifestyle = st.selectbox("Your Lifestyle", ["Student in PG/Hostel", "Working Professional", "Family with Kids", "Other"])

if st.button("Get Started 🌱"):
    if name == "" or city == "":
        st.error("Please fill in all details!")
    else:
        st.session_state.name = name
        st.session_state.age = age
        st.session_state.city = city
        st.session_state.lifestyle = lifestyle
        st.success(f"Welcome {name}! Use the sidebar to explore EcoSmart 🌍")