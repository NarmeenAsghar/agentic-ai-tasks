# imports necessary libraries
import chainlit as cl
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Initialize Chainlit app
@cl.on_message
async def main(message: cl.Message):
    user_prompt = message.content
# Sets up the headers for the OpenRouter API request, including the authorization token
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
# Constructs the request body for the OpenRouter API
    body = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }
# Sends a POST request to the OpenRouter API with the user's message
    response = requests.post(OPENROUTER_URL, headers=headers, json=body)
# Checks the response status and extracts the reply from the API response
    if response.status_code == 200:
        data = response.json()
        reply = data['choices'][0]['message']['content']
    else:
        reply = f"API Error: {response.status_code}"
# Sends the reply back to the user in the Chainlit interface
    await cl.Message(content=reply).send()