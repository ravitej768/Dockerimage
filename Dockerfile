# Use an official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy your Flask app into the container
COPY app.py .

# Install Flask in the container
RUN pip install flask

# Expose port 5000 for the app
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
