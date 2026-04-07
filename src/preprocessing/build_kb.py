from load_data import load_json
from chunking import chunk_text
from tqdm import tqdm
import json
import os


def build_kb(doc_path, output_path):
    data = load_json(doc_path)

    kb = []

    for domain in data["doc_data"]:
        for doc_id, doc in data["doc_data"][domain].items():

            for span_id, span in doc["spans"].items():

                text = span["text_sp"]
                section = span.get("title", "")

                chunks = chunk_text(text)

                for i, chunk in enumerate(chunks):
                    kb.append({
                        "doc_id": doc_id,
                        "span_id": f"{span_id}_{i}",
                        "text": chunk,
                        "section": section
                    })

    print(f"Total passages: {len(kb)}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(kb, f, indent=2)


if __name__ == "__main__":
    build_kb(
        doc_path="data/raw/multidoc2dial/multidoc2dial_doc.json",
        output_path="data/processed/kb_passages.json"
    )