# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variable for the port
ENV PORT 8080

# Expose the port FastAPI will run on
EXPOSE 8080

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]