# Pull base image
FROM python:3.10.4-slim-bullseye

#Set Environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set work directory 
WORKDIR /bookstore

#Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copy Project
COPY . .


