# Use the official Raspbian image as the base image
FROM arm32v7/raspbian

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-dev python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install required Python packages
RUN pip3 install pymysql python-telegram-bot secrets

# Set the working directory
WORKDIR /app

# Copy the bot.py file into the container's filesystem
COPY bot.py /app/

# Expose any required ports (if your bot uses a specific port)
# EXPOSE 8080

# Start the bot.py script when the container starts
CMD ["python3", "bot.py"]
