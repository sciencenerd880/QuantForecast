# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory (including the src folder)
COPY . .

# Change working directory to src where app.py is located
WORKDIR /app/src

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]