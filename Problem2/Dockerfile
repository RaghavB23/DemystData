# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if necessary, for example if using Spark UI)
EXPOSE 4040

# Define the command to run the script
CMD ["python", "-m", "problem2"]

