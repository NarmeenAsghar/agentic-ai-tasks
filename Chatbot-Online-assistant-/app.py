import chainlit as cl
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import logging
import json

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

# Career knowledge base
career_kb = {
    "career paths": "Popular career paths include Software Development, Data Science, Digital Marketing, Product Management, UX/UI Design, and Cybersecurity.",
    "interview tips": "Research the company, practice common questions, prepare your own questions, dress appropriately, and follow up with a thank-you note.",
    "skill building": "Consider learning Python, data analysis, cloud computing, communication skills, or project management to improve your chances.",
    "resume advice": "Keep your resume concise, highlight achievements with metrics, tailor it for each job, and avoid generic phrases.",
    "motivation": "Remember, every expert was once a beginner. Keep learning and stay positive!",
    "common interview questions": "Tell me about yourself, What are your strengths and weaknesses?, Why do you want to work here?, Describe a challenge you faced and how you overcame it."
}

def search_career_kb(query: str) -> str:
    logger.info(f"Searching career KB for: '{query}'")
    query_lower = query.lower()
    matched_answers = []

    for key, val in career_kb.items():
        if key in query_lower or any(word in query_lower for word in key.split()):
            matched_answers.append(val)
    
    if matched_answers:
        return "\n\n".join(matched_answers) + "\n\nWould you like to know more or ask something else?"
    else:
        return ("Sorry, I don't have information on that right now. "
                "But feel free to ask me anything about careers or interviews!")

search_tool_schema = {
    "type": "function",
    "function": {
        "name": "search_career_kb",
        "description": "Find career advice, interview tips, resume help, or motivation.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "User's question or topic about careers, interviews, or skill-building."
                }
            },
            "required": ["query"]
        }
    }
}

class CareerCoachAgent:
    def __init__(self, model: str, tools: list):
        self.model = model
        self._tools = {"search_career_kb": search_career_kb}
        self.tools_config = tools

    async def generate_response(self, messages: list[dict]) -> str:
        try:
            response = await client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools_config,
                tool_choice="auto",
                temperature=0.7,
                max_tokens=400
            )
            msg = response.choices[0].message
            content = msg.content

            # Handle tool calls if any
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                tool_call = msg.tool_calls[0]
                tool_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                if tool_name in self._tools:
                    tool_output = self._tools[tool_name](**args)
                    messages.append(msg)
                    messages.append({
                        "role": "tool",
                        "name": tool_name,
                        "content": tool_output
                    })
                    follow_up = await client.chat.completions.create(
                        model=self.model,
                        messages=messages,
                        tools=self.tools_config,
                        tool_choice="auto",
                        temperature=0.7,
                        max_tokens=300
                    )
                    return follow_up.choices[0].message.content
            
            return content if content else "Can you please ask that differently?"
        
        except Exception as e:
            logger.error(f"Error in generate_response: {e}", exc_info=True)
            return "Oops! Something went wrong. Please try again later."

agent = CareerCoachAgent(
    model=MODEL,
    tools=[search_tool_schema]
)

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("messages", [
        {
            "role": "system",
            "content": (
                "You are a friendly, professional career coach chatbot. "
                "Help users with career advice, interview preparation, resume tips, and motivation."
            )
        },
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm your Personal Career Coach. How can I help you with your career today?"
        }
    ])
    await cl.Message(content="""
**Welcome to your Career Coach!** 🎯

Ask me about:
- Career paths and options
- Interview tips & common questions
- Resume and skill-building advice
- Motivational support

How can I assist you today?
""").send()

@cl.on_message
async def main(message: cl.Message):
    messages = cl.user_session.get("messages")
    messages.append({"role": "user", "content": message.content})

    try:
        response = await agent.generate_response(messages)
        messages.append({"role": "assistant", "content": response})
        await cl.Message(content=response).send()

    except Exception as e:
        logger.error(f"Error handling message: {e}", exc_info=True)
        await cl.Message(content="Sorry, something went wrong. Please try again.").send()
