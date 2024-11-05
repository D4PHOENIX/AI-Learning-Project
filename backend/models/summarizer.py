from transformers import pipeline

class Summarizer:
    def __init__(self, model_name='t5-small'):
        # Initialize the summarization pipeline
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text: str, max_length: int = 150, min_length: int = 40) -> str:
        # Use the pipeline to generate the summary
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
        
        # Extract the summary text from the output
        return summary[0]['summary_text']
