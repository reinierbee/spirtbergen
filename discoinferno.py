#!/usr/bin/python

from phue import Bridge
import random
import threading

b = Bridge('192.168.0.100')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

lights = b.get_light_objects()

def disco():
  threading.Timer(1.0, disco).start()
  for light in lights:
	light.brightness = 254
	light.xy = [random.random(),random.random()]

disco()

