from fastapi import APIRouter, UploadFile, File
import shutil
import os
import uuid

from app.services.pdf_service import extract_pdf_text
from app.services.image_service import extract_image_text
from app.services.audio_service import extract_audio_text
from app.services.embeddings import generate_embedding
from app.services.graph_service import build_graph
from app.database.chroma import collection

router = APIRouter()

UPLOAD_FOLDER = "uploads"

def clear_collection():

    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):

    clear_collection()

    file_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_pdf_text(file_path)

    if len(text) > 4000:
        text = text[:4000]

    embedding = generate_embedding(text)

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[file_id]
    )

    graph_edges = build_graph(text)

    return {
        "status": "PDF uploaded successfully",
        "graph": graph_edges
    }

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):

    clear_collection()

    file_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_image_text(file_path)

    if len(text) > 4000:
        text = text[:4000]

    embedding = generate_embedding(text)

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[file_id]
    )

    graph_edges = build_graph(text)

    return {
        "status": "Image uploaded successfully",
        "graph": graph_edges
    }

@router.post("/audio")
async def upload_audio(file: UploadFile = File(...)):

    clear_collection()

    file_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_audio_text(file_path)

    embedding = generate_embedding(text)

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[file_id]
    )

    return {
        "status": "Audio uploaded successfully"
    }