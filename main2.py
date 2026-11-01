import os
from constants import GEMINI_API_KEY
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain, SequentialChain
from langchain_classic.memory import ConversationBufferMemory

os.environ["GEMINI_API_KEY"]=GEMINI_API_KEY

st.title("!! Pentastic football Player !!")
input_text = st.text_input("search here")

   # First Template
first_input_prompt = PromptTemplate(
    input_variables= ["name"],
    template="tell me about {name}"
)

   # Memory
person_memory = ConversationBufferMemory(
    input_keys = "name",
    memory_keys = "chat_history"
)

   # 
llm = ChatGoogleGenerativeAI(     
    model = "gemini-3.5-flash",
    temperature = 0.8
)

if input_text:
    prompt = first_input_prompt.format(name=input_text)
    response = llm.invoke(prompt)
    st.write(response.content[0]["text"]) 