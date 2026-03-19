# 🤖 Rule-Based Chatbot (Pattern Matching)

A simple **Rule-Based Chatbot** built using **Python** that demonstrates how conversational systems can be created using **pattern matching, intents, and predefined rules**.

This chatbot supports basic conversation flows such as greetings, help, small talk, and can also answer domain-specific questions using a **knowledge base**. It runs interactively in the console and logs all conversations.

---

# 📌 Project Overview

Chatbots are widely used in applications like customer support, virtual assistants, and information systems. This project demonstrates a **rule-based approach** to chatbot development without using complex machine learning models.

The chatbot works by:

- Matching user input with predefined patterns
- Identifying user intent
- Returning appropriate rule-based responses
- Fetching answers from a small knowledge base

---

# ✨ Features

- Pattern matching using simple rules
- Intent recognition (greetings, help, small talk, exit)
- Rule-based responses
- Domain-specific knowledge base (AI-related questions)
- Interactive console-based chatbot
- Conversation history logging
- Simple and easy-to-understand implementation

---

# 🧠 Supported Intents

| Intent | Example Inputs |
|------|---------------|
| Greeting | hi, hello, hey |
| Help | help, assist |
| Small Talk | how are you, what's up |
| Exit | bye, quit, exit |

---

# 📚 Knowledge Base

The chatbot includes a small built-in knowledge base to answer questions like:

- What is AI?
- What is Machine Learning?
- What is Python?
- What is Data Science?

---

# 🗂 Project Structure
rule_based_chatbot/
│
├── main.py # Entry point (runs chatbot)
├── chatbot.py # Chatbot logic and intent handling
├── knowledge_base.py # Domain knowledge (Q&A)
├── logger.py # Conversation logging
└── README.md

---

# ⚙️ How It Works

The chatbot follows a simple pipeline:

    User Input → Pattern Matching → Intent Detection → Response Generation

1. User enters a message
2. System checks:
   - Knowledge base (exact match)
   - Intent patterns (regex)
3. Returns appropriate response
4. Logs the conversation

---

# 📥 Installation

Clone the repository:
```bash
    git clone https://github.com/tayade-aniket/Syntecxhub-rule-based-chatbot.git
```

Navigate to the project folder:
```bash
    cd Syntecxhub-rule-based-chatbot
```

---

# ▶️ Running the Chatbot

Run the chatbot using:
```bash
    python main.py
```

---

# 💬 Example Interaction
```bash
    === Rule-Based Chatbot ===
    Type 'exit' to quit

    You: hi
    Bot: Hello! How can I help you today?

    You: what is ai
    Bot: Artificial Intelligence is the simulation of human intelligence in machines.

    You: how are you
    Bot: I'm just a bot, but I'm doing great! How about you?

    You: help
    Bot: I can answer basic AI questions or chat with you.

    You: bye
    Bot: Goodbye! Have a nice day.
```
---

# 📝 Conversation Logging

All conversations are stored in:
```bash
    chat_log.txt
```

---

# 👨‍💻 Author
Mr. Aniket G. Tayade
