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

Lights will start to enable at 13:00 and slowly build up to full daylight at 17:30 lights start to dimm back to night time.
Fallback mechanism, between 13:30 and 17:30 the code will know its daylight and recovers to that state in case of emergency.
Between 18:30 - night time is enabled and the code will reset state to night time.

18:00 - 18:30 northernlight simulation is showns.


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
