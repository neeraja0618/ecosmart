import streamlit as st
from groq import Groq

import os
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.set_page_config(page_title="My Eco Report", page_icon="📄", layout="wide")

st.title("📄 My Eco Report")
st.write("Download your complete sustainability report")

st.divider()

if "name" not in st.session_state:
    st.warning("Please go to Home page first and enter your details!")
else:
    st.subheader(f"Report for {st.session_state.name}")

    if st.button("Generate My Full Report 📄"):
        with st.spinner("Generating your report..."):

            carbon = st.session_state.get("carbon_result", "Not calculated yet")
            tips = st.session_state.get("eco_tips", "Not generated yet")

            prompt = f"""
            Create a complete eco report for this person:
            
            Name: {st.session_state.name}
            Age: {st.session_state.age}
            City: {st.session_state.city}
            Lifestyle: {st.session_state.lifestyle}
            
            Carbon Footprint Analysis:
            {carbon}
            
            Eco Tips Given:
            {tips}
            
            Please create a formal report with:
            1. Executive Summary
            2. Current Carbon Footprint Status
            3. Top 3 Areas To Improve
            4. 30 Day Eco Challenge Plan
            5. Motivational closing message
            
            Make it formal but friendly.
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )

            report = response.choices[0].message.content
            st.session_state.final_report = report

            st.success("Report Generated! 📄")
            st.write(report)

    if "final_report" in st.session_state:
        st.divider()
        st.download_button(
            label="⬇️ Download Report as Text File",
            data=st.session_state.final_report,
            file_name=f"{st.session_state.name}_eco_report.txt",
            mime="text/plain"
        )