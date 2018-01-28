FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code /code/python /code/python/marketo_api
WORKDIR /code/python/marketo_api/
ADD requirements.txt /code/python/marketo_api/
RUN pip install -r requirements.txt