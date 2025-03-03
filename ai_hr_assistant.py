import os
import streamlit as st
import openai
import fitz  # PyMuPDF for PDF processing
import pandas as pd
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# Function to extract text from an uploaded PDF
def extract_text_from_pdf(pdf_file):
    try:
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            text = "\n".join([page.get_text() for page in doc])
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# Function to analyze CV vs Job Description
def analyze_cv_vs_jd(cv_text, jd_text):
    prompt = f"""
    Given the following Job Description (JD):
    {jd_text}

    And the following Candidate's CV:
    {cv_text}

    Provide:
    1. Match Score (0-100%)
    2. Key skills that match
    3. Areas where the candidate is lacking
    4. Overall recommendation (Fit / Not Fit / Consider for another role)
    """
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert AI HR assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Function to generate interview questions
def generate_interview_questions(jd_text, cv_text):
    prompt = f"""
    Based on the following Job Description:
    {jd_text}
    
    And the following Candidate's CV:
    {cv_text}
    
    Generate 5 personalized interview questions to assess the candidate’s fit.
    """
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert interviewer generating insightful questions."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("🤖 AI Talent Match & Interview Assistant")

# Session state initialization
if "cv_text" not in st.session_state:
    st.session_state.cv_text = None
if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "questions" not in st.session_state:
    st.session_state.questions = None

uploaded_cv = st.file_uploader("📂 Upload Candidate CV (PDF)", type=["pdf"])
uploaded_jd = st.text_area("📋 Paste Job Description Here")

if uploaded_cv is not None and uploaded_jd:
    if st.session_state.cv_text is None:
        st.session_state.cv_text = extract_text_from_pdf(uploaded_cv)

    st.subheader("📑 Extracted CV Text")
    st.text_area("Extracted CV Text", st.session_state.cv_text, height=200, label_visibility="collapsed")
    
    if st.button("Analyze Candidate Fit"):
        st.session_state.analysis = analyze_cv_vs_jd(st.session_state.cv_text, uploaded_jd)

    if st.session_state.analysis:
        st.subheader("📊 Candidate Analysis")
        st.write(st.session_state.analysis)

    if st.button("Generate Interview Questions"):
        st.session_state.questions = generate_interview_questions(uploaded_jd, st.session_state.cv_text)

    if st.session_state.questions:
        st.subheader("🎤 AI-Generated Interview Questions")
        st.write(st.session_state.questions)
