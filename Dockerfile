FROM python:3.9.10-buster

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 8000
