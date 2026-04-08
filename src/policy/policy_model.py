from .prompts import SYSTEM_PROMPT
from .decision_utils import safe_parse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class ToolPolicyModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

    def decide(self, query):
        prompt = f"""
        {SYSTEM_PROMPT}

        User Query: {query}
        Output JSON:
        """

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = self.model.generate(**inputs, max_new_tokens=200)

        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return safe_parse(text)
