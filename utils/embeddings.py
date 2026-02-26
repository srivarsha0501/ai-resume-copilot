# utils/embeddings.py

from sentence_transformers import SentenceTransformer

# load once globally (important)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text_list(text_list):
    vectors = model.encode(text_list)
    return vectors