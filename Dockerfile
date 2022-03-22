# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Debian Env
ENV DEBIAN_FRONTEND=noninteractive

# Create app dir and give exec rights
RUN mkdir /app && chmod 777 /app

# Set app Workdir
WORKDIR /app

# Install Python 3 and pip
RUN apt -qq update && apt -qq install -y git python3 python3-pip
COPY . .

# Install pip requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["bash","start.sh"]
