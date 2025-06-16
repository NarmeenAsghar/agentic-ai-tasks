import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel # type: ignore
from agents.run import RunConfig # type: ignore


load_dotenv()


gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise EnvironmentError("GEMINI_API_KEY not found in .env file!")

client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


chat_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)


settings = RunConfig(
    model=chat_model,
    model_provider=client,
    tracing_disabled=True
)


async def main():
    my_agent = Agent(
        name="CodeHelper",
        instructions="You are a helpful assistant that can help with coding tasks.",
        model=chat_model
    )

    prompt = "Explain recursion in programming with a simple example."
    response = await Runner.run(my_agent, prompt, run_config=settings)
    
    print("Response:\n", response.final_output)


if __name__ == "__main__":
    asyncio.run(main())

