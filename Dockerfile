FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
RUN mkdir /code/django-media
RUN mkdir /code/mediamanagementproject
COPY django-media /code/django-media/
COPY mediamanagementproject /code/mediamanagementproject/
RUN pip install -r /code/mediamanagementproject/requirements.txt
WORKDIR /code/django-media
RUN python3 run.py
WORKDIR /code/mediamanagementproject

