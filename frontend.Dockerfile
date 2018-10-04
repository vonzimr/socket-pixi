from node
ENV PYTHONBUFFERED=0
WORKDIR app 

COPY ./frontend /app

RUN NODE_ENV=dev npm install
