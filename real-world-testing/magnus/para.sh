#!/bin/bash
echo "adding parameters" 
echo $1 
echo $2 
echo $3
sudo tc qdisc add dev eth0 root handle 1: htb default 1
sudo tc class add dev eth0 parent 1: classid 0:1 htb rate $3kbit
sudo tc qdisc add dev eth0 parent 1:1 handle 10: netem delay $1ms loss $2%
