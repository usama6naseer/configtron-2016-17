#!/bin/bash
for FILE1 in "$@"
do
   echo $FILE1
   sudo ip route change default via 152.3.144.61 dev eth0  proto static initcwnd $FILE1
   sudo ip route change 152.3.144.0/23 dev eth0  proto kernel  scope link  src 152.3.144.154  metric 1 initcwnd $FILE1
done

