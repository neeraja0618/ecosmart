import streamlit as st
from groq import Groq

import os
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.set_page_config(page_title="Carbon Footprint", page_icon="♻️", layout="wide")

st.title("♻️ Carbon Footprint Checker")
st.write("Find out how much carbon you're producing daily")

st.divider()

# Transport
st.subheader("🚗 Transport")
transport = st.selectbox("Primary mode of transport", 
    ["Walking/Cycling", "Public Bus/Metro", "Two Wheeler", "Car", "Cab/Auto daily"])
travel_km = st.slider("How many KMs do you travel daily?", 0, 100, 10)

# Food
st.subheader("🍽️ Food Habits")
diet = st.selectbox("Your diet type", 
    ["Vegan", "Vegetarian", "Occasionally Non-Veg", "Daily Non-Veg"])

# Energy
st.subheader("⚡ Home Energy")
ac_usage = st.selectbox("AC Usage", 
    ["No AC", "AC occasionally", "AC daily few hours", "AC all day"])
appliances = st.multiselect("Appliances you use daily", 
    ["Washing Machine", "Dishwasher", "Electric Geyser", "Microwave", "TV"])

# Shopping
st.subheader("🛍️ Shopping Habits")
shopping = st.selectbox("How often do you shop for new clothes/products?", 
    ["Rarely", "Once a month", "Weekly", "Very frequently"])

if st.button("Calculate My Carbon Footprint 🌍"):
    with st.spinner("Calculating your carbon footprint..."):
        
        # Save to session state
        st.session_state.transport = transport
        st.session_state.diet = diet
        st.session_state.ac_usage = ac_usage
        
        prompt = f"""
        Calculate the carbon footprint for this person and give a detailed analysis:
        
        Transport: {transport}, travelling {travel_km} km daily
        Diet: {diet}
        AC Usage: {ac_usage}
        Daily Appliances: {appliances}
        Shopping habits: {shopping}
        
        Please provide:
        1. Estimated daily CO2 in kg (be specific with numbers)
        2. Monthly CO2 estimate
        3. How this compares to average Indian person
        4. Which of their habits contributes most to carbon footprint
        5. Overall carbon footprint rating: Low/Medium/High/Very High
        
        Keep it clear, friendly and use simple language.
        """
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        
        answer = response.choices[0].message.content
        
        # Save result to session state
        st.session_state.carbon_result = answer
        
        st.success("Carbon Footprint Analysis Complete! 🌍")
        st.write(answer)
