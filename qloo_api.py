import requests
import os


def get_qloo_recommendations(prompt):
    api_key = os.getenv("QLOO_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    # Replace with real Qloo endpoint and data
    url = "https://api.qloo.com/v1/recommendations"
    payload = {"text": prompt, "type": "music"}  # adjust accordingly
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
