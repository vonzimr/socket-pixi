from node
ENV PYTHONBUFFERED=0
WORKDIR APP

COPY ./frontend /app

RUN NODE_ENV=dev npm install
