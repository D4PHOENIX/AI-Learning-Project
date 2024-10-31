# test.py
from backend.models.chat_manager import ChatManager

# Create an instance of ChatManager
chat_manager = ChatManager()

# Simulate adding messages
chat_manager.add_message("Hello!", "Hi there!")
chat_manager.add_message("How are you?", "I'm just a bot, but I'm doing great!")

# Get the context
context = chat_manager.get_context()
print(context)
