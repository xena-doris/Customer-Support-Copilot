from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .prompt_builder import build_prompt
from src.alignment.reward_model import RewardModel


class GeneratorModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
        self.reward_model = RewardModel()

    def generate(self, query, passages):
        if not passages:
            return "I am not sure based on the available information."

        # 🔥 limit noise
        passages = passages[:3]

        prompt = build_prompt(query, passages)

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)

        candidates = []

        # 🔥 Generate multiple answers (key for alignment)
        for _ in range(3):
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )

            answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # 🔧 Clean answer
            answer = answer.strip()

            if len(answer.split()) < 5:
                answer = f"Based on the available information, {answer}."

            answer = answer.capitalize()

            candidates.append(answer)

        # 🔥 Score using reward model
        scored_candidates = []

        for ans in candidates:
            score = self.reward_model.score(ans)
            scored_candidates.append((ans, score))

        # 🔥 Select best answer
        best_answer = sorted(scored_candidates, key=lambda x: x[1], reverse=True)[0][0]

        return best_answer