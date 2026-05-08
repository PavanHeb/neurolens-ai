import fitz
import re

def clean_text(text):

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'References.*', '', text, flags=re.IGNORECASE)

    text = re.sub(r'Bibliography.*', '', text, flags=re.IGNORECASE)

    text = re.sub(r'Copyright.*', '', text, flags=re.IGNORECASE)

    text = re.sub(r'All rights reserved.*', '', text, flags=re.IGNORECASE)

    return text.strip()

def extract_pdf_text(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    text = clean_text(text)

    return text