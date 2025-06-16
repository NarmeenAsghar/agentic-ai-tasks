🤖 Chainlit Gemini Chatbot

Welcome to the Chainlit Gemini Chatbot project! This AI assistant is built using Chainlit and LiteLLM, and integrates Google's Gemini 2.0 Flash model to deliver fast, intelligent conversational responses.

📌 Overview

This chatbot creates a real-time interactive conversation experience using a lightweight and scalable architecture:

⚙️ Built on Python

💬 Interactive chat powered by Chainlit

🌐 Responses generated through Gemini 2.0 Flash using LiteLLM

🗂️ Saves chat history for reference

🔐 Uses .env for secure API management

🛠️ Installation Guide

1. Clone the Repository

git clone https://github.com/yourusername/chainlit-gemini-chatbot.git
cd chainlit-gemini-chatbot

2. Set Up Python Environment

Install the required packages:

pip install -r requirements.txt

Or install manually:

pip install chainlit litellm python-dotenv

3. Create the .env File

In the root directory, create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

You can get the Gemini API key from Google’s developer portal if you don’t already have one.

4. Run the Chatbot

chainlit run chainlit_gemini_chatbot.py

Then open the provided local URL (usually http://localhost:8000) to start chatting with your assistant!

🧠 How It Works

Chat Flow

When the user connects, a welcome message is shown.

Each new message is appended to the session history.

The message history is sent to Gemini 2.0 Flash via LiteLLM.

The assistant’s reply is displayed and logged.

When the chat ends, all messages are stored in conversation_log.json.

Core Technologies

Component

Role

Chainlit

Real-time UI for LLM interaction

LiteLLM

Simple wrapper to access Gemini and other LLM APIs

Python dotenv

For secure handling of API keys

JSON

Storing chat logs
