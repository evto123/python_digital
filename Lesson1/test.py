from random import randint
from time import sleep

print("Welcome to our cube game \n-----------\nEach turn cost: 3 ILS ")

money=int(input("Enter how much money do you have?\n"))
turns=(money//3)
print("You have: " + str(turns//3) + "turns\nYour change: " + str(money%3) + " ILS\n")
prize=0

for i in range(turns):
    print("Round number: " + str(i+1) + "\n--------------\n")
    sleep(2)
    cube1=randint(1,4)
    cube2=randint(1,4)
    print("Cube1: " + str(cube1) + "\nCube2: " + str(cube2) + "\n")
    if(cube1==cube2):
        if(cube1==6):
            prize=prize + 1000
        else:
            prize=prize+100
    elif(cube1==cube1):
        prize=prize + 20
    elif(cube2==cube2):
        prize + 40
    print("Calculating your prize: ")
    sleep(2)
    print("Your prize: " + str(prize) + " ILS ")
