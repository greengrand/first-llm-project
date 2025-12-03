# examples/call_openai.py
from dotenv import load_dotenv
import os
import requests
import sys

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("OPENAI_API_KEY not set. Please fill .env or set env variable.", file=sys.stderr)
    sys.exit(1)

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
payload = {
    "model": "gpt-4o-mini",   # при необходимости поменяй на модель, доступную в твоём аккаунте
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Напиши короткое приветствие на русском (1-2 предложения)."}
    ],
    "max_tokens": 120,
    "temperature": 0.2
}

try:
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    data = r.json()
    # безопасно выберем текст
    text = None
    if "choices" in data and data["choices"]:
        text = data["choices"][0].get("message", {}).get("content") or data["choices"][0].get("text")
    print("Model response:\n", text)
except requests.HTTPError as e:
    print("HTTP error:", e, r.text if 'r' in locals() else "", file=sys.stderr)
except Exception as e:
    print("Error:", e, file=sys.stderr)
