import os
import requests
from dotenv import load_dotenv

# Load .env file in same directory
load_dotenv(dotenv_path=".env")

# Load API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print(f"🔑 API Key Loaded: {OPENROUTER_API_KEY}")  # Debug print

if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY is missing!")

# Prepare request
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://openrouter.ai",  # Try this for referer
    "X-Title": "Test App"
}
payload = {
    "model": "openai/gpt-4o",
    "messages": [
        {"role": "user", "content": "What is Python?"}
    ],
    "max_tokens": 100
}

# Send request
response = requests.post(url, headers=headers, json=payload)

print("\n" + "="*60)
print(f"Status code: {response.status_code}")
print("="*60 + "\n")

try:
    answer = response.json()['choices'][0]['message']['content']
    print("✅ Response:\n")
    print(answer)
except Exception:
    print("⚠️ Unexpected response format:")
    print(response.text)
