import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyDh48o5_G8Xpis1qCbQmRLH-8r4ooIlkGE"))

# Use Gemini Pro text-only model


def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini API Error: {e}"
