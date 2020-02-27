FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN apk update && apk add python3-dev
RUN pip install requests pycodestyle snapshottest coverage pytest pytest-cov
RUN cd des_process && pytest --cov
