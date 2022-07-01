#!/usr/bin/python3
from param import offsets #Edit offset.py according to your testbench
import time
from IPython import embed
from odri_spi_rpi import *
#import time délaré 2 fois
import numpy as np
from delta_utils import *

dt = 0.001
ud = SPIuDriver(absolutePositionMode=True, offsets=offsets)
ud.transfer()
#if i%1000 == 0:
#    print(f)
# ud.goto(0,0)

N=10000 #10 seconds
c = np.array([0., 0.1])
r = 0.04
f = 1 # Hz

def my_circle_pos(t):
    return np.array([c[0] + r*cos(2*np.pi*f*t), c[1] + r*sin(2*np.pi*f*t)])

def my_circle_vel(t):
    return np.array([-r*2*np.pi*f*sin(2*np.pi*f*t), r*2*np.pi*f*cos(2*np.pi*f*t)])

q = ik_delta(my_circle_pos(0))
print(q)
ud.goto(q[0], q[1])

ud.kp0= 5.
ud.kp1= 5.
ud.kd0= 0.3
ud.kd1= 0.3



t = time.perf_counter()
t0 = t
i=0
for i in range(N):
    q = ik_delta(my_circle_pos(t-t0))
    v = np.linalg.inv(J(q)) @ my_circle_vel(t-t0)

    ud.refPosition0 = q[0]
    ud.refPosition1 = q[1]
    ud.refVelocity0 = v[0]
    ud.refVelocity1 = v[1]

    ud.transfer() #transfer
    #wait for next control cycle
    t +=dt
    while(time.perf_counter()-t<dt):
        pass
        time.sleep(0.0001)
    if (i%100==0):
        print(f"q={q}")

ud.stop() #Terminate