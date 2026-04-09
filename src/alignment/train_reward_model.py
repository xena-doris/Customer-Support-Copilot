import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle


def load_data():
    with open("data/preference_data.json") as f:
        data = json.load(f)

    texts = []
    labels = []

    for item in data:
        texts.append(item["good"])
        labels.append(1)

        texts.append(item["bad"])
        labels.append(0)

    return texts, labels


def train():
    texts, labels = load_data()

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    with open("models/reward_model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)

    print("Reward model trained!")


if __name__ == "__main__":
    train()