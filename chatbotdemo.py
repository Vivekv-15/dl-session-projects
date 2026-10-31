
import streamlit as st

#import os 
#from dotenv import load_doten
#langchainimport

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="C++ RAG Chatbot")
st.title("C++ RAG Chatbot")
st.write("Ask any question related to C++ Introduction")

@st.cache_resource

def load_vectorstore():
    #Load Document
    loader = TextLoader("C++_Introduction", encoding="utf-8") 
    documents = loader.load()

    #Split Text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    final_documents = text_splitter.text_split_documents(documents)

    #embedding 
    embeddings= huggingFaceEmbeddings(
        model_name = "all-MiniLM-L6-v2"
    )


    #create FAISS Vector Store
    db=FAISS.from_documents(final_documents,embeddings)
    return db


    #load vector  DB(only once)
    db = load_vectorstore()
    query= st.text_input("Enter yout question about c++ :")

    #--------
    #user input
    #---------
    if query:
        docs = db.similarity_search(query, k=3)
        st.subheader("Recursived context:")
        for i, doc in enumerate(docs):
            st.write(f"Document {i+1}:**")
            st.write(doc.page_content)

