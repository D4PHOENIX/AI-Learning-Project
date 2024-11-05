class ChatManager:
    def __init__(self):
        self.history = []

    def add_message(self, user_input: str, bot_response: str):
        self.history.append((user_input, bot_response))

    def get_context(self) -> str:
        # Simply returns the formatted chat history
        return " ".join([f"User: {msg[0]}, Bot: {msg[1]}" for msg in self.history])

    def clear_history(self):
        self.history = []  # Method to clear chat history
