from sentence_transformers import CrossEncoder

class CrossEncoderModel:
    def __init__(self, model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def predict(self, pairs):
        return self.model.predict(pairs)