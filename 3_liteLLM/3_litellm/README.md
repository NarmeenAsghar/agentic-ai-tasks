# 🤖 Multi-Model AI Prompt Script using LiteLLM

This Python script demonstrates how to interact with multiple large language models (LLMs) — including **OpenAI GPT-4o** and **Anthropic Claude 3** models — using the [LiteLLM](https://github.com/BerriAI/litellm) library.

---

## 📦 Features

- ✅ Easily switch between different AI models (OpenAI & Claude)
- 📤 Sends a simple prompt and receives model-specific responses
- 🧪 Great for testing response differences between models
- 🔐 Uses environment variables for secure API key handling

---

## 🛠️ Requirements

- Python 3.7 or higher
- `litellm` Python package
- Valid API keys for:
  - OpenAI (for GPT-4o)
  - Anthropic (for Claude 3 models)

---

## 📥 Installation

First, clone this repository or copy the script to your local machine.

Then install the required package:

```bash
pip install litellm




🔑 API Key Setup
Before running the script, you need to set your API keys. You can either:

Method 1: Set API keys directly in the script
python
Copy
Edit
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-api-key"
Method 2: Use environment variables in your terminal
Linux / macOS:

bash
Copy
Edit
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
Windows (CMD):

cmd
Copy
Edit
set OPENAI_API_KEY=your-openai-api-key
set ANTHROPIC_API_KEY=your-anthropic-api-key
🚀 How to Use
python
Copy
Edit
from script import use_openai, use_claude, use_claude_opus

use_openai()         # Sends message to OpenAI GPT-4o
use_claude()         # Sends message to Claude 3 Sonnet
use_claude_opus()    # Sends message to Claude 3 Opus
Each function sends a simple message: "Hello, what have you been upto?" to the respective model and prints the response.

