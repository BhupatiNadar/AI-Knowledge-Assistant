# 🤖 AI Knowledge Assistant

An AI-powered Knowledge Assistant that allows users to upload PDF documents, generate embeddings, and chat with their documents using Retrieval-Augmented Generation (RAG).

The system retrieves relevant document chunks, provides accurate answers, and includes source citations with page references for transparency and trust.

---

## 🌐 Live Demo

https://ai-knowledge-assistant-project.streamlit.app/

---

## ✨ Features

### 📄 Document Upload
- Upload PDF documents securely.
- Extract text from PDF pages automatically.
- Store document metadata and content in Supabase.

### 🧠 Intelligent Retrieval
- Generate embeddings using Sentence Transformers.
- Perform semantic similarity search.
- Retrieve the most relevant document chunks.

### 💬 AI-Powered Chat
- Ask questions in natural language.
- Get answers based only on uploaded documents.
- Maintain conversation history.

### 📚 Source Citations
- Every answer includes:
  - Source document name
  - Page number
- Improves transparency and trustworthiness.

### 🔍 Retrieval-Augmented Generation (RAG)
- Query embeddings generated from user questions.
- Relevant chunks retrieved from vector database.
- Context sent to the LLM for grounded responses.

### 👤 User Authentication
- User Signup
- User Login
- Secure password hashing with bcrypt

### 📜 Conversation History
- Save previous conversations.
- Resume old chats anytime.
- Delete conversations when needed.

### 📂 Document Management
- View uploaded documents.
- Delete documents.
- Generate embeddings from uploaded files.

---

## 🏗️ System Architecture

```text
User Query
    │
    ▼
Generate Query Embedding
    │
    ▼
Vector Search (Supabase)
    │
    ▼
Retrieve Relevant Chunks
    │
    ▼
Build Context
    │
    ▼
Groq LLM (Qwen 3 32B)
    │
    ▼
Answer + Source Citations
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- Supabase

### AI Models
- Groq (Qwen/Qwen3-32B)

### Embedding Model
- sentence-transformers/all-MiniLM-L6-v2

### PDF Processing
- PyMuPDF

### Authentication
- bcrypt

---

## 📁 Project Structure

```text
├── src/ 
    ├── UI/ 
    │   ├── __init__.py
    │   ├── __pycache__/ 
    │   │   ├── base_layout.cpython-313.pyc
    │   │   └── base_layout.cpython-313.pyc.2414922744208
    │   └── base_layout.py 
    ├── screens/ (5200 tokens)
    │   ├── __init__.py
    │   ├── __pycache__/ 
    │   │   ├── Login.cpython-313.pyc
    │   │   └── Signup.cpython-313.pyc
    │   ├── Setting.py
    │   ├── Documents.py 
    │   ├── History.py 
    │   ├── Home.py 
    │   ├── Chat.py 
    │   ├── Upload.py 
    │   ├── Login.py 
    │   └── Signup.py 
    ├── database/ 
    │   ├── __init__.py
    │   ├── config.py
    │   └── db.py 
    ├── assets/ 
    │   ├── user_logo_img.png
    │   ├── right_panel_img.png
    │   └── Signup_right_panel_img.jpg
    └── RAG/ (2400 tokens)
    │   ├── ingestion/ 
    │       ├── text_cleaner.py 
    │       └── chunker.py 
    │   ├── embeddings/ 
    │       └── embedder.py 
    │   ├── Generation/ 
    │       ├── searchtool.py 
    │       ├── agent.py 
    │       └── generation_pipline.py 
    │   ├── retrieval/ 
    │       └── retriever.py 
    │   └── pipline/ 
    │       └── ragpipline.py 
├── .gitignore
├── requirements.txt
├── .streamlit/ 
    └── config.toml
└── app.py 
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/AI-Knowledge-Assistant.git
cd AI-Knowledge-Assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL="your_supabase_url"
SUPABASE_KEY="your_supabase_key"
GROQ_API_KEY="your_groq_api_key"
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📋 Workflow

### Upload Phase

1. User uploads PDF.
2. PDF text is extracted.
3. Pages stored in Supabase.
4. Text cleaned.
5. Text chunked.
6. Embeddings generated.
7. Embeddings stored in database.

### Retrieval Phase

1. User asks a question.
2. Query embedding generated.
3. Similar chunks retrieved.
4. Context built from chunks.
5. Context sent to LLM.
6. Response returned with citations.

---

## 🎯 Example Questions

- Summarize the document.
- What are the main conclusions?
- What is the leave policy?
- Explain chapter 3.
- What benefits are mentioned?
- List important dates from the document.

---

## 🔒 Security

- Passwords hashed using bcrypt.
- User documents isolated by user ID.
- Secure API key management through Streamlit Secrets.
- Citation-based responses reduce hallucinations.

---

## 🚀 Future Improvements

- Multi-document chat
- Hybrid Search (Keyword + Vector)
- Reranking
- OCR Support
- Document Summarization
- Multi-LLM Support
- Bookmark System
- Citation Highlighting
- Streaming Responses
- Role-Based Access Control

---

## 👨‍💻 Author

Bhupati Nadar

GitHub:
https://github.com/BhupatiNadar

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🛠️ Contribute improvements

---
Built with ❤️ using Streamlit, Supabase, Groq, and RAG.
