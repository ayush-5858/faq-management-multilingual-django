# Use official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1  # Ensures Python output is sent straight to the terminal (without buffering)
ENV PYTHONPATH=/app  # Sets the working directory for Python

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . /app/

# Expose port 8000 (default Django port)
EXPOSE 8000

# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
