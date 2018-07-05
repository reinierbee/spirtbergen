#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home


sleep 60

cd /
cd home/pi/pihue/spitsbergen 
python spitsbergen.py
cd /

