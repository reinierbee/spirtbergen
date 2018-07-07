#!/usr/bin/python

from phue import Bridge
import threading
from numpy import random
from random import randrange
from datetime import datetime, time
from time import gmtime, strftime

#Connection
b = Bridge('192.168.2.3')
b.connect()

#Timing


start_of_night_transition_hours = "09"
start_of_night_transition_minutes = "40"
#start_of_night_transition_time = 18000
start_of_night_transition_time = 300


start_of_night_transition = time(int(float(start_of_night_transition_hours)), int(float(start_of_night_transition_minutes)))
end_of_night_transition = time(9,45)
end_of_nothernlights = time(9, 50)


#Lights
dayX = 0.4500
dayY = 0.3500

nightX = 0.5900
nightY = 0.3800

can_i_has_nothernlights = False

start_of_night_light = {'transitiontime' : (start_of_night_transition_time * 10), 'on' : True, 'bri' : 0, 'xy' : [nightX, nightY]}

night_time_light = {'on' : False, 'bri' : 0, 'xy' : [dayX, dayY]}
day_time_light = {'on' : True, 'bri' : 254, 'xy' : [dayX, dayY]}

end_of_day_time = "T" + start_of_night_transition_hours + ":" + start_of_night_transition_minutes + ":00"


def bootstrap():
    b.set_light([1,2,3,4,5], day_time_light)
    planner()
    day_time_routine()


#planner
def planner():
    b.delete_schedule(1)
    today = strftime("%Y-%m-%d", gmtime())
    date_time = today + end_of_day_time
    b.create_schedule('End of day', date_time, 1, start_of_night_light)

    print("Planned new event for: " + date_time)
    print("Duration : ")

    #rescedule this every 4 hours to be sure we queue up again on the right time
    threading.Timer(14400, planner).start()


def is_night(time_to_check):
    if time_to_check > end_of_night_transition or time_to_check < start_of_night_transition:
        return True

    if time_to_check > start_of_night_transition and time_to_check < end_of_night_transition:
        return False

    if time_to_check == end_of_night_transition:
        return True

    return True

def day_time_routine():
    threading.Timer(30.0, day_time_routine).start()
    global can_i_has_nothernlights

    now__time = datetime.now().time()

    if is_night(now__time):
        print("Night Time detected, checking northernlights.")
        if now__time < end_of_nothernlights:
            print("Nothern lightsssss")
            can_i_has_nothernlights = True
            northernlights_routine()
        else:
            can_i_has_nothernlights = False
            b.set_light([1,2,3,4,5], night_time_light)
    else:
        print("Day Time detected.")
        can_i_has_nothernlights = False


#northernlights
def northernlights_flow(x, y, brightness, flow_time):
    l1Time = randrange(0, flow_time)
    remainder = flow_time - l1Time
    l2Time = randrange(0,remainder)
    remainder =  remainder- l2Time
    l3Time = randrange(0,remainder)
    remainder = remainder - l3Time
    l4Time = randrange(0,remainder)
    remainder = remainder - l4Time
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

def northernlights_routine():
    if can_i_has_nothernlights:
        xlight = random.uniform(0.05, 0.20)
        ylight = random.uniform(0.65, 0.35)
        brightness = randrange(30,100)
        flow_time = randrange(30,70)
        dimmed_time = random.choice([0,0,0,0,0,0,0,10,10,20,30,100])
        totalTime = flow_time + dimmed_time

        northernlights_flow(xlight, ylight, brightness, flow_time)
        threading.Timer((totalTime/10), northernlights_routine).start()
    else:
        return

#Do all routines
bootstrap()
