import streamlit as st
from pptx import Presentation
from docx import Document
from transformers import pipeline

# Load pretrained summarization model
summarizer = pipeline("summarization")

# Function to extract text from a PowerPoint file
def extract_text_from_ppt(ppt):
    pr = Presentation(ppt)
    text = []
    for slide in pr.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text.append(shape.text)
    return "\n".join(text)

# Function to extract text from a Word document
def extract_text_from_docx(file):
    text = ""
    doc = Document(file)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Streamlit app configuration
st.set_page_config(page_title="Document Text Summarizer", page_icon="🗒️", layout="wide")
st.title("🗒️  NOTES BUILDER CHAN")

# Display an image
try:
    st.image('study.jpg', caption='THE ONE AND ONLY')
except FileNotFoundError:
    st.warning("Image file 'study.jpg' not found.")

# File uploader for PPTX or DOCX files
uploaded_file = st.file_uploader("Upload a PPT or Word document", type=["pptx", "docx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1]
    if file_ext == "pptx":
        extracted_text = extract_text_from_ppt(uploaded_file)
    elif file_ext == "docx":
        extracted_text = extract_text_from_docx(uploaded_file)

    st.write("Extracted Text:")
    st.write(extracted_text)
    
    # Ask user for summary length
    st.write("Set Summary Length:")
    min_length = st.number_input("Minimum Length of Summary", min_value=30, max_value=100, value=30)
    max_length = st.number_input("Maximum Length of Summary", min_value=50, max_value=500, value=150)
    
    if st.button("Generate Summary"):
        if extracted_text:
            summary = summarizer(extracted_text, max_length=max_length, min_length=min_length, do_sample=False)
            st.write("SUMMARY :")
            st.write(summary[0]['summary_text'])
        else:
            st.write("No text extracted to summarize.")
