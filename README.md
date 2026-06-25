# 🤖 LangChain Agent Template

A clean, customizable AI Agent template built with **LangChain**, **Groq**, and **Streamlit**.
Designed to be a solid starting point — add your own tools, system prompt, and data sources.

---

## ✨ Features

- 🧠 **Conversational AI Agent** powered by LangChain + Groq API
- 🔍 **Web Search** via SerpAPI
- 🕐 **Current Date/Time** tool built-in
- 💾 **Sliding-Window Memory** with auto-summarization for long conversations
- 🖥️ **Streamlit UI** — clean chat interface, no frontend knowledge needed
- 📊 **LangSmith Tracing** — monitor every agent run in real time
- 📦 **Modular structure** — easy to extend with new tools or swap the LLM

---

## 🗂️ Project Structure

```
agent_block/
├── main.py                  # Streamlit app entry point
├── .env                     # Your API keys 
├── .env.example             # Template for required environment variables
├── requirements.txt         # Project dependencies
│
├── agent/
│   ├── agent_ex.py          # Agent setup: prompt, memory, pipeline
│   ├── memory.py            # Custom sliding-window memory with summarization
│   ├── summon_llm.py        # LLM initialization (Groq via OpenAI-compatible API)
│   └── tools.py             # Agent tools (current_date + your custom tools)
│
└── config/
    └── summon_langsmith.py  # LangSmith tracing setup
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Youssef-Mohamed-Albiely/agent_block.git
cd agent_block
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
```

### 4. Run the app

```bash
streamlit run main.py
```

---

## 🔑 Required API Keys

| Service | Purpose | Free Tier |
|---|---|---|
| [Groq](https://console.groq.com) | LLM inference (fast & free) | ✅ Yes |
| [LangSmith](https://smith.langchain.com) | Agent tracing & debugging | ✅ Yes |
| [SerpAPI](https://serpapi.com) | Web search tool | ✅ 100 searches/month |

---

## 🛠️ How to Customize

This project is built as a template. Here's where to make changes:

### Change the system prompt
Edit `agent/agent_ex.py` → find `system_prompt` and write your agent's persona and rules.

### Add a new tool
Open `agent/tools.py` and add a new function with the `@tool` decorator:

```python
@tool
def my_custom_tool(input: str):
    """Describe what this tool does — the agent reads this description."""
    # your logic here
    return result
```

Then add it to the `all_tools` list at the bottom of the file.

### Change the LLM
Edit `agent/summon_llm.py` — swap the model name or switch to a different provider.

### Adjust memory window
In `agent/agent_ex.py`, change `"k": 20` in the `config` dict to control how many messages the agent remembers before summarizing.

---

## 📝 Example Use Cases

By customizing the system prompt and tools, this template can become:

- 🏥 A medical lab assistant (query patient records)
- 🛒 An e-commerce support agent (check orders, answer FAQs)
- 📚 A research assistant (web search + document summarization)
- 💼 An internal company bot (connect to your own database)

---

## 🤝 Contributing

Feel free to fork this project, open issues, or submit pull requests.
This is an open template — improvements are welcome.

---

## 👤 Author

**Youssef Mohamed Ali**
Building AI Agents | LangChain | Python

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
