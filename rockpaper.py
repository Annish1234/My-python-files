#!/usr/bin/python3
import random
n=(int(input("press 1 to play")))
i=0
j=0
while(n==1):
    t=["rock","paper","scissors"]
    Computer=t[random.randint(0,2)]
    print("Enter your Choice:-")
    Player="False"
    Player=input("rock, paper, scissors")
    print("player",Player,"computer",Computer)
    if(Computer==Player):
        print("tie!")
    elif(Computer=="rock"):
        if(Player=="paper"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            print("The paper Wraps the stone!")
            print("Player Wins!")
            i=i+1
        else:
            print("Computer Wins")
            j=j+1
    elif(Computer=="paper"):
        if(Player=="scissors"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            print("The scissors Cuts paper!")
            print("Player Wins!")
            i=i+1
        else:
            print("Computer Wins")

            j=j+1
    elif(Computer=="scissors"):
        if(Player=="rock"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            print("rock Breaks the scissors")
            print("Player Wins!")
            i=i+1
        else:
            print("Computer Wins")
            j=j+1
    if(i>j):
        print("player leads by ",i-j)
    elif(i==j):
        print("The Scores are tied ")
    else:
        print("computer leads by ",j-i)