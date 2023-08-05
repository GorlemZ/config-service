FROM python:3.8-slim

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /src/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /src/