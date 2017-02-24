#!/bin/bash
echo "adding parameters" 
echo $1 
echo $2 
echo $3
sudo sysctl -w net.ipv4.tcp_slow_start_after_idle=$1
sudo sysctl -w net.ipv4.tcp_autocorking=$2
sudo sysctl -w net.ipv4.tcp_low_latency=$3