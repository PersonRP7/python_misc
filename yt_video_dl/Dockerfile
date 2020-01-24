FROM python:3.9.0a2-alpine3.10
WORKDIR /application
COPY ./python .
RUN pip install --upgrade pip
RUN pip install youtube-dl
RUN pip install pafy