# **WiseUp AI Project Documentation**

WiseUp AI is a comprehensive AI application designed to assist users with various NLP tasks, including a chatbot, quiz generator, and text summarizer. This project leverages a Large Language Model to provide contextual responses, interactive quiz generation, and efficient text summarization.

**Live Application**: [WiseUp AI on Hugging Face Spaces](https://d4phoenix-wiseup.hf.space)

---

## **Table of Contents**

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Docker Setup](#docker-setup)
  - [Local Environment (Non-Docker)](#local-environment-non-docker)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Chatbot](#chatbot)
  - [Quiz Generator](#quiz-generator)
  - [Summarizer](#summarizer)
- [Deployment](#deployment)
  - [Docker Deployment](#docker-deployment)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
---

## **Project Overview**

WiseUp AI provides an intuitive interface for interacting with NLP capabilities, including conversation-based assistance, quiz generation, and text summarization. The backend is powered by FastAPI, and the frontend is built with Gradio, all containerized using Docker for seamless deployment.

---

## **Features**

1. **Chatbot**: Interactive AI-powered chatbot with conversation history.
2. **Quiz Generator**: Automatically generates quizzes from input text.
3. **Summarizer**: Generates concise summaries of provided text.

---

## **Getting Started**

### **Docker Setup**
Ensure Docker is installed and running on your machine. We will use Docker Compose to build and start both the frontend and backend.

    docker-compose up --build
    
### **Local Environment (Non-Docker)**
If you prefer to run the application without Docker:

1. **Set up a virtual environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    
2. **Install Dependencies**:

    ```bash
    pip install -r backend/requirements.txt

### **Environment Variables**
  Define environment variables to configure the application. Create a .env file in the project’s root directory with the following:

    BACKEND_URL=<Backend URL>  # Example: http://localhost:8000
    FRONTEND_URL=<Frontend URL> # Example: http://localhost:7860

---

## **Usage**

Once the application is running, navigate to http://localhost:7860 for local deployment or visit the live app on Hugging Face Spaces.

### 1.**Chatbot**:

The Chatbot interface allows users to interact with an AI-powered chatbot that maintains conversation history for a natural conversational flow.

**Fields:**
* Subject: Enter the conversation subject.
* Topic: Specify the topic to narrow down the discussion.
* Your Question: Type your question here.

**Buttons:**
* Ask Chatbot: Sends the question to the chatbot.
* Clear Chat History: Resets the chat history.

### 2.**Quiz Generator**:

The Quiz Generator creates multiple-choice questions based on the provided text.

**Fields:**
* Subject: Specify a broad topic for the quiz.
* Topic: Narrow down the quiz topic.
* Text for Quiz Generation: Provide text for generating questions.
* Max Questions: Choose the maximum number of questions.

**Button:**
* Generate Quiz: Generates quiz questions based on the input text.

### 3.**Summarizer**:

The Summarizer creates concise summaries based on input text.

**Fields:**
* Text to Summarize: Input the text to summarize.
* Max Summary Length: Set the maximum length for the summary.
* Min Summary Length: Set the minimum length for the summary.

**Button:**
* Summarize: Generates a summary of the provided text.

---

## **Deployment**
The application is hosted on Hugging Face Spaces and can be accessed at [WiseUp AI on Hugging Face Spaces](https://d4phoenix-wiseup.hf.space).

### **Docker Deployment**
To deploy on your own server or local setup:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/D4PHOENIX/wiseup-ai
    cd wiseup-ai
2. **Run Docker Compose**:
    ```bash
    docker-compose up --build

---

## **API Endpoints**
Here’s a quick reference to the main API endpoints:
- /chat (POST): Accepts a user message and returns the chatbot's response.
- /chat/history (GET): Retrieves the chat history.
- /chat/clear (POST): Clears the chat history.
- /summarize (POST): Summarizes the given text based on length parameters.
- /quiz (POST): Generates quiz questions from input text.
For API documentation, visit http://localhost:8000/docs when the backend is running.

---

## **Screenshots**
(Include screenshots or a GIF of the application in action here)

---

## **License**
This project is licensed under the MIT License.
