FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install Django==3.2.6
RUN pip install psycopg2
ADD . /code/