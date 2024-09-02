# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install watchdog


# Make port 8080 available to the world outside this container (optional if needed for a web app)
EXPOSE 8080

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the application
# CMD ["watchmedo", "auto-restart", "--pattern=*.py", "--recursive", "--", "python", "main.py"]
