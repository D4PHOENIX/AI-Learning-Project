# **WiseUp AI Project**

WiseUp AI is an interactive AI-powered application designed to assist users through various NLP tasks, including chat-based assistance, quiz generation, and text summarization. This project leverages an LLM (Gemini model) to provide meaningful responses, personalized interactions, and efficient processing of user inputs.

**Live Application**: The application is hosted on [Hugging Face Spaces](https://d4phoenix-wiseup.hf.space) and can be accessed here: [WiseUp AI on Hugging Face](https://d4phoenix-wiseup.hf.space).

## **Table of Contents**

- [Project Overview](#project-overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Chatbot](#chatbot)
  - [Quiz Generator](#quiz-generator)
  - [Summarizer](#summarizer)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## **Project Overview**

WiseUp AI is built with a FastAPI backend and a Gradio-based frontend interface, containerized using Docker for easy setup and deployment. The application is hosted on [Hugging Face Spaces](https://d4phoenix-wiseup.hf.space), providing live access to the interactive AI functionalities.

## **Features**

1. **Chatbot**: An intelligent chatbot that maintains conversation history, enabling contextual interactions.
2. **Quiz Generator**: Generates quizzes based on input text with configurable question limits.
3. **Summarizer**: Provides concise summaries of long text inputs with customizable length parameters.

## **System Architecture**

The system comprises a backend built with FastAPI and a frontend interface created using Gradio. Docker is used to streamline development and production environments.

*(Optional: Add a diagram if needed)*

---

## **Getting Started**

### **Prerequisites**

- **Docker**: Ensure Docker is installed on your system to run the application in containers.
- **Git**: For cloning the repository.
- **Python 3.10+**: Required if you are not using Docker for running the backend.

### **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/wiseup-ai
   cd wiseup-ai
