#!/usr/bin/python3
import smtplib
import time
import os
import RPi.GPIO as GPIO
import speech_recognition as sr
import random
a=0
x=0
print("secrity system with high security opens only for authorised users only")
r=input("press the letter s for entering into the acceing menu :::")
if r=="s":
	print("your now in front of a most securable safety wall")
	print("press the letter v for opening the door by voice command .open it if your a authorised users only")
	print("press the letter s for opening the door by sensing.strictly only for authorised users only")
	print("press the letter q for opening the door by access code only authorised,registered user can access this ")
	print("your under surviliance be carefull.")
	b=input("press your choice to get the most secure bank locker in this world::::")
	if b=="v":
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source,duration=5)
			print("Say something!")
			while True:
				audio = r.listen(source) 
				print("You said: " + r.recognize_google(audio))
				if r.recognize_google(audio)=="hello":
					print("the door will be open for 3seconds")
					GPIO.setmode(GPIO.BOARD)
					GPIO.setup(7,GPIO.OUT)
					GPIO.setup(11,GPIO.OUT)
					GPIO.output(7,True)
					GPIO.output(11,False)
					time.sleep(4)
					GPIO.output(7,False)
					GPIO.output(11,True)
					time.sleep(1)
					GPIO.cleanup()
					os.system("fswebcam -F 3 --fps 20 -r 1200x800 DOOR.jpg")
					s = smtplib.SMTP('smtp.gmail.com',)
					s.starttls()
					s.login("balajikumar189@gmail.com", "balaji@google")
					message = "ALERT,ALERT TO THE AUTHORIZED USERS OF HI TECH SAFETY DOOR OF THE BANK IS BEEN ACCESSED USING THE SECRET PASSWORD"
					s.sendmail("balajikumar189@gmail.com", "balajikumar189@gmail.com", message)
					s.quit()
	if b=="s":
		print("this part of the door security is unprotected with no password and the door will be opened for 3seconds,the door is opened by means of sensing only")
		pir = MotionSensor(27)
		while True:
			if pir.motion_detected:
					print("SOME STRANGER IS IN FRONT OF THE DOOR")
					os.system("fswebcam -F 3 --fps 20 -r 1200x800 DOOR1.jpg")
					GPIO.cleanup()
					GPIO.setmode(GPIO.BOARD)
					GPIO.setup(7,GPIO.OUT)
					GPIO.setup(11,GPIO.OUT)
					GPIO.output(7,True)
					GPIO.output(11,False)
					time.sleep(4)
					GPIO.output(7,False)
					GPIO.output(11,True)
					time.sleep(1)
					GPIO.cleanup()
					print("the door is been opened by u but the authority will get the message that the door is opened by sensing,your in hi.tech security system")
					s = smtplib.SMTP('smtp.gmail.com',)
					s.starttls()
					s.login("balajikumar189@gmail.com", "balaji@google")
					message = "ALERT,ALERT TO THE AUTHORIZED USERS OF HI TECH SAFETY DOOR OF THE BANK IS BEEN ACCESSED USING THE SECRET PASSWORD"
					s.sendmail("balajikumar189@gmail.com", "balajikumar189@gmail.com", message)
					s.quit()
					os.system("fswebcam -F 3 --fps 20 -r 1200x800 DOOR2.jpg")				
    if b=="q":
    	print("you will get otp to your mail if and only if your a authorized user")
    	bal=input("press g to get the access code::")
    	if bal=="g":
    		s = smtplib.SMTP('smtp.gmail.com',)
    		s.starttls()
    		s.login("balajikumar189@gmail.com","indian-american")
    		m=str(random.randint(111111,999999))
    		s.sendmail("balajikumar189@gmail.com", "balajikumar189@gmail.com", m)
    		s.quit()
    		print("please enter the otp sent to your authorised email id ")
    		a=str(input("enter the otp send to your mail id:::"))
    		if a=="m":
    			GPIO.setmode(GPIO.BOARD)
                GPIO.setup(7,GPIO.OUT)
                GPIO.setup(11,GPIO.OUT)
                GPIO.output(7,True)
                GPIO.output(11,False)
                time.sleep(4)
                GPIO.output(7,False)
                GPIO.output(11,True)
                time.sleep(1)
                GPIO.cleanup()
				print("thank u")