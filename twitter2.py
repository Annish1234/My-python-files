#!/usr/bin/python3
import os 
import time
from gpiozero import MotionSensor #importing motion sensors for the programme 
from TwitterAPI import TwitterAPI
CONSUMER_KEY = 'G5VEfOdfZC2BpVNN3VmIXhmp1'
CONSUMER_SECRET = '2aUoYnMXSjhIGuBATwmamFnK7rb2CCs4eRFbYpcaVn33bhcosq'
ACCESS_TOKEN_KEY = '910781772824068097-4UctxNpBE7ZCS0PcdKk18UwQ0oWyAhV'
ACCESS_TOKEN_SECRET = 'TZcDnfeK6oFNsUOumAWWCHMAGPOQUatAWrxDMJZvdb6D9'
# these are the key and access secret codes for sending the tweet
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
pir = MotionSensor(4)
while True :
    if  pir.motion_detected:
            img="/home/pi/cam/imgs.jpg"
            cmd="fswebcam -F 3 --fps 20 -r 800x600 " +img
            os.system(cmd)
            print ("pic taken")
            file = open(img, 'rb')
            data = file.read()
            r = api.request('statuses/update_with_media', {'status':'pic from pyhton script'}, {'media[]':data})
            print(r.status_code) 
# this is the webcam code including in the programmme , it takes pic and sends to tweeter as status



    
