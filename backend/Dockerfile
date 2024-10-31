# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files from the current directory to the working directory in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH to the working directory
ENV PYTHONPATH=/app

# Expose port for the FastAPI app
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
