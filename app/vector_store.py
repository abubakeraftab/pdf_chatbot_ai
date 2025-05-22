# Import the SentenceTransformer for embedding text using pre-trained models
from sentence_transformers import SentenceTransformer
# Import FAISS for efficient similarity search in vector space
import faiss
# Import numpy for array operations
import numpy as np

class PDFVector:
    """
    A class to vectorize and semantically search PDF text using SentenceTransformers + FAISS.
    """
    def __init__(self):
        self.model=SentenceTransformer('all-MiniLM-L6-v2')
        self.index=faiss.IndexFlatL2(384)
        self.chunks=[]
    
    def add_text(self,text):
        """
        Splits text into chunks, generates embeddings, and stores them in the FAISS index.
        """
        chunks=[text[i:i+500] for i in range(1,len(text),500)]
        embedding=self.model.encode(chunks)
        self.index.add(np.array(embedding).astype('float32'))
        self.chunks.extend(chunks)
        
    def search(self,query,top_k=5):
        """
        Performs a semantic search against the indexed chunks using vector similarity.
        """
        query_embedding=self.model.encode([query]).astype('float32')
         # Search for the most similar vectors (chunks) in the FAISS index
        D,I=self.index.search(query_embedding,top_k)
         # Return the matched text chunks, filtered to avoid index errors
        return [self.chunks[i] for i in I[0] if i < len(self.chunks)]
    
