FROM ubuntu:14.04

RUN apt-get update

RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y wget
RUN apt-get install -y git

RUN wget https://bootstrap.pypa.io/get-pip.py -P /tmp
RUN python /tmp/get-pip.py

ENV REFRESHED_AT 2017-02-08T17:49:00

RUN echo user1 | sudo -S pip install git+git://github.com/eyalev/lk.git@dev#egg=lk

ADD setup.sh .
RUN bash setup.sh

USER user1

WORKDIR /home/user1
