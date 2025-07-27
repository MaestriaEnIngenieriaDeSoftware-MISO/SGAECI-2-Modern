FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock ./

# Install the dependencies globally
RUN pipenv install --system --deploy

# Copy the rest of the application code into the container
COPY . .

# Copy the .env.development file into the container
COPY .env.development .env

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the application
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3000"]
