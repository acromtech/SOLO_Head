#!/usr/bin/python3
from param import offsets #Edit offset.py according to your testbench
import time
from IPython import embed
from odri_spi_rpi import *
import time
import numpy as np
from delta_utils import *

dt = 0.001
ud = SPIuDriver(absolutePositionMode=True, offsets=offsets)
ud.transfer()
# ud.goto(0,0)

f = np.load("traj3.npz")
ps = f["ps"]

q = ik_delta(ps[0])
print(q)
ud.goto(q[0], q[1])

ud.kp0= 5.
ud.kp1= 5.
ud.kd0= 0.3
ud.kd1= 0.3



t = time.perf_counter()
t0 = t
i=0
for i in range(len(ps)):
    q = ik_delta(ps[i])
    v = np.array([0., 0.])

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