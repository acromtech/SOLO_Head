#!/usr/bin/python3
#Thomas Flayols - feb 2022
import time
from IPython import embed
from odri_spi_rpi import *
import time

dt = 0.001
ud = SPIuDriver(absolutePositionMode=True)
ud.transfer()
#ud.goto(0,0)
#ud.goto(0,0)
t = time.perf_counter()
goal_position = 0.00
state=0
while True :
    init_goal_position = 2*pi
    while True :
        if init_goal_position > goal_position :
            if state==0: #acceleration
                goal_position = goal_position + (0.005 * (abs(goal_position-init_goal_position)+0.001))
                if init_goal_position*(1/3)<goal_position:
                    state=1
            elif state==1: #plat
                goal_position = goal_position + (0.005)
                if init_goal_position*(2/3)<goal_position:
                    state=2
            elif state==2: #deceleration
                goal_position = goal_position + (0.005 * ((init_goal_position-goal_position)+0.001))
                if init_goal_position < goal_position :
                    state=0
                    break

        elif init_goal_position < goal_position :
            if state==0: #acceleration
                goal_position = goal_position - (0.005 * (abs(init_goal_position-goal_position)+0.001))
                if init_goal_position*(1/3)>goal_position:
                    state=1
            if state==1: #plat
                goal_position = goal_position - (0.005)
                if init_goal_position*(2/3)>goal_position:
                    state=2
            if state==2: #deceleration
                goal_position = goal_position - (0.005 * ((goal_position-init_goal_position)+0.001))
                if init_goal_position > goal_position :
                    state=0
                    break

        ud.transfer() #transfer
        ud.refCurrent0 = 2.0 * (goal_position-ud.position0) - 0.01 * ud.velocity0
        ud.refCurrent1 = 0 #1.0 * (goal_position-ud.position1) - 0.1*ud.velocity1
        print(f"pos={ud.position0}")
        #print(f"i0 ={ud.refCurrent0}")
        #wait for next control cycle
        t += dt
        while(time.perf_counter()-t<dt):
            pass

    init_goal_position = 0
    while True :
        if init_goal_position > goal_position :
            if state==0: #acceleration
                goal_position = goal_position + (0.005 * (abs(goal_position-init_goal_position)+0.001))
                if init_goal_position*(1/3)<goal_position:
                    state=1
            elif state==1: #plat
                goal_position = goal_position + (0.005)
                if init_goal_position*(2/3)<goal_position:
                    state=2
            elif state==2: #deceleration
                goal_position = goal_position + (0.005 * ((init_goal_position-goal_position)+0.001))
                if init_goal_position < goal_position :
                    state=0
                    break

        elif init_goal_position < goal_position :
            if state==0: #acceleration
                goal_position = goal_position - (0.005 * (abs(init_goal_position-goal_position)+0.001))
                if init_goal_position*(1/3)>goal_position:
                    state=1
            if state==1: #plat
                goal_position = goal_position - (0.005)
                if init_goal_position*(2/3)>goal_position:
                    state=2
            if state==2: #deceleration
                goal_position = goal_position - (0.005 * ((goal_position-init_goal_position)+0.001))
                if init_goal_position > goal_position :
                    state=0
                    break

        ud.transfer() #transfer
        ud.refCurrent0 = 2.0 * (goal_position-ud.position0) - 0.01 * ud.velocity0
        ud.refCurrent1 = 0 #1.0 * (goal_position-ud.position1) - 0.1*ud.velocity1
        print(f"pos={ud.position0}")
        #print(f"i0 ={ud.refCurrent0}")
        #wait for next control cycle
        t += dt
        while(time.perf_counter()-t<dt):
            pass
ud.stop() #Terminate