#!/usr/bin/env bash

adduser --disabled-password --gecos "" user1
echo "user1:user1_pass" | chpasswd
adduser user1 sudo

su - user1

su user1 -c 'lk add-bash-completion'

source ~/.bashrc
