# Arcticography (Spitsbergen)

Of inhabitants, guides, and passengers from Spitsbergen The Northernmost inhabited area of the world See the transformation of the landscape before it disappears Feel how tangible climate change is

Project by: Tim van der Meer and Laurie Hermans
Website: http://kaartdragers.com/
Lights: Reinier Boon

This repo has all instructions to operate and program the lights during the exposition. 

## Resources

- Philips Hue bridge
- Philips Hue White and Color lamps (5x)
- Raspberry pi or something that can run Python code over the network

## Timing

Lights will start to dimm to night time from 13:00 to 18:00.

Fallback mechanism, system will boot with day light enabled and will poll to check for either northernlights or night time mode. If the system was rebooted during the transistion it will not continue to dimm but reset it to day light.

Between 18:00 - 18:30 northernlight simulation is showns.


## Installation

### Using distutils

```
sudo easy_install phue
```
or
```
pip install phue
```

### Run

python spitsbergen.py

### Updating the code

Open terminal 
```
ctrl+alt+t
```

Connect with ssh to raspberry pi device and enter the password
```
ssh pi@192.168.2.5
```

Go to directory
```
cd ~/pihue/spitsbergen
```

Update code by pulling it from github
```
git pull
```

reboot machine
```
reboot -i
```
