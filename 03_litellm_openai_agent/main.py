# import necessary libraries
import os
from litellm import completion, exceptions

# Set up the environment variable for the Gemini (Vertex AI) API key
os.environ["VERTEXAI_API_KEY"] = "AIzaSyBfbSChGq3k1bP3edGHg_xnwVC607iztTU"

# Example usage of LiteLLM with Gemini (Vertex AI) API
messages = [{"role": "user", "content": "Hello, Gemini! How are you?"}]

# exceptions are used to handle errors gracefully
try:
    response = completion(model="gemini/gemini-1.5-flash", messages=messages)
    print("Gemini Response:", response['choices'][0]['message']['content'])
except exceptions.OpenAIError as e:
    print(f"LiteLLM Error: {e}")


print("=" * 80)

# # Interactive chat with Gemini using LiteLLM
import os
from litellm import completion, exceptions

# Set up the environment variable for the Gemini (Vertex AI) API key
os.environ["VERTEXAI_API_KEY"] = "AIzaSyBfbSChGq3k1bP3edGHg_xnwVC607iztTU"

print("💬 Gemini Chatbot started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Exiting chat. Goodbye!")
        break

    messages = [{"role": "user", "content": user_input}]

# exception handling for the chat completion  
    try:
        response = completion(model="gemini/gemini-1.5-flash", messages=messages)
        print("Gemini:", response['choices'][0]['message']['content'])
    except exceptions.OpenAIError as e:
        print(f"⚠️ LiteLLM Error: {e}")


