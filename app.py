from flask import Flask, render_template, request
# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize, word_tokenize
# import spacy
from pdfminer.high_level import extract_text
from docx import Document
import os
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load Spacy French model
# nlp = spacy.load('fr_core_news_sm')

# Model names
Bart = "facebook/bart-large-cnn" 
mT5 = "csebuetnlp/mT5_multilingual_XLSum"

# Initialize the summarization pipeline
Bart_Summarizer = pipeline("summarization", model=Bart, tokenizer=Bart)
mT5_summarizer = pipeline("summarization", model=mT5, tokenizer=mT5)

def read_pdf(file_path):
    text = extract_text(file_path)
    return text

def read_word(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def summarize_file(file_path):
    # Text Extraction
    if file_path.endswith('.pdf'):
        text = read_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = read_word(file_path)
    elif file_path.endswith('.txt'):
        with open(file_path) as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file format")
    
    # Work
    B_summary = Bart_Summarizer(text, num_workers = 6)
    mT5_summary = mT5_summarizer(text, num_workers = 6)

    return B_summary[0]['summary_text'], mT5_summary[0]['summary_text']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and (file.filename.endswith('.pdf') or file.filename.endswith('.docx')or file.filename.endswith('.txt')):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        try:
            summary, main_theme = summarize_file(file_path)
            return render_template('index.html', summary=summary, main_theme=main_theme)
        except Exception as e:
            return f"An error occurred: {str(e)}", 500
    return "Unsupported file format", 400
 
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)