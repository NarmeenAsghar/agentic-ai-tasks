import os
import json
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise RuntimeError("Missing GEMINI_API_KEY. Please add it to your .env file.")

@cl.on_chat_start
async def handle_start():
    cl.user_session.set("history", [])
    await cl.Message(content="👋 Hey there! I'm your AI assistant. What can I help you with today?").send()

@cl.on_message
async def handle_message(msg: cl.Message):
    prompt = msg.content
    conversation = cl.user_session.get("history") or []
    conversation.append({"role": "user", "content": prompt})

    loading = cl.Message(content="Let me think...")
    await loading.send()

    try:
        reply = completion(
            model="gemini/gemini-2.0-flash",
            api_key=gemini_key,
            messages=conversation
        )

        bot_message = reply.choices[0].message.content
        loading.content = bot_message
        await loading.update()

        conversation.append({"role": "assistant", "content": bot_message})
        cl.user_session.set("history", conversation)

        # Optional logging
        print(f"User: {prompt}\nBot: {bot_message}\n")

    except Exception as error:
        loading.content = f"⚠️ Something went wrong: {error}"
        await loading.update()
        print(f"Error occurred: {error}")

@cl.on_chat_end
async def handle_end():
    chat = cl.user_session.get("history") or []
    with open("conversation_log.json", "w") as file:
        json.dump(chat, file, indent=2)
    print("Chat log stored successfully.")
