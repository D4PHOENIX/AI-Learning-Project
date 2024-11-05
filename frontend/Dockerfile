# Frontend Dockerfile
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the frontend code
COPY . .

# Expose port 7860 (Gradio's default port)
EXPOSE 7860

# Run the Gradio app
CMD ["python", "app.py"]
