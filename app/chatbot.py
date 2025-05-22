from app.vector_store import PDFVector
from openai import OpenAI

# Import dotenv to load API key from .env file
from dotenv import load_dotenv
import os

# Initialize the vector store for storing PDF embeddings
store=PDFVector()
# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key securely
api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def ingest_text(text):
    
    """
    Takes raw PDF text and adds it to the vector store by generating embeddings.
    This enables semantic search later.
    """
    store.add_text(text)

def answer_questions(questions):
    
    """
    Takes raw PDF text and adds it to the vector store by generating embeddings.
    This enables semantic search later.
    """
    try:
        chunks=store.search(questions)
        context = "\n".join(chunks)
        
        # Construct a system prompt for GPT model
        prompt = f"""
        You are a helpful assistant. Use the following PDF content to answer the user's question.

        PDF Content:
        {context}

        Question: {questions}
        Answer:
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        # Extract and return the chatbot’s reply from the response
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Chatbot error"
        
    