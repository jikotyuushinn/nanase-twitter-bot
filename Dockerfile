FROM python:3.8.7

RUN mkdir /app
WORKDIR /app

ADD . .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
