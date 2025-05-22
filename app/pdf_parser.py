#importing library to extract text from PDF
import pdfplumber

def extract_text_pdf(file):
    """
    Extracts all text content from a PDF file using pdfplumber.
    """
    try:
        text=""
        # Open the PDF file using pdfplumber
        with pdfplumber.open(file) as pdf:
             # Iterate through each page of the PDF
            for p in pdf.pages:
                page_text=p.extract_text()
                # If text is found, add it to the full text string
                if page_text:
                    text+=page_text+"\n"
        return text
    except Exception as e:
        raise RuntimeError("PDF extraction error")
            
        