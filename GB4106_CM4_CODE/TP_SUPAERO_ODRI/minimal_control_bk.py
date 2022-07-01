#!/usr/bin/python3
import time
from IPython import embed
from odri_spi_rpi import *
import time
dt = 0.001
ud = SPIuDriver()
ud.transfer()
t = time.perf_counter()


Kp = 1.
Kd = 0.05
pos_ref0 = 0.
vel_ref0 = 0.
pos_ref1 = 0.
vel_ref1 = 0.


while True:

    pos_ref0 = ud.position1
    vel_ref0 = ud.velocity1
    pos_ref1 = ud.position0
    vel_ref1 = ud.velocity0
    ud.refCurrent0 = Kp * (pos_ref0 - ud.position0) + Kd * (vel_ref0 - ud.velocity0)
    ud.refCurrent1 = Kp * (pos_ref1 - ud.position1) + Kd * (vel_ref1 - ud.velocity1)

    if int(1000*t) % 100 == 0:
        print((ud.position0, ud.position1))




    ud.transfer() #transfer
    #wait for next control cycle
    t +=dt
    while(time.perf_counter()-t<dt):
        time.sleep(100e-6)
        pass
ud.stop() #Terminate