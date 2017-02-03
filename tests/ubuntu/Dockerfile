FROM ubuntu:14.04

RUN apt-get update

RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y wget
RUN apt-get install -y git

RUN wget https://bootstrap.pypa.io/get-pip.py -P /tmp
RUN python /tmp/get-pip.py

RUN echo user1 | sudo -S pip install git+git://github.com/eyalev/lk.git#egg=lk

ADD setup.sh .
RUN bash setup.sh

USER user1

WORKDIR /home/user1
