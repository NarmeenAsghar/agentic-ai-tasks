

````markdown
# 🧠 Full Agentic Project Suite

This repository contains a suite of experimental and educational Python-based agentic projects. Each project explores a specific concept or tool in AI agent development, such as swarm logic, package management with `uv`, OpenRouter-based LLM integration using LiteLLM, and building interactive chat agents using Chainlit.

---

## 📁 Project Structure

```bash
full_agentic_project/
│
├── 01_swarm/               # Simulated swarm behavior logic
├── 02_uv/                  # Python project setup using uv
├── 03_openrouter_litellm/  # LLM queries using OpenRouter + LiteLLM
├── 04_hello_agent/         # Chatbot agent using Chainlit and DeepSeek
└── README.md               # Main documentation
````

---

## 🔧 01\_swarm — Simulated Swarm Logic

This simple project demonstrates basic coordinated agent behavior.

### ✅ Features:

* Dummy agent logic simulating swarm movement.
* Good starting point for multi-agent system simulations.

### 🚀 Run

```bash
python main.py
```

---

## ⚡ 02\_uv — Exploring `uv`

`uv` is a super-fast Python package manager and virtual environment tool.

### ✅ Features:

* Alternative to `pip`, `venv`, and `pip-tools`.
* Extremely fast project setup and dependency installation.

### 🛠 Usage

```bash
uv init --package exploring-uv
cd exploring-uv
uv run exploring-uv
```

To run your own script (e.g., `main.py`):

```bash
python main.py
```

---

## 🌐 03\_openrouter\_litellm — LLM Access via OpenRouter + LiteLLM

This project integrates OpenRouter (multi-model API) using the `litellm` package to query different LLM providers like DeepSeek, GPT-3.5, Gemini, etc.

### ✅ Features:

* Query any OpenRouter-supported model.
* Easily configurable via `.env`.

### 🛠 Setup

1. Create a `.env` file:

   ```
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run:

   ```bash
   python main.py
   ```

---

## 💬 04\_hello\_agent — Chatbot using Chainlit + DeepSeek

This project uses `Chainlit` to build a web-based chatbot interface with OpenRouter LLMs.

### ✅ Features:

* Runs a real-time chat UI.
* Uses DeepSeek (or any LLM via OpenRouter).
* Tracks session history.

### 🛠 Setup

1. Add your `.env`:

   ```
   OPENROUTER_API_KEY=your_key_here
   ```

2. Install:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the chatbot:

   ```bash
   chainlit run main.py -w
   ```

---

## 📦 Installation (Generic For All Projects)

1. **Clone the repo**

   ```bash
   git clone <repo-url>
   cd full_agentic_project
   ```

2. **Setup virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # or source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔐 API Keys

Some projects require API keys. Create a `.env` file in the root of the relevant project folder with:

```env
OPENROUTER_API_KEY=your_key_here
```

For Gemini or other providers via OpenRouter, make sure they are allowed in your model settings.

---

## 📚 Requirements

* Python 3.10+
* [Chainlit](https://docs.chainlit.io/)
* [LiteLLM](https://github.com/BerriAI/litellm)
* [uv](https://github.com/astral-sh/uv)
* [OpenRouter](https://openrouter.ai/)
* DeepSeek, Gemini, or any other OpenRouter-compatible model

---

## ✅ Start Exploring

```bash
cd 01_swarm
python main.py
```

or

```bash
cd 04_hello_agent
chainlit run main.py -w
```
