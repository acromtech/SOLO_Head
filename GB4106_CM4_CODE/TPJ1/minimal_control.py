#!/usr/bin/python3
import time
from IPython import embed
from odri_spi_rpi import *
import time
dt = 0.001
ud = SPIuDriver()
ud.transfer()
t = time.perf_counter()
while True:
    ud.transfer() #transfer
    print(ud.position0)
    #wait for next control cycle
    t +=dt
    while(time.perf_counter()-t<dt):
        pass
ud.stop() #Terminate