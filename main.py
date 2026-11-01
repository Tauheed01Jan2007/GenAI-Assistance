import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

llm = ChatGoogleGenerativeAI(
    
    model = "gemini-3.5-flash",
    #Temperature = 0.7
    
)
response = llm.invoke("what is Generative AI?")

print(response.content[0]["text"])