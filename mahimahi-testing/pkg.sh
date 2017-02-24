#!/bin/sh
sudo add-apt-repository ppa:keithw/mahimahi
sudo apt-get update
sudo apt-get install mahimahi -y
sudo apt-get update
sudo apt-get install protobuf-compiler -y
sudo apt-get install libprotobuf-dev -y
sudo apt-get install autotools-dev -y
sudo apt-get install dh-autoreconf -y
sudo apt-get install iptables -y
sudo apt-get install pkg-config -y
sudo apt-get install dnsmasq-base -y
sudo apt-get install apache2-bin -y
sudo apt-get install debhelper -y
sudo apt-get install libssl-dev -y
sudo apt-get install ssl-cert -y
sudo apt-get install libxcb-present-dev -y
sudo apt-get install libcairo2-dev -y
sudo apt-get install libpango1.0-dev -y
sudo apt-get install chromium-browser -y
sudo apt-get install xvfb -y
sudo apt-get install python3-pip -y
sudo pip3 install selenium
sudo sysctl net.ipv4.ip_forward=1
sudo apt-get install default-jre -y
sudo apt-get install default-jdk -y
sudo pip3 install pyvirtualdisplay
sudo apt-get install xterm -y
