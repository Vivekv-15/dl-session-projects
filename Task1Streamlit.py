import streamlit as st
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="C++ Document Search", page_icon="🔎", layout="wide")

st.title("🔎 C++ Document Search")
st.write("Ask a question about the content of **task1data.txt**.")

DATA_FILE = "task1data.txt"

@st.cache_resource
def create_vector_database():
    # Data loading
    loader = TextLoader(DATA_FILE, encoding="utf-8")
    cppdata = loader.load()

    # Text splitting
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=200
    )
    finalDocuments = text_splitter.split_documents(cppdata)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # FAISS vector store
    db = FAISS.from_documents(finalDocuments, embeddings)

    return db

# Check that the required text file exists
if not os.path.exists(DATA_FILE):
    st.error(
        f"'{DATA_FILE}' was not found. "
        "Put task1data.txt in the same folder as app.py."
    )
    st.stop()

try:
    db = create_vector_database()
    st.success("Document loaded and vector database created.")
except Exception as e:
    st.error(f"Error while creating the vector database: {e}")
    st.stop()

query = st.text_input(
    "Enter your query:",
    placeholder="Example: What is a class in C++?"
)

if st.button("Search", type="primary"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Searching..."):
            docs = db.similarity_search(query)

        st.subheader("Relevant Results")

        if not docs:
            st.info("No relevant documents found.")
        else:
            for i, doc in enumerate(docs, start=1):
                with st.expander(f"Result {i}", expanded=True):
                    st.write(doc.page_content)

st.sidebar.header("Project Information")
st.sidebar.write("**Embedding model:** all-MiniLM-L6-v2")
st.sidebar.write("**Vector store:** FAISS")
st.sidebar.write("**Chunk size:** 200")
st.sidebar.write("**Chunk overlap:** 200")
