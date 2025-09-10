from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv
from typing import List
from langchain.schema import Document

#Extract Data From the PDF File
loader = DirectoryLoader(
    path="data" ,
    glob='*.pdf' ,
    loader_cls=PyPDFLoader
)

docs = loader.load()

#Split the Data into Text Chunks
splitter = CharacterTextSplitter(
    separator="",
    chunk_size = 500 ,
    chunk_overlap = 20
)

text_chunk = splitter.split_documents(docs)
print(len(text_chunk))
print(text_chunk)

#Download the Embeddings from HuggingFace 
def download_embeddings():
    """ 
    Download and return the HuggingFace embedding model
    """
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    embedding = HuggingFaceEmbeddings(model_name=model_name)
    return embedding

# Call function
# embedded_data = download_embeddings()
