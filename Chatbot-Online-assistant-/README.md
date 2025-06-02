
```markdown
# 💼 Career Coach Chatbot (Chainlit + LiteLLM + OpenRouter)

A professional career guidance chatbot built with **Chainlit**, **LiteLLM**, and **OpenRouter**. It offers advice on career paths, interview tips, resume building, skill development, and motivational support.

---

## 🚀 Features

- Ask questions about:
  - Career paths
  - Interview preparation
  - Resume tips
  - Motivation and personal development
- Uses:
  - `Chainlit` for UI and interaction
  - `LiteLLM` for LLM integration
  - `OpenRouter` for connecting to LLM providers (e.g., Gemini)
- Async tool calls for knowledge base search
- Fully customizable

---

## 📁 Project Structure

```

career-coach-chatbot/
│
├── app.py                # Main Chainlit app file
├── .env                  # Contains API keys (not committed)
├── requirements.txt      # List of dependencies
└── README.md             # You're here!

````

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/career-coach-chatbot.git
cd career-coach-chatbot
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` not present, manually install:

```bash
pip install chainlit litellm openai python-dotenv
```

### 4. Set up `.env` file

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---

## ✅ Run the Chatbot

```bash
chainlit run app.py
```

Open your browser at: [http://localhost:8000](http://localhost:8000)

---

## 📌 Notes

* This project requires an OpenRouter account and API key.
* Ensure you are using a compatible version of `openai` with `litellm`.

