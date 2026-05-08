import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

try:
    client.delete_collection("multimodal_rag")
except:
    pass

collection = client.create_collection(
    name="multimodal_rag"
)