import json


def create_preference_data():
    data = [
        {
            "query": "What is eligibility for benefits?",
            "good": "Based on [doc_id:1, span:2], eligibility depends on age and benefit type.",
            "bad": "You can get benefits if you apply."
        },
        {
            "query": "How do I apply?",
            "good": "According to [doc_id:3, span:1], you must submit an application form.",
            "bad": "Just apply online."
        }
    ]

    with open("data/preference_data.json", "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    create_preference_data()