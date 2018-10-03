FROM python:3.7
ENV PYTHONBUFFERED=0
WORKDIR /app
COPY ./backend /app

run pip install -r requirements.txt
