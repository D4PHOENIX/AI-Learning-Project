import gradio as gr
import requests
import os

# Backend URL
BACKEND_URL = os.getenv("BACKEND_URL")

# Function to prepare the context for the chatbot
def initial_context_gathering(subject, topic, user_prompt):
    # Combine subject, topic, and user prompt to create a context for the chatbot
    context = f"Subject: {subject}\nTopic: {topic}\nUser Input: {user_prompt}"
    return context, context  # Return the context as both variables if needed

# Chatbot Interface
def chatbot_with_context(subject, topic, user_prompt):
    try:
        # Prepare the full prompt for the chatbot
        context, full_prompt = initial_context_gathering(subject, topic, user_prompt)
        
        # Send the user's message to the backend
        response = requests.post(f"{BACKEND_URL}/chat", json={"message": full_prompt}).json()
        
        if "response" not in response:
            return "Error: No response from the backend.", {}

        # Get the chatbot's response
        bot_response = response["response"]
        
        # Fetch the chat history from the backend
        history_response = requests.get(f"{BACKEND_URL}/chat/history").json()
        
        # Return the response and the chat history
        return history_response.get("history", "No history available."), {}
        
    except Exception as e:
        return f"Error: {str(e)}", {}

def clear_chat_history():
    try:
        # Clear the chat history via the backend
        response = requests.post(f"{BACKEND_URL}/chat/clear").json()
        return response.get("message", "Chat history cleared!"), {}
    except Exception as e:
        return f"Error: {str(e)}", {}

# Summarization Interface
def summarize_text(text, max_length, min_length):
    try:
        response = requests.post(f"{BACKEND_URL}/summarize", json={
            "text": text,
            "max_length": max_length,
            "min_length": min_length
        }).json()
        return response.get("summary", "No summary generated")
    except Exception as e:
        return f"Error: {str(e)}"

# Quiz Interface
def quiz_with_context(subject, topic, text_for_quiz, max_questions):
    try:
        context, full_prompt = initial_context_gathering(subject, topic, text_for_quiz)
        response = requests.post(f"{BACKEND_URL}/quiz", json={"text": full_prompt, "max_questions": max_questions}).json()
        
        return response.get("questions", "Error generating quiz"), {}
    except Exception as e:
        return f"Error: {str(e)}", {}

# Gradio Blocks Interface
with gr.Blocks() as app:
    with gr.Tab("Chatbot"):
        with gr.Row():
            with gr.Column():
                subject_input = gr.Textbox(label="Subject")
                topic_input = gr.Textbox(label="Topic")
                clear_history_button = gr.Button("Clear Chat History")

            with gr.Column(scale=2):
                chatbot_response = gr.Textbox(label="Chatbot Conversation", interactive=True, lines=10, placeholder="Chatbot conversation will appear here...")
                user_input = gr.Textbox(label="Your Question")

            with gr.Column():
                context_output = gr.JSON(label="Stored Context")

        chat_button = gr.Button("Ask Chatbot")
        chat_button.click(chatbot_with_context, inputs=[subject_input, topic_input, user_input], outputs=[chatbot_response, context_output])
        clear_history_button.click(clear_chat_history, outputs=[chatbot_response, context_output])

    with gr.Tab("Quiz Generator"):
        quiz_subject_input = gr.Textbox(label="Subject")
        quiz_topic_input = gr.Textbox(label="Topic")
        text_for_quiz = gr.Textbox(lines=10, label="Text for Quiz Generation")
        max_questions_slider = gr.Slider(minimum=5, maximum=20, value=10, label="Max Questions")
        quiz_output = gr.JSON(label="Generated Quiz")
        quiz_context_output = gr.JSON(label="Stored Context")

        quiz_button = gr.Button("Generate Quiz")
        quiz_button.click(quiz_with_context, inputs=[quiz_subject_input, quiz_topic_input, text_for_quiz, max_questions_slider], outputs=[quiz_output, quiz_context_output])

    with gr.Tab("Summarizer"):
        text_to_summarize = gr.Textbox(lines=10, label="Text to Summarize")
        max_length_slider = gr.Slider(minimum=50, maximum=300, value=150, label="Max Summary Length")
        min_length_slider = gr.Slider(minimum=20, maximum=100, value=40, label="Min Summary Length")
        summary_output = gr.Textbox(label="Generated Summary")
        summarize_button = gr.Button("Summarize")
        summarize_button.click(summarize_text, inputs=[text_to_summarize, max_length_slider, min_length_slider], outputs=summary_output)

# Launch the app
app.launch(share=True)
