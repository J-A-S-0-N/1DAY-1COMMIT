import keyboard 
from time import sleep
import os
from os import system
import numpy as np

os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\todo app")


def assign_sch_as_var():
    sch_data = {

    }
    data_file = np.genfromtxt("todo.txt", delimiter =  ",")
    vari1 = 1
    for i in data_file:
        sch_data["schedule".format(vari1)] = i
        vari1 += 1


def main():
    while True:
        file = open("todo.txt", "r+")
        data_file = np.genfromtxt("todo.txt", delimiter =  ",")
        system("cls")
        print("press [a] to add new todo list else press [c] to continue")
        inp = input(">> ")
        if inp == "a":
            while True:
                system("cls")
                print("enter the schedule")
                sch_inp = input(">> ")
                if sch_inp != "":
                    file.write(sch_inp + ",")
                    file.close()
                    break
                else:
                    system("cls")
                    print("please enter a valid schdule")
                    sleep(4)
        elif inp == "c":
            while True:
                data = file.readline()
                system("cls")
                print("enter [d] to delete an schedule enter the number of")
        
        else:
            system("cls")
            print("please enter an valid option")
            sleep(3)
            system("cls")
    
if __name__ == "__main__":
    main()