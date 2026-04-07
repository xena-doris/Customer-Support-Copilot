from retriever import Retriever

retriever = Retriever()

query = "How do I apply for benefits?"

results = retriever.search(query, top_k=10)

for i, r in enumerate(results):
    print(f"\nResult {i+1}")
    print(r["text"])
    print(r["section"])