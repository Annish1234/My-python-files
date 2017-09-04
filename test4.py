#!/usr/bin/python3
import random 
count=0
r=0
while count<=200:
	roll=input("press r to roll dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is", r)
		print("you are on count",count)																	
	if count==8:
		count=37
		print("you got a ladder")

		
  