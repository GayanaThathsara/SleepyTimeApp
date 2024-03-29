FROM python:3.9.15-slim

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /app/

CMD bash start.sh
