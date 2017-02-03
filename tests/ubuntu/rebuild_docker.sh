#!/usr/bin/env bash

docker rm -f lk
docker build -t lk .
docker run -it -d --name=lk lk bash
