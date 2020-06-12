import random
from time import sleep
import sys
import keyboard
from os import system



r = "rock"
p = "paper" 
s = "sissor" 
rps = [r,p,s]




while True:
    print("enter rock[r] paper[p] sissor[s]]")
    aic = random.choice(rps)
    while True:
        if keyboard.is_pressed("r"):
            print("ai   : "+aic)
            print("user : rock")
            if aic == p:
                print("you lost")
                time = 10
                for i in range(0 ,10):
                    print("enter rock[r] paper[p] sissor[s]]")
                    print("ai   : "+aic)
                    print("user : rock")
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)

            elif aic == r: 
                print("draw")
                sleep(3)
                time = 10
                sleep(2)
                system("cls")
                for i in range(0 ,10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
                
            elif aic == s:
                print("you won nice")
                time = 10
                sleep(2)
                system("cls")
                for i in range(0 ,10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
        if keyboard.is_pressed("p"):
            print("ai   : " + aic)
            print("user : paper")
            if aic == p:
                print("draw")
                sleep(3)
                time = 10
                sleep(2)
                system("cls")
                for i in range(0 ,10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
            elif aic == r:
                print("nice you won")
                time = 10
                sleep(2)
                system("cls")
                for i in range(0, 10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
            elif aic == s:
                print("you lost")
                time = 10
                sleep(2)
                system("cls")
                for i in range(0 ,10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
        if keyboard.is_pressed("s"):
            print("ai   : "+aic)
            print("user : sissor")
            if aic == p:
                print("nice you won")
                time = 10
                sleep(2)
                system("cls")
                for i in range(0 ,10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
            elif aic == r:
                print("you lost")
                time = 10
                sleep(2)
                system("cls")
                for i in range(0 ,10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
            elif aic == s:
                print("draw")
                sleep(3)
                time = 10
                sleep(2)
                system("cls")
                for i in range(0 ,10):
                    print("closing in " + str(time))
                    time = time - 1
                    sleep(1)
                    system("cls")
                    if time == 0:
                        sys.exit(0)
