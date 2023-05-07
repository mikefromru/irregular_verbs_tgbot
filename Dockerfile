from python:slim

RUN mkdir app
RUN cd app

WORKDIR /app

ADD . /app

RUN pip3 install -r req.txt

CMD python main.py
