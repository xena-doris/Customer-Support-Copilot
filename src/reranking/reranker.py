from .cross_encoder import CrossEncoderModel

class Reranker:
    def __init__(self):
        self.model = CrossEncoderModel()

    def rerank(self, query, passages, top_k=5):
        pairs = [(query, p["text"]) for p in passages]

        scores = self.model.predict(pairs)

        ranked = list(zip(passages, scores))
        ranked = sorted(ranked, key=lambda x: x[1], reverse=True)

        return [item[0] for item in ranked[:top_k]]