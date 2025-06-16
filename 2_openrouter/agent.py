import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"  # ✅ Some versions expect `/api/v1`, not `/v1`
MODEL = "gpt-4o"

# ✅ Use full config with headers
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL,
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "MyAIApp"
    }
)

set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in detail.",
        model=OpenAIChatCompletionsModel(
            model=MODEL,
            openai_client=client
        ),
    )

    result = await Runner.run(
        agent,
        "What is OpenRouter?",
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
