# utils/vector_store.py
import os
import faiss
import numpy as np

def create_faiss_index(vectors):
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(vectors).astype("float32"))

    return index


def save_index(index, path="vector_db/resume.index"):
    
    folder = os.path.dirname(path)

    if folder and not os.path.exists(folder):os.makedirs(folder,exist_ok=True)
    faiss.write_index(index, path)
    
def load_index(path="vector_db/resume.index"):
    return faiss.read_index(path)

def search_index(index, query_vector, top_k=3):
    distances, indices = index.search(query_vector.astype("float32"), top_k)

    return indices[0]

