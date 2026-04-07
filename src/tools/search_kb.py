from .base_tool import BaseTool
from src.retrieval.retriever import Retriever
from src.reranking.reranker import Reranker


class SearchKB(BaseTool):
    name = "SearchKB"

    description = "Search knowledge base and return most relevant sections."

    input_schema = {
        "query": "string"
    }

    output_schema = {
        "results": [
            {
                "text": "string",
                "section": "string",
                "doc_id": "string"
            }
        ]
    }

    def __init__(self):
        self.retriever = Retriever()
        self.reranker = Reranker()

    def run(self, input_data):
        query = input_data["query"]

        candidates = self.retriever.search(query, top_k=10)
        reranked = self.reranker.rerank(query, candidates, top_k=3)

        return {
            "results": reranked
        }