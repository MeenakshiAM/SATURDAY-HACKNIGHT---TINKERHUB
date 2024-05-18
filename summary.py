import streamlit as st
import PyPDF2
from docx import Document
from transformers import pipeline

# Load pretrained summarization model
summarizer = pipeline("summarization")

# Function to extract text from PDF file
def extract_text_from_pdf(file):
    text = ""
    with open(file, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

# Function to extract text from Word document
def extract_text_from_docx(file):
    text = ""
    doc = Document(file)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Streamlit app
st.set_page_config(page_title="Document text summarizer", page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart: Document Text Summarizer")

uploaded_file = st.file_uploader("Upload a PDF or Word document", type=["pdf", "docx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1]
    if file_ext == "pdf":
        extracted_text = extract_text_from_pdf(uploaded_file)
    elif file_ext == "docx":
        extracted_text = extract_text_from_docx(uploaded_file)

    st.write("Extracted Text:")
    st.write(extracted_text)
    summary = summarizer(extracted_text, max_length=150, min_length=30, do_sample=False)

    st.write("Summary:")
    st.write(summary[0]['summary_text'])
