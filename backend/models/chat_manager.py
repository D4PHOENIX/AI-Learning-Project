import logging
from typing import List
from backend.models.summarizer import Summarizer  
from backend.utils.relevance import check_relevance  

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChatManager:
    def __init__(self, max_context_length=5, length_limit=500, relevance_threshold=0.5):
        self.history = []
        self.max_context_length = max_context_length
        self.length_limit = length_limit  # Configure length limit
        self.relevance_threshold = relevance_threshold  # Configure relevance threshold
        self.summarizer = Summarizer()  # Ensure this class exists and is imported correctly

    def add_message(self, user_input: str, bot_response: str):
        self.history.append((user_input, bot_response))
        if len(self.history) > self.max_context_length:
            self.history.pop(0)

    def get_context(self) -> str:
        # Create a context string based on the current history
        context = " ".join([f"User: {msg[0]}, Bot: {msg[1]}" for msg in self.history])
        
        # Filter messages based on relevance
        relevant_messages = [msg for msg in self.history if check_relevance(msg[0], context, self.relevance_threshold)]
        
        # Format the relevant messages for final context
        context = " ".join([f"User: {msg[0]}, Bot: {msg[1]}" for msg in relevant_messages])
        
        # Summarize if the context exceeds the length limit
        if len(context) > self.length_limit:
            try:
                logging.info("Context length exceeded, summarizing...")
                context = self.summarizer.summarize(context)
            except Exception as e:
                logging.error(f"Error during summarization: {e}")
                # Return the original context if summarization fails
                return context

        logging.info("Context successfully created and returned.")
        return context
