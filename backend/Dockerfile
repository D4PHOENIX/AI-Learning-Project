# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Create a cache directory for Hugging Face
RUN mkdir -p /app/.cache/huggingface/hub && \
    chmod -R 777 /app/.cache

# Set the environment variable for cache directory
ENV HF_HOME=/app/.cache/huggingface

# Copy all files from the current directory to the working directory in the container
COPY ./ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH to the working directory
ENV PYTHONPATH=/app

# Expose port 7860 for FastAPI
EXPOSE 7860

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
