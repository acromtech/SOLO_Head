#!/usr/bin/python3
import time
from IPython import embed
from odri_spi_rpi import *
import time

import numpy as np
import matplotlib.pyplot as plt

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

f = 5. # Hz
a = np.pi # amplitude

t0 = t
duration = 5. # s
pos_ref0s = np.zeros(int(duration/dt) + 1)
pos0s = np.zeros(int(duration/dt) + 1)

i = 0
while (t < t0 + duration):
    pos_ref0 = a*np.sin(2*np.pi*f*(t - t0))
    vel_ref0 = 2*np.pi*f*a*np.cos(2*np.pi*f*(t - t0))

    pos_ref1 = 0.
    vel_ref1 = 0.

    ud.refCurrent0 = Kp * (pos_ref0 - ud.position0) + Kd * (vel_ref0 - ud.velocity0)
    ud.refCurrent1 = Kp * (pos_ref1 - ud.position1) + Kd * (vel_ref1 - ud.velocity1)

    # if int(1000*t) % 100 == 0:
    #     print((ud.position0, pos_ref0))

    ud.transfer() #transfer

    pos_ref0s[i] = pos_ref0
    pos0s[i] = ud.position0

    #wait for next control cycle
    t +=dt
    i = i + 1
    while(time.perf_counter()-t<dt):
        time.sleep(100e-6)
        pass
ud.stop() #Terminate

plt.figure()
plt.plot(pos_ref0s)
plt.plot(pos0s)

plt.show()