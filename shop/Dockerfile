FROM python:3.9

ENV PYTHONBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD=Tr0ub4dor@3

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .