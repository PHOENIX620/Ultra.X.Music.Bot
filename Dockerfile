# Use the latest Debian image
FROM debian:latest

# Update and install necessary dependencies in one layer
RUN apt update && apt upgrade -y && \
    apt install -y git curl python3-pip ffmpeg python3-full && \
    curl -sL https://deb.nodesource.com/setup_17.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Set up the application directory
RUN mkdir /app/
WORKDIR /app/

# Copy the current directory contents into the container
COPY . /app/

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["python3", "main.py"]
