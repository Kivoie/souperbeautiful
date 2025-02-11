#!/bin/bash

while :
do

	reachability=$(fping -t2000 8.8.8.8 -r 0)
	if [ -n "$(echo $reachability | grep 'is alive')" ]
	then
		break
	fi
	sleep 5

done

$(date +"[%Y%m%d-%H:%M:%S] crons/boot/: started souperbeautiful" >> /home/ubuntu/Documents/my_debugs.log)
/bin/python3 /home/ubuntu/Documents/souperbeautiful/main.py

