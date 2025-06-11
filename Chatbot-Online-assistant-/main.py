# imports necessary libraries
import chainlit as cl
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"

if not API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Configure OpenAI
client = AsyncOpenAI(api_key=API_KEY)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="""
**Welcome to the Chat Assistant!** 👋

I'm here to help you with any questions you have. Feel free to ask anything!
""").send()

@cl.on_message
async def main(message: cl.Message):
    try:
        # Log the API key status (without showing the actual key)
        logger.info(f"API Key present: {'Yes' if API_KEY else 'No'}")
        
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.content}
            ],
            temperature=0.7,
            max_tokens=400
        )
        
        reply = response.choices[0].message.content
        await cl.Message(content=reply).send()
        
    except Exception as e:
        error_message = f"Error details: {str(e)}"
        logger.error(error_message, exc_info=True)
        await cl.Message(content=f"An error occurred: {error_message}").send()
