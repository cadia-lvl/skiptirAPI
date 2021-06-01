FROM pypy:3.7

RUN apt-get update \
 && apt-get install git

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app/

RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

WORKDIR /usr/src/app
RUN git clone https://github.com/krunars/skiptir.git

WORKDIR /usr/src/app
COPY main.py main.py

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0
