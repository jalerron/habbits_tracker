FROM python:3.11-alpine

WORKDIR /habits_tracker

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
