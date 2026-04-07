import json
import numpy as np
import faiss
import os
from embedder import Embedder


def load_kb(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_faiss_index(embeddings, save_path):
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs(save_path, exist_ok=True)
    faiss.write_index(index, f"{save_path}/index.faiss")


def main():
    kb = load_kb("data/processed/kb_passages.json")

    texts = [item["text"] for item in kb]

    embedder = Embedder()
    embeddings = embedder.encode(texts)

    embeddings = np.array(embeddings).astype("float32")

    # Save embeddings
    np.save("data/processed/embeddings.npy", embeddings)

    # Build FAISS index
    build_faiss_index(embeddings, "models/faiss_index")

    print("✅ FAISS index built!")


if __name__ == "__main__":
    main()