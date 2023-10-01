import streamlit as st
import langchain_helper as lch

st.title("Property Management Assistant Demo")
with st.sidebar:
    with st.form(key="my_form"):
        complaint = st.sidebar.text_area(label="What is the problem?", max_chars=50, key="complaint")
        submit_button = st.form_submit_button(label="Submit")
if complaint and submit_button:
    answer = lch.generate_story(complaint)
    audio = lch.text2speech(answer)
    # audio = lch.elevenlabvoice(answer)