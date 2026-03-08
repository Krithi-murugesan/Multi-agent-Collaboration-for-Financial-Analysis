# Multi-agent-Collaboration-for-Financial-Analysis
AI agents working together via CrewAI to analyze financial data, generate insights, and support investment decisions
# 📊 Multi-Agent Financial Analysis System (CrewAI)

A **multi-agent AI system for financial market analysis** built using **CrewAI**.
The project simulates a collaborative team of AI agents that analyze market data, develop trading strategies, evaluate risks, and suggest optimal trade execution plans.

This system demonstrates how **autonomous AI agents can collaborate to perform complex financial analysis tasks**.

---

# 🚀 Features

* 🤖 **Multi-Agent Collaboration** using CrewAI
* 📈 **Market Data Analysis** for identifying trends and signals
* 💡 **Automated Trading Strategy Generation**
* ⚡ **Trade Execution Planning** based on market conditions
* 🛡️ **Risk Assessment & Mitigation Analysis**
* 🔎 **Web Search + Website Scraping** using Serper & Scrape tools

---

# 🧠 Agent Architecture

The system consists of **four specialized AI agents**:

### 1️⃣ Data Analyst Agent

* Monitors and analyzes financial market data
* Detects trends and predicts potential market movements
* Uses web search and scraping for market insights

### 2️⃣ Trading Strategy Developer

* Generates trading strategies based on analytical insights
* Considers user-defined **risk tolerance**
* Evaluates multiple strategy approaches

### 3️⃣ Trade Advisor

* Determines optimal trade execution timing
* Suggests pricing and entry/exit strategies
* Aligns execution with trading strategies

### 4️⃣ Risk Management Advisor

* Performs risk analysis on proposed strategies
* Identifies potential market threats
* Suggests mitigation strategies

---

# ⚙️ Tech Stack

* **CrewAI** – Multi-agent orchestration
* **OpenAI GPT Models** – Reasoning and decision making
* **LangChain OpenAI** – LLM integration
* **Serper API** – Real-time search
* **CrewAI Tools** – Web scraping and data collection
* **Python**

---

# 📂 Project Structure

```
financial-analysis-crewai/
│
├── main.py                # Main crew orchestration
├── requirements.txt       # Dependencies
├── .env                   # API keys
└── README.md
```

---

# 🔑 Environment Setup

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
OPENAI_MODEL_NAME=gpt-3.5-turbo
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/crewai-financial-analysis.git
cd crewai-financial-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run the main script:


python main.py

Example input:

```
Stock: AAPL
Initial Capital: $100000
Risk Tolerance: Medium
Strategy Preference: Day Trading
```

The agents will collaborate and generate:

* Market insights
* Trading strategies
* Execution plan
* Risk analysis report

---

# 📊 Example Workflow

```
Market Data → Data Analyst Agent
                 ↓
        Trading Strategy Agent
                 ↓
         Trade Execution Agent
                 ↓
          Risk Management Agent
```

Each agent contributes specialized knowledge to produce a **comprehensive trading recommendation**.

---

# 🎯 Use Cases

* AI-powered financial research
* Autonomous trading assistants
* LLM multi-agent experimentation
* FinTech AI prototyping
* Portfolio project for AI/ML engineers

---

# ⚠️ Disclaimer

This project is **for educational and research purposes only**.
It does **not provide financial advice** and should not be used for real trading decisions.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

# 📜 License

MIT License
