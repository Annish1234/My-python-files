#!/usr/bin/python3
import os 
import time
from gpiozero import MotionSensor
pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("perimeter breached code red")
        b=1
        cmd="fswebcam -F 3 --fps 20 -r 800x600 cam"+str(b)+ ".jpg"
        os.system(cmd)

