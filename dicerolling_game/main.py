import random 
from time import sleep
from os import system
import keyboard
import sys

a = 1
b = 2
c = 3
d = 4
e = 5 
f = 6

a = [a,b,c,d,e,f]
    
while True:
    print("if you got higher number than the ai you win")
    sleep(2)
    print("press enter ")
    while True:
        if keyboard.is_pressed("enter"):
            while True:
                system("cls")
                aic = random.choice(a)
                userc = random.choice(a)
                out1 = False
                out2 = False
                sleep(2)
                print("ai's choice   : " + str(aic))
                sleep(2)
                print("user's choice : " + str(userc))
                sleep(2)
                if aic < userc:
                    print("nice you won")
                    print("do you want to do it agian? yes[y] no[n]")
                    while True: 
                        if keyboard.is_pressed("y"):
                            out2 = True
                            out1 = True
                        elif keyboard.is_pressed("n"):
                            cd = 10
                            for i in range(0,10):
                                system("cls")
                                print("closing in " + str(cd))
                                cd = cd - 1
                                sleep(1)
                                if cd == 0:
                                    sys.exit(0)
                        if out1 == True:
                            break
                elif aic == userc:
                    print("draw")
                    print("do you want to do it agian? yes[y] no[n]")
                    while True: 
                        if keyboard.is_pressed("y"):
                            out2 = True
                            out1 = True
                        elif keyboard.is_pressed("n"):
                            cd = 10
                            for i in range(0,10):
                                system("cls")
                                print("closing in " + str(cd))
                                cd = cd - 1
                                sleep(1)
                                if cd == 0:
                                    sys.exit(0)
                        if out1 == True:
                            break
                else:
                    print("you lost")
                    print("do you want to do it agian? yes[y] no[n]")
                    while True: 
                        if keyboard.is_pressed("y"):
                            out2 = True
                            out1 = True
                        elif keyboard.is_pressed("n"):
                            cd = 10
                            for i in range(0,10):
                                system("cls")
                                print("closing in " + str(cd))
                                cd = cd - 1
                                sleep(1)
                                if cd == 0:
                                    sys.exit(0)
                        if out1 == True:
                            break



