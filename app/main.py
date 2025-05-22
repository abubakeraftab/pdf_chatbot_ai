# importing libraries and frameworks for building APIs and file handling
from fastapi import FastAPI, UploadFile,File,Form
from fastapi.responses import HTMLResponse
import shutil
import os
from app.pdf_parser import extract_text_pdf
from app.chatbot import ingest_text, answer_questions

#Initializ FastAPI application
app=FastAPI()

@app.get('/',response_class=HTMLResponse)
def root():
    
    #Open and return the HTML file
    with open("interface/index.html","r") as f:
        return f.read()

@app.post("/upload/")
async def upload_file(file:UploadFile=File(...)):
    path=f"temp/{file.filename}"
    os.makedirs("temp",exist_ok=True)
    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    try:
        #Extract text from saved PDF
        text=extract_text_pdf(path)
        # Ingest the text into the vector store
        ingest_text(text)
        return{"File uploaded and text ingested"}
    except Exception as e:
        return {"Failed to process"+' '+str(e)}

@app.post("/ask/")
async def ask(question:str=Form(...)):
    
    try:
        # Use the chatbot logic to answer based on ingested PDF text
        answer=answer_questions(question)
        return {"answer":answer}
    except Exception as e:
        return {"Failed to process question"+' '+str(e)}
        

    
