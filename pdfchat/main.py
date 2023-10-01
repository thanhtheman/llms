import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings import HuggingFaceInstructEmbeddings, OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="n/", chunk_size=1000, chunk_overlap=200, length_function=len ) 
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    #pip install InstructorEmbedding and sentence_transformers
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    print("vector store is successfully created!")
    return vector_store

def main():
    st.set_page_config(page_title="chat with pdfs", page_icon=":books:")
    st.header("chat with pfd")
    st.text_input("ask a question")

    with st.sidebar:
        st.subheader("your documents")
        pdf_docs = st.file_uploader("upload your documents", accept_multiple_files=True)
        if st.button("process"):
            with st.spinner("processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vectorstore(text_chunks)
    

if __name__ == "__main__":
    main()
