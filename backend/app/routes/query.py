from fastapi import APIRouter

from app.services.embeddings import generate_embedding
from app.services.llm_service import generate_answer
from app.database.chroma import collection

router = APIRouter()

@router.post("/")
async def query_rag(data: dict):

    query = data["query"]

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    retrieved_docs = results["documents"][0]

    if not retrieved_docs:

        return {
            "answer": "No relevant information found."
        }

    context = retrieved_docs[0]

    short_context = context[:2500]

    answer = generate_answer(
        query,
        short_context
    )

    return {
        "answer": answer
    }