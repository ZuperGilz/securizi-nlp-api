from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

class IndoBertNER:
    def __init__(self):
        model_name = "indobenchmark/indobert-base-p1"  # gratis
        self.nlp = pipeline(
            "ner",
            model=AutoModelForTokenClassification.from_pretrained(model_name),
            tokenizer=AutoTokenizer.from_pretrained(model_name),
            aggregation_strategy="simple"
        )

    def extract(self, text: str):
        return self.nlp(text)
