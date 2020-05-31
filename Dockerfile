FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /django_api

WORKDIR /django_api

COPY . /django_api/

RUN pip install -r requirements.txt