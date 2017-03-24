#!/usr/bin/env bash

# BreezoMeter user

adduser --disabled-password --gecos "" user2
echo "user2:user2_pass" | chpasswd
adduser user2 sudo

su - user2

su user2 -c 'lk add-bash-completion'

source ~/.bashrc


