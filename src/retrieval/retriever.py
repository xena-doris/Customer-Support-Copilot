import faiss
import numpy as np
import json
from embedder import Embedder


class Retriever:
    def __init__(self):
        self.embedder = Embedder()

        self.index = faiss.read_index("models/faiss_index/index.faiss")

        with open("data/processed/kb_passages.json", "r", encoding="utf-8") as f:
            self.kb = json.load(f)

    def search(self, query, top_k=5):
        query_vec = self.embedder.encode([query])
        query_vec = np.array(query_vec).astype("float32")

        distances, indices = self.index.search(query_vec, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.kb[idx])

        return results