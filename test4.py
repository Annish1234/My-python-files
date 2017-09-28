#!/usr/bin/python3
import random # it imports random
count=0
r=0
while count<=200:
	roll=input("press r to roll dice")# its the input give to run the programme
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is", r)
		print("you are on count",count)																	
	

		
  
