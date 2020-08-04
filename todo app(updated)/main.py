#imports
import keyboard 
from time import sleep
import os
from os import system
import numpy as np

#change the diratory for opening file
os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\todo app")


def assign_sch_as_var():
    #dict for all the schadule
    sch_data = {

    }
    #opening the file for the data
    data_file = np.genfromtxt("todo.txt", delimiter =  ",")
    vari1 = 1
    for i in data_file:
        #add data named "schdule"
        sch_data["schedule".format(vari1)] = i
        vari1 += 1


def main():
    while True:
        #open the file for writeing the data
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
                #if the input sch_inp is not empty
                if sch_inp != "":
                    #wite the line from  sch_inp and add , at the end
                    file.write(sch_inp + ",")
                    #close the file
                    file.close()
                    break
                else:
                    #this will run if the inp input is not valid or is empty
                    system("cls")
                    print("please enter a valid schdule")
                    sleep(4)
        elif inp == "c":
            # this is the main part
            while True:
                data = file.readline()
                assign_sch_as_var()
                system("cls")
                print("enter [d] to delete an schedule enter the number of")
        
        else:
            # this will run if the inp is not assigned
            system("cls")
            print("please enter an valid option")
            sleep(3)
            system("cls")
    
#main loop
if __name__ == "__main__":
    main()