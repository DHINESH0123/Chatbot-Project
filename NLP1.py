import streamlit as st
import PyPDF2 as pdf
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
import os
import warnings
warnings.filterwarnings("ignore")

load_dotenv()

# Upload your API key in streamlit sidebar
GEMNI_Api_Key = st.sidebar.text_input(label="🔑 Enter your Gemni API key", type="password")

# Extract the text from the PDF
def input_text(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Generating a LLM response
def get_response(input):
    try:
        llm= GoogleGenerativeAI(
            model="gemini-2.5-flash-preview-04-17",  # Correct model name per Groq docs
            api_key=GEMNI_Api_Key
        )
        response=llm.invoke(input)
        return response
    except Exception as e:
        return f"An error occurred: {e}"
    

# Streamlit App UI

st.header("📄 NotePad LLM - PDF Analyzer")
AD = st.text_area("📝 Type your query or topic related to the PDF")
File = st.file_uploader("📎 Upload your PDF file", type="pdf", help="Only PDF files are supported.")   
submit = st.button("🚀 Submit")

if submit:
    if not GEMNI_Api_Key:
        st.warning("Please enter your Gemni API key.")
    elif File is None:
        st.warning("Please upload a PDF file.")
    else:
        with st.spinner("🔍 Analyzing your document. Please wait..."):
            text = input_text(File)

            full_prompt = f"""Summarize the following PDF document based on the topic: "{AD}" (if applicable).

Document content:
{text}

Summary:
"""
            response = get_response(full_prompt)
            if response:
                st.write(response)
                st.success("✅ Analysis Completed")
