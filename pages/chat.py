import streamlit as st
from groq import Groq

import os
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.set_page_config(page_title="Eco Chat", page_icon="💬", layout="wide")

st.title("💬 Ask EcoSmart Anything")
st.write("Chat with your personal AI sustainability assistant")

st.divider()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show old messages
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# New message input
question = st.chat_input("Ask anything about sustainability...")

if question:
    st.session_state.chat_history.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are EcoSmart, a friendly AI sustainability assistant. Answer all questions related to environment, sustainability, carbon footprint and eco friendly living. Keep answers practical and relevant to Indian lifestyle."},
                *st.session_state.chat_history
            ]
        )
        answer = response.choices[0].message.content

    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)