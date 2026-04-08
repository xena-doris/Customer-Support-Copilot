# Customer-Support-Copilot
 A customer-support copilot that answers user queries using evidence from a provided knowledge base (documents).


Steps to perform do all these from the root directory
1) python src/retrieval/build_index.py # create the index.faiss file
2) python -m test_retriever # test the retriever
3) python -m test_reranker # test the reranker
4) python -m test_agent # test the agent