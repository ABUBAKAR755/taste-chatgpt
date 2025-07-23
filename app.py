import streamlit as st
from utils import get_gemini_response

st.set_page_config(page_title="TasteGPT", page_icon="🎯")
st.title("🎯 TasteGPT - AI Lifestyle Curator")

st.write("Tell me about your interests (music, food, movies, books, etc.), and I’ll recommend things that match your vibe!")

# Example prompt shown to user
user_input = st.text_input(
    "Example: I like 90s rock music, fantasy novels, and Italian food.")

if st.button("Get AI Recommendations") and user_input:
    with st.spinner("Generating cultural recommendations using Gemini..."):
        try:
            response = get_gemini_response(user_input)
            st.subheader("🎨 TasteGPT Recommends:")
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
