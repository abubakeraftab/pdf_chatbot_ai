
# 🧠 PDF Chatbot with Python, FastAPI & OpenAI

This project is an AI-powered chatbot that can answer questions based on the content of uploaded PDF documents. It combines FastAPI for the backend, sentence-transformers + FAISS for semantic search, and OpenAI GPT for generating answers.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🤖 Ask questions in natural language
- 🔍 Semantic search with Sentence Transformers
- 🧠 GPT-3.5-turbo-powered answers
- ⚡ FastAPI backend with HTML frontend
- 🐳 Dockerized for easy deployment

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-chatbot-ai.git
cd pdf-chatbot-ai
```

### 2. Create .env file
```bash
OPENAI_API_KEY=your_openai_key_here
```

### 3. Create a virtual environment and install dependencies
```bash

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### 4. Run the App
```bash
uvicorn app.main:app --reload
Visit: http://localhost:8000
```
### 🐳 Docker Deployment
Build Docker image
```bash

docker build -t pdf-chatbot .
```
Run Docker container
```bash
docker run -p 8000:8000 pdf-chatbot
```

### 🧩 API Endpoints
| Method | Endpoint   | Description                       |
| ------ | ---------- | --------------------------------- |
| `GET`  | `/`        | Loads the frontend chat interface |
| `POST` | `/upload/` | Upload a PDF file                 |
| `POST` | `/ask/`    | Ask a question based on the PDF   |

### 📂 Project Structure
pdf-chatbot-ai/
├── app/
│   ├── main.py
│   ├── chatbot.py
│   ├── vector_store.py
│   └── pdf_parser.py
├── interface/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
├── README.md
