#!/usr/bin/python3
from gpiozero import MotionSensor

pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("perimeter breached code red")
