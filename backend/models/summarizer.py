from transformers import T5Tokenizer, T5ForConditionalGeneration

class Summarizer:
    def __init__(self, model_name='t5-small'):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text: str) -> str:
        # Prepare the text for T5 model
        input_ids = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)

        # Generate the summary
        summary_ids = self.model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode the generated summary
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
