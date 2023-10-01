from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings()

def create_vector_db(youtube_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(youtube_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)
    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    #joining 4 documents together seperated by a space
    docs_page_content = " ".join([d.page_content for d in docs])
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.7)
    prompt = PromptTemplate(input_variables=["question", "docs"], 
    template="""You are a helpful Youtube assistant that can answer questions about
    videos bsaed on the video's transcript. 
    Answer the following questions: {question}
    By searching the following video transcript: {docs} 
    Only use the factual information from the transcript to answer the question.
    If you feel like you don't have enough information to answer the question. Please say 
    "I don't know".
    Your answers should be detailed.""")
    response = LLMChain(llm=llm, prompt=prompt).predict(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response


