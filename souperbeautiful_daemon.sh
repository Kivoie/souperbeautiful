#!/bin/bash

sleep 10
$(date +"[%Y%m%d-%H:%M:%S] crons/boot/: started souperbeautiful" >> /home/ubuntu/Documents/my_debugs.log)
/bin/python3 /home/ubuntu/Documents/souperbeautiful/main.py

