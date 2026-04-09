from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .prompt_builder import build_prompt


class GeneratorModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

    def generate(self, query, passages):
        if not passages:
            return "I am not sure based on the available information."

        # 🔥 limit noise (VERY IMPORTANT)
        passages = passages[:3]

        prompt = build_prompt(query, passages)

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            top_p=0.9
        )

        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # 🔥 Improve readability
        if len(answer.split()) < 6:
            answer = f"Based on the available information, {answer}."

        # Capitalize properly
        answer = answer.strip().capitalize()

        return answer