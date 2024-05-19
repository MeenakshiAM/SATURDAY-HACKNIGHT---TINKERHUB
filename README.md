

![Streamlit notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/e8052bb6-ad89-48c3-b6e9-124f94c1cd01)




# SUMMARY GENERATOR CHAN
Content summarization app using Streamlit
## Team members
1. [Varalakshmi K G](https://github.com/MeenakshiAM)
2. [Meenakshi A M](https://github.com/Varalakshmi2354)
## product walkthrough
[link to video](Link Here)

![Screenshot 2024-05-19 110629](https://github.com/MeenakshiAM/SATURDAY-HACKNIGHT---TINKERHUB/assets/140526841/bad5e54d-196b-4d51-8b00-544f1260f12f)
![Screenshot 2024-05-19 110645](https://github.com/MeenakshiAM/SATURDAY-HACKNIGHT---TINKERHUB/assets/140526841/32daa384-4a7c-4307-9f4d-d295dafdfdc4)
![Screenshot 2024-05-19 111019](https://github.com/MeenakshiAM/SATURDAY-HACKNIGHT---TINKERHUB/assets/140526841/1c88226f-7a71-4241-bbe3-26f50221ade8)


## How it Works ?
1. The user can upload docx,pdf,pptx or text input from the user and generates summary
2. the user can play music while waiting for the summary to be generated
## Libraries used
Streamlit: Used for building interactive web applications with Python.<br>
pptx: Used to work with Microsoft PowerPoint files (PPTX).<br>
docx: Used to work with Microsoft Word files (DOCX).<br>
transformers: Used for accessing pre-trained natural language processing models, particularly the summarization pipeline.<br>
fitz: Used for extracting text from PDF files.<br>
time: Used for adding time delays to simulate processing time.
## How to configure
Install the recquired libraries:<br>
`pip install streamlit`<br>
`pip install python-pptx`<br>
`pip install python-docx`<br>
`pip install transformers`<br>
`pip install pymupdf`
## How to Run
`streamlit run document_summarizer.py`
make sure to use your own filename
