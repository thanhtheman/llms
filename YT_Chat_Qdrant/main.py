from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import YoutubeLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = QdrantClient(
    url=os.getenv("QDRANT_URL"), 
    api_key=os.getenv("QDRANT_API_KEY")
)

# we only run this ONCE to create the collection
# client.recreate_collection(
#     collection_name="first-collection",
#     #1536 dimensions vector for OpenAIEmbeddings
#     vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
# )

# we only run this ONCE load and split the youtube transcript into chunks
# url = "https://www.youtube.com/watch?v=2eWuYf-aZE4&t=5s"
# def get_chunks(youtube_url):
#     loader = YoutubeLoader.from_youtube_url(youtube_url)
#     transcript = loader.load()
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=100,
#         length_function=len
#     )
#     chunks = text_splitter.split_documents(transcript) # this will return a list of documents
#     return chunks


embeddings = OpenAIEmbeddings()
# as the chunks are documents, we use from_documents method, we only run this ONCE to add the youtube transcript and create a vector store
# Qdrant.from_documents(get_chunks(url), embeddings, url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"), collection_name="first-collection")
vector_store = Qdrant(collection_name="first-collection", embeddings=embeddings, client=client, distance_strategy="COSINE")


#creating a chat feature
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.7), chain_type="stuff", retriever=vector_store.as_retriever(),return_source_documents=True)

query = "what is stable diffusion?"
# response = qa.run(query)
response = qa({"query": query})
# print(response["result"])

# we can take it one step further by feeding this result into another prompt to ask LLM to check if how good the answer is.
print(response["source_documents"])
