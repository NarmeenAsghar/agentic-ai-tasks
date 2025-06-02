# modules required: chainlit, openai, python-dotenv
# This code is a simple Chainlit application that interacts with the OpenRouter API using the DeepSeek Chat model.
import chainlit as cl
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

# it assumed .env file is present in the same directory with OPEN_ROUTER_API_KEY set
load_dotenv()

# Initialize the OpenAI client with the OpenRouter API key and base URL
client = AsyncOpenAI(
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

model = "deepseek/deepseek-chat"

# Define the Chainlit application
# chainlit is a framework for building interactive applications with Python
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! How can I help you today?").send()

# Handle incoming messages from the user
@cl.on_message
async def on_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    response = await client.chat.completions.create(
        model=model,
        messages=history
    )

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    cl.user_session.set("history", history)

    await cl.Message(content=reply).send()
