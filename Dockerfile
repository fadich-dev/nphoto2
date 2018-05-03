FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/django
WORKDIR /opt/django
ADD . /opt/django/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
