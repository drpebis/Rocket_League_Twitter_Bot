# lightweight Alpine linux based Docker image
FROM python:3.7-alpine

# Set working directory
WORKDIR /srv

# Copy important files into container
COPY requirements.txt .
COPY my_twitter_bot.py .
COPY last_seen_id.txt .

# Install libraries
RUN pip install -r requirements.txt

# Run the script
CMD ["python3", "rl_helper_bot.py"]