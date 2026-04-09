import pickle


class RewardModel:
    def __init__(self):
        with open("models/reward_model.pkl", "rb") as f:
            self.vectorizer, self.model = pickle.load(f)

    def score(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict_proba(X)[0][1]