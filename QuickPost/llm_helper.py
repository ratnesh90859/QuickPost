from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

try:
    load_dotenv()
except:
    
    pass


groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    
    import streamlit as st
    groq_api_key = st.secrets.get("GROQ_API_KEY", "")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are ")
    print(response.content)
