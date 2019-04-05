#-*- coding: utf-8 -*-
from mq import *
import sys, time

#try:
#    print("Press CTRL+C to abort.")
    
#    mq = MQ();
#    while True:
#        perc = mq.MQPercentage()
#        sys.stdout.write("\r")
#        sys.stdout.write("\033[K")
#        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
#        sys.stdout.flush()
#        time.sleep(0.1)

#except:
#    print("\nAbort by user")
   # e = sys.exc_info()[0]
   # print(e)
   
def Calibrate():
        mq = MQ();
        
def getValue(SensorID):
    mq = MQ();
    perc = mq.MQPercentage()
    if SensorID == 0:
        return perc["GAS_LPG"]
    if SensorID == 1:
        return perc["CO"]
    if SensorID == 3:
        return perc["SMOKE"]
