
# Flask Application for Automatic Text Summarization

This Flask application allows users to upload PDF, DOCX, or TXT files and automatically generates a summary of the content using summarization models based on Hugging Face's `transformers` library.

## Features

- **File Upload**: Users can upload PDF, DOCX, or TXT files through the web interface.
- **Text Extraction**: Text is extracted from PDF and DOCX files using `pdfminer` and `python-docx`.
- **Automatic Summarization**: The extracted text is summarized using two summarization models: BART (`facebook/bart-large-cnn`) and mT5 (`csebuetnlp/mT5_multilingual_XLSum`).

## Dependencies

- `Flask`: A lightweight web framework for Python.
- `pdfminer`: A tool for extracting text from PDF files.
- `python-docx`: A library for working with Word documents.
- `transformers`: Hugging Face's library for NLP (Natural Language Processing) models.

## Code Structure

- **Flask Application Initialization**: The Flask application is initialized with a configured upload folder.
- **Model Loading**: Two summarization models (BART and mT5) are initialized to generate summaries.
- **Text Extraction Functions**:
  - `read_pdf(file_path)`: Extracts text from a PDF file.
  - `read_word(file_path)`: Extracts text from a DOCX file.
- **Summarization Function**:
  - `summarize_file(file_path)`: Extracts text from the uploaded file and generates summaries using the BART and mT5 models.
- **Flask Routes**:
  - `'/'`: Displays the homepage with a file upload form.
  - `'/upload'`: Handles file uploads and returns the generated summaries.

## Usage

1. Clone the repository and install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create the upload folder if necessary:
   ```bash
   mkdir uploads
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Access the application via a web browser at `http://127.0.0.1:5000/` and upload a file to get its summary.

## Notes

- This application is designed to work with files in PDF, DOCX, and TXT formats.
- Ensure that the BART and mT5 models are downloaded correctly during the pipeline initialization.
