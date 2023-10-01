import streamlit as st
import langchain_helper as lch
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.sidebar.text_area(label="Enter a youtube url")
        query = st.sidebar.text_area(label="What is your question", max_chars=50, key="query")
        submit_button = st.form_submit_button(label="Submit")

if query and youtube_url:
    db = lch.create_vector_db(youtube_url)
    response = lch.get_response(db, query, k=4)
    response = textwrap.fill(response, width=50)
    st.subheader("Answer")
    st.text(response)