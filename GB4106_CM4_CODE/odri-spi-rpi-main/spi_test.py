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
goalPosition = 0.0
while True:
    goalPosition +=0.01
    ud.transfer() #transfer
    ud.refCurrent0 = 2.0 * (goalPosition-ud.position0)-0.01*ud.velocity0
    ud.refCurrent1 = 0 #1.0*(goalPosition-ud.position1)-0.1*ud.velocity1
    print(f"pos={ud.position0}")
    #print ( f"i0 ={ud.refCurrent0}" )
    #wait for next control cycle
    t +=dt
    while(time.perf_counter()-t<dt):
        pass
    if goalPosition >2*pi:
        break

while True:
    goalPosition -=0.01
    ud.transfer() #transfer
    ud.refCurrent0 = 2.0 * (goalPosition-ud.position0)-0.01*ud.velocity0
    ud.refCurrent1 = 0 #1.0*(goalPosition-ud.position1)-0.1*ud.velocity1
    print(f"pos={ud.position0}")
    #print ( f"i0 ={ud.refCurrent0}" )
    #wait for next control cycle
    t +=dt
    while(time.perf_counter()-t<dt):
        pass
    if goalPosition <0:
        break
ud.stop() #Terminate