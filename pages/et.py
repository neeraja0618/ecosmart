import streamlit as st
from groq import Groq

import os
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.set_page_config(page_title="Eco Tips", page_icon="🌱", layout="wide")

st.title("🌱 Personalized Eco Tips")
st.write("Get AI powered sustainability tips based on your lifestyle")

st.divider()

if "name" not in st.session_state:
    st.warning("Please go to Home page first and enter your details!")
else:
    st.subheader(f"Hello {st.session_state.name}! Here are your personalized eco tips")
    
    focus_area = st.multiselect("What areas do you want to improve?",
        ["Transport & Travel", "Food & Diet", "Energy at Home", 
         "Shopping & Waste", "Water Usage", "Digital Carbon Footprint"])
    
    difficulty = st.selectbox("How easy should the tips be?",
        ["Very Easy — Small changes", 
         "Medium — Some effort needed",
         "Challenging — I am serious about this"])
    
    if st.button("Get My Eco Tips 🌱"):
        with st.spinner("Generating your personalized tips..."):
            prompt = f"""
            Generate personalized sustainability tips for this person:
            
            Name: {st.session_state.name}
            Age Group: {st.session_state.age}
            City: {st.session_state.city}
            Lifestyle: {st.session_state.lifestyle}
            Focus Areas: {focus_area}
            Difficulty Level: {difficulty}
            
            Please provide:
            1. 5 specific actionable eco tips for their lifestyle
            2. For each tip mention: what to do, why it helps, how much CO2 it saves
            3. One challenge they can start TODAY
            4. Motivational closing message
            
            Keep it friendly, specific to Indian lifestyle and very practical.
            """
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            
            answer = response.choices[0].message.content
            st.session_state.eco_tips = answer
            
            st.success("Your Eco Tips Are Ready! 🌱")
            st.write(answer)