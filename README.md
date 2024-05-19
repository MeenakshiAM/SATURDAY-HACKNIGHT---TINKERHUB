

![Streamlit notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/e8052bb6-ad89-48c3-b6e9-124f94c1cd01)




# NOTES BUILDER CHAN
Content summarization app using Streamlit
## Team members
1. [Varalakshmi K G](https://github.com/MeenakshiAM)
2. [Meenakshi A M](https://github.com/Varalakshmi2354)
## product walkthrough
[link to video](Link Here)
## How it Works ?
1. The user can upload docx,pdf,pptx or text input from the user and generates summary
2. the user can play music while waiting for the summary to be generated
## Libraries used
Streamlit: Used for building interactive web applications with Python.
pptx: Used to work with Microsoft PowerPoint files (PPTX).
docx: Used to work with Microsoft Word files (DOCX).
transformers: Used for accessing pre-trained natural language processing models, particularly the summarization pipeline.
fitz: Used for extracting text from PDF files.
time: Used for adding time delays to simulate processing time.
## How to configure
Install the recquired libraries:
`pip install streamlit`
`pip install python-pptx`
`pip install python-docx`
`pip install transformers pymupdf`
## How to Run
`streamlit run document_summarizer.py`
make sure to use your own filename
