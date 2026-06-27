# 🔬 Agentic Research Assistant

An advanced **Human-in-the-Loop AI Research Agent** built with **LangGraph**, **Groq**, **Tavily Search**, and **Streamlit**.

🚀 **Live Demo:** https://anhu321-agentic-research-assistant.hf.space

The system performs autonomous research by:

1. Rewriting user questions into optimized search queries.
2. Searching the web using Tavily.
3. Synthesizing findings into a comprehensive answer using an LLM.
4. Critically evaluating answer quality.
5. Requesting human approval before finalizing.
6. Iteratively improving responses using human feedback.

This creates a research workflow that combines **AI autonomy** with **human oversight**, making outputs more reliable and trustworthy.

---

# 🚀 Live Demo

🌐 **Try the application here:**

**https://anhu321-agentic-research-assistant.hf.space**

No installation required—simply open the link and start using the AI-powered research assistant.

---

## ✨ Features

### 🧠 Intelligent Query Rewriting

The agent rewrites vague or broad questions into focused, high-signal search queries before performing web research.

Example:

**User Query**

> Impact of AI on software engineering jobs

**Rewritten Query**

> AI impact on software engineering employment trends 2025

---

### 🌐 Autonomous Web Research

Uses **Tavily Search** to gather relevant web information from multiple sources.

Each result includes:

* Title
* URL
* Content snippet

---

### 📝 Research Synthesis

The LLM combines:

* User query
* Search results
* Retrieved context

into a structured research report containing:

* Key findings
* Evidence-backed insights
* Source citations
* References section

---

### 🔍 Self-Critique (Critic Agent)

Before presenting an answer, a dedicated critic node evaluates:

* Source support
* Completeness
* Relevance
* Quality

If the answer is weak, the system automatically retries with improved research.

---

### 👨‍💻 Human-in-the-Loop Approval

The workflow pauses before completion and requests human review.

Users can:

✅ Approve the answer

or

🔄 Provide feedback such as:

> Add more recent examples

> Include industry statistics

> Compare with Europe

The feedback is injected into the next research cycle.

---

### ♻️ Iterative Improvement Loop

Rejected answers trigger:

```text
Human Feedback
        ↓
Query Rewrite
        ↓
Web Search
        ↓
Answer Generation
        ↓
Critic Review
        ↓
Human Review
```

This continues until the answer is approved.

---

### 📚 Research History

The Streamlit interface stores previous research sessions and allows users to revisit completed investigations.

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │ User Question    │
                    └─────────┬────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │ Query Rewriter     │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │ Tavily Search      │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │ LLM Synthesizer    │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │ Critic Agent       │
                   └───────┬────────────┘
                           │
             Retry Needed? │
                           ▼
                    ┌──────────┐
                    │  Retry   │
                    └──────────┘

                           │
                           ▼

                ┌────────────────────┐
                │ Human Approval     │
                └───────┬────────────┘
                        │
           Approved?    │
                        ▼

                     END
```

---

## 🛠️ Tech Stack

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| LangGraph     | Agent workflow orchestration |
| Groq          | High-speed LLM inference     |
| Llama 3.3 70B | Reasoning and synthesis      |
| Tavily        | Web search                   |
| Streamlit     | Frontend UI                  |
| LangChain     | LLM abstractions             |
| Python        | Backend                      |

---

## 📂 Project Structure

```text
project/
│
├── agent.py
├── app.py
├── requirements.txt
├── .env
└── README.md
```

### agent.py

Contains:

* State definition
* LangGraph workflow
* Query rewrite node
* Search node
* Synthesizer node
* Critic node
* Human approval node

### app.py

Provides:

* Streamlit UI
* Research history
* Approval workflow
* Session management

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/agentic-research-assistant.git

cd agentic-research-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run Application

### Option 1: Use the Live Demo

Open your browser and visit:

**https://anhu321-agentic-research-assistant.hf.space**

---

### Option 2: Run Locally

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Example Workflow

### Step 1

User asks:

```text
What are the latest developments in quantum computing?
```

### Step 2

Agent rewrites the query.

### Step 3

Agent performs web research.

### Step 4

LLM generates a research report.

### Step 5

Critic validates the answer quality.

### Step 6

Human reviews the output.

### Step 7

If rejected:

```text
Include recent breakthroughs from IBM and Google.
```

The agent performs another research cycle.

### Step 8

Human approves the final answer.

---

## State Management

The workflow uses a custom `ResearchState`.

```python
class ResearchState(TypedDict):
    query: str
    search_query: str
    web_results: str
    final_answer: str
    needs_retry: bool
    retry_count: int
    human_approved: bool
    human_feedback: str
```

This state is persisted through LangGraph checkpoints, enabling interruptions and resumptions.

---

## Future Improvements

* PDF export of research reports
* Multi-agent debate system
* Research memory across sessions
* Citation verification
* RAG integration
* Deep research mode
* Multi-source ranking
* Knowledge graph generation
* Report generation with charts

---

## Why This Project?

Most AI research assistants either:

* Generate answers without verification
* Search the web without reasoning
* Lack human oversight

This project combines:

✅ Autonomous Search

✅ Structured Reasoning

✅ Self-Critique

✅ Human Feedback

✅ Iterative Improvement

to create a more reliable AI research workflow.

---

## License

MIT License

---

## Author

Built using:

* LangGraph
* Groq
* Tavily
* Streamlit

for creating production-style Human-in-the-Loop AI agents.
