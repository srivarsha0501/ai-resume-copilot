# 🤖 AI Resume Analyzer
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sri-resume-ai.streamlit.app/)
# AI Resume Copilot

A Streamlit app that extracts text from PDFs, identifies skills, 
and uses Semantic Search (FAISS) to answer questions about a resume.

## Setup Instructions
1. Activate the environment: 
   venv\Scripts\activate

2. Install requirements:
   pip install streamlit pypdf2 sentence-transformers faiss-cpu python-dotenv openai

3. Set up your API Key:
   Create a .env file and add: OPENAI_API_KEY=your_sk_key_here

4. Run the app:
   streamlit run app.py

# 🤖 AI Resume Copilot (RAG Project)

AI Resume Copilot is an end-to-end Retrieval Augmented Generation (RAG) application that analyzes resumes, answers questions, matches jobs, scores resumes, and generates tailored resume versions.

## 🚀 Features

* Resume parsing (PDF)
* Skill extraction
* Resume embeddings + FAISS vector search
* Ask questions about resume (RAG)
* Resume ATS scoring
* Job matching using semantic similarity
* AI tailored resume generation
* Streamlit UI

## 🧠 Tech Stack

* Python
* Streamlit
* FAISS
* Sentence Transformers
* Ollama (local LLM)
* RAG architecture

## 💡 Key Concepts Demonstrated

* Embeddings
* Vector databases
* Semantic search
* Retrieval Augmented Generation
* LLM orchestration
* Prompt engineering

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

