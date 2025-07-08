# Use the official Python image from Docker Hub
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Tell Docker how to run the app
CMD ["python", "app.py"]
