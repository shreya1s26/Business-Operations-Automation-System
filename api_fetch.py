import requests
from config import API_URL, API_KEY

def fetch_api_data():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()
    return response.json()
