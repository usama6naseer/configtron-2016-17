#!/bin/bash
sudo sysctl -w net.ipv4.tcp_congestion_control=$1
