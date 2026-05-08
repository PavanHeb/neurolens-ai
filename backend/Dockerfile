FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn python-multipart chromadb sentence-transformers==2.6.1 transformers==4.38.2 pymupdf networkx spacy easyocr pillow python-dotenv numpy<2 torch torchvision torchaudio

RUN python -m spacy download en_core_web_sm

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]