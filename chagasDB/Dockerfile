# Dockerfile aims at packaging the ChagasDB Django application
# Get a Linux Python 3.9 image
FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

# Prepare directory to host ChagasDB code
RUN mkdir /code
WORKDIR /code

# Install depedencies
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Copy ChagasDB code into the image
ADD . /code/
