FROM python:3.11.3

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/Spark

COPY ./requirements.txt /usr/src/Spark/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/Spark/