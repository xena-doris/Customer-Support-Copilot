from retrieval.retriever import Retriever
from reranking.reranker import Reranker

retriever = Retriever()
reranker = Reranker()

query = "How do I apply for benefits?"

# Step 1: Retrieve
candidates = retriever.search(query, top_k=10)

# Step 2: Rerank
final_results = reranker.rerank(query, candidates, top_k=3)

for i, r in enumerate(final_results):
    print(f"\nFinal Result {i+1}")
    print(r["text"])