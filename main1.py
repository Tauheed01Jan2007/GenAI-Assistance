import os
from constants import GEMINI_API_KEY 
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

os.environ["GEMINI_API_KEY"]=GEMINI_API_KEY

st.title("!! our first langchain Demo !!")
input_text = st.text_input("search here")

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash",
    temperature = 0.8
)

if input_text:
    response = llm.invoke(input_text)
    st.write(response.content[0]["text"])