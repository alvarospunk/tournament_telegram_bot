# Use the official Alma Linux image as the base image
FROM python:latest

# Install necessary dependencies
# RUN yum install -y python3.11 python3.11-devel python3.11-pip openssl openssl-devel && \
#     yum clean all && \
#     rm -rf /var/cache/yum

# Upgrade pip
RUN python3.12 -m pip install --upgrade pip

# Install required Python packages
RUN pip3 install pymysql pyopenssl python-telegram-bot

# Set the working directory
WORKDIR /app

# Copy the bot.py file into the container's filesystem
COPY bot.py /app/

# Expose any required ports (if your bot uses a specific port)
EXPOSE 443

# Start the bot.py script when the container starts
CMD ["python3.12", "bot.py"]
