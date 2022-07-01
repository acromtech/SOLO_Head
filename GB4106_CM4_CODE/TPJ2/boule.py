#!/usr/bin/python3
import time
from IPython import embed
from odri_spi_rpi import *
import time

from param import offsets #Edit offset.py according to your testbench
import numpy as np
import matplotlib.pyplot as plt

from delta_utils import *

dt = 0.001
ud = SPIuDriver(absolutePositionMode=True, offsets=offsets)
ud.transfer()
t = time.perf_counter()

r = 0.04
p0 = np.array([0., 0.1])

i = 0
while (True):
    q = np.array([ud.position0,ud.position1])
    p = fk_delta(q)

    d = np.linalg.norm(p - p0)

    # if i%100 == 0:
    #     print(p, p0)

    f = np.zeros(2) if d > r else (1/d/d)*(p - p0)

    tau = 0.5*J(q).transpose()@f

    ud.refCurrent0 = tau[0]
    ud.refCurrent1 = tau[1]

    ud.transfer() #transfer

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