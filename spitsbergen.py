#!/usr/bin/python

from phue import Bridge
import random
import threading


#Connection
b = Bridge('ip_of_your_bridge')
b.connect()

#Light group settings

#Lights

#Timing

#northernlights


def northernlightsFlow(x, y, bightness, flowTime):
    l1Time = randrange(0,flowTime)
    remainder = flowTime - l1Time
    l2Time = randrange(0,remainder)
    remainder =  remainder- l2Time
    l3Time = randrange(0,remainder)
    remainder = remainder - l3Time
    l4Time = randrange(0,remainder)
    remainder = remaider - l4Time
    l5Time = remainder

    l1 =  {'transitiontime' : l1Time, 'on' : True, 'bri' : brightness, 'xy' : [x,y] }
    l2 =  {'transitiontime' : l2Time, 'on' : True, 'bri' : brightness, 'xy' : [x,y] }
    l3 =  {'transitiontime' : l3Time, 'on' : True, 'bri' : brightness, 'xy' : [x,y] }
    l4 =  {'transitiontime' : l4Time, 'on' : True, 'bri' : brightness, 'xy' : [x,y] }
    l5 =  {'transitiontime' : l5Time, 'on' : True, 'bri' : brightness, 'xy' : [x,y] }

    b.set_light(1, l1)
    b.set_light(2, l2)
    b.set_light(3, l3)
    b.set_light(4, l4)
    b.set_light(5, l5)







def northernlightsRoutine():

    xlight = uniform(0.15, 0.23)
    ylight = uniform(0.75, 0.51)
    bightness = randrange(30,100)
    flowTime = randrange(30,70)
    dimmedTime = choice([0,0,0,0,0,0,0,10,10,20,30,100])
    totalTime = flowTime + dimmedTime

    northerlightsFlow(xlight,ylight,birghtness,flowTime)
    threading.Timer((totalTime/10), northernlightsRoutine).start()
