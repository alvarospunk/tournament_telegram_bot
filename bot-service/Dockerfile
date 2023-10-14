# Use the official Alma Linux image as the base image
FROM almalinux:9.2

# Install necessary dependencies
RUN yum install -y python311 python311-devel python311-pip && \
    yum clean all && \
    rm -rf /var/cache/yum

# Upgrade pip
RUN python3.9 -m pip install --upgrade pip

# Install required Python packages
RUN pip3 install pymysql python-telegram-bot secrets

# Set the working directory
WORKDIR /app

# Copy the bot.py file into the container's filesystem
COPY bot.py /app/

# Expose any required ports (if your bot uses a specific port)
# EXPOSE 8080

# Start the bot.py script when the container starts
CMD ["python3.11", "bot.py"]
