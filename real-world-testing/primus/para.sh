#!/bin/bash
echo "changing parameters"
echo $1
echo $2
sudo tc qdisc change dev eth0 root netem delay $1ms loss $2%
