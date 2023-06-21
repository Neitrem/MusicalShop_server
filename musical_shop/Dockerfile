FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /back_django
WORKDIR /back_django
COPY requirements.txt /back_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /back_django/