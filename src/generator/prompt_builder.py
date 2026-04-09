def build_prompt(query, passages):
    evidence_text = ""

    for p in passages:
        evidence_text += f"[doc_id: {p['doc_id']}, span: {p['span_id']}]\n"
        evidence_text += f"{p['text']}\n\n"

    prompt = f"""
        You are a helpful and friendly customer support assistant.

        Answer the user's question in a clear, complete, and natural way.

        User Question:
        {query}

        Evidence:
        {evidence_text}

        Instructions:
        - Use the evidence to form a complete sentence
        - Explain the answer clearly (not just a phrase)
        - Include citations like [doc_id, span_id]
        - If unsure, say: I am not sure

        Answer:
        """

    return prompt