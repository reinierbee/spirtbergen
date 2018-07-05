#!/usr/bin/python

from phue import Bridge
import random
import threading
import time

#Connection
b = Bridge('ip_of_your_bridge')
b.connect()

#Light group settings


#Timing

startOfDayHours = "13"
startOfDayMinutes = "00"
startOfDayTransitionTime = 1800
startOfDayTransitionTimeM = startOfDayTransitionTime/60

endOfDayHours = "17"
endOfDayMinutes = "30"
endOfDayTransitionTime = 1800
endOfDayTransitionTimeM = endOfDayTransitionTime/60

onTime = time(int(float(startOfDayHours))),int(float(startOfDayMinutes)))
offTime = time(int(float(endOfDayHours))) + 1,int(float(endOfDayMinutes)))


#Lights
dayX = 0.4500
dayY = 0.4000

nightX = 0.4500
nightY = 0.4000

startOfDayLight = {'transitiontime' : (startOfDayTransitionTime*10), 'on' : True, 'bri' : 100, 'xy' : [dayX,dayY]}
endOfDayLight = {'transitiontime' : (endOfDayTransitionTime*10), 'on' : True, 'bri' : 100, 'xy' : [nightX,nightY]}

startOfDayTime = "T"+ startOfDayHours +":"+ startOfDayMinutes +":00"
endOfDayTime = "T"+ endOfDayHours +":"+ endOfDayMinutes +":00"


#int(float())



def groupReset():
    b.delete_group(1)
    b.create_group('all', [1,2,3,4,5])
    b.set_group(1, 'on', True, 'bri' : 100,)


#planner
def planner():
    b.delete_schedule(1)
    today = time.strftime("%Y-%m-%d")
    b.create_schedule('Start of day', today + startOfDayLight, 1, startOfDayLight)
    b.create_schedule('End of day', today + endOfDayLight, 1, endOfDayLight)
    #rescedule this every 4 hours to be sure we queue up again on the right time
    threading.Timer(14400, planner).start()


def isnight(time_to_check, on_time, off_time):
    if time_to_check > onTime and time_to_check < offTime:
        return False

    if time_to_check > offTime or time_to_check < onTime:
        return True

    if time_to_check == onTime:
        return False
    return False

def dayTimeRoutine():
    threading.Timer(10.0, dayTimeRoutine).start()

    if isnight(datetime.now().time(), on_time, off_time):
        print("Night Time detected.")
        b.set_light([1,2,3],nightTimeLight)
    else:
        print("Day Time detected.")
        if datetime.now().time() < day_time_nothing
            b.set_light([1,2,3],dayTimeLight)


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
    #l4 =  {'transitiontime' : l4Time, 'on' : True, 'bri' : brightness, 'xy' : [x,y] }
    #l5 =  {'transitiontime' : l5Time, 'on' : True, 'bri' : brightness, 'xy' : [x,y] }

    b.set_light(1, l1)
    b.set_light(2, l2)
    b.set_light(3, l3)
    #b.set_light(4, l4)
    #b.set_light(5, l5)

def northernlightsRoutine():

    xlight = uniform(0.05, 0.20)
    ylight = uniform(0.65, 0.35)
    bightness = randrange(30,100)
    flowTime = randrange(30,70)
    dimmedTime = choice([0,0,0,0,0,0,0,10,10,20,30,100])
    totalTime = flowTime + dimmedTime

    northerlightsFlow(xlight,ylight,birghtness,flowTime)
    threading.Timer((totalTime/10), northernlightsRoutine).start()

#Do all routines
#planner()
northernlightsRoutine()
#daytimeRoutine()
