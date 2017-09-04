#!/usr/bin/python3
import random 
count=0
r=0
while count<=100:
	roll=input("press r to roll dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is", r)
		print("you are on count",count)
		if r<=100:
			print ("u won")