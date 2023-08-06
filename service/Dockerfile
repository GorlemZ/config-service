FROM python:3.8-slim

WORKDIR /

COPY ./requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get clean

RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .