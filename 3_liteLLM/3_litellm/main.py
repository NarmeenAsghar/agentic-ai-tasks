import os
from litellm import completion
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not OPENAI_API_KEY or not ANTHROPIC_API_KEY:
    print("Please set your API keys in the .env file")
    exit(1)

def use_openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[
            {
                "role": "user",
                "content": "Hello, what about you?"
            }
        ]
    )
    print(response)

def use_claude():
    response = completion(
        model="claude/claude-3-sonnet",
        messages=[
            {
                "role": "user",
                "content": "Hello, what about you?"
            }
        ]
    )
    print(response)


def use_claude_opus():
    response = completion(
        model="claude/claude-3-opus",
        messages=[
            {
                "role": "user",
                "content": "Hello, what about you?"
            }
        ]
    )
    print(response)



