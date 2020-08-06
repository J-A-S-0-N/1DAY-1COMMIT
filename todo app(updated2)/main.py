#imports
import keyboard 
from time import sleep
import os
from os import system
import numpy as np

#change the diratory for opening file
os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\todo app")
file = open("todo.txt", "r+")

def assign_sch_as_var():
    #opening the file for the data
    data = file.read()
    global data_list
    data_list = data.split(",")

def print_all():
    count = 1
    for i in data_list:
        print(str(count) + " " + str(i))
        count += 1

def test_dict_printall():
    print(data_dict)

def adding_to_dict():
    global data_dict
    data_dict = {

    }
    global count
    count = 1
    for i in data_list:
        data_dict.update({"sch" + str(count) : i})
        count += 1



def delete(item):
    pass

def main():
    while True:
        #open the file for writeing the data
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
                    empty = os.stat("todo.txt").st_size == 0 
                    if empty == True:
                        file.write(sch_inp)
                    else:
                        file.write(","+ sch_inp)

                    break
                else:
                    #this will run if the inp input is not valid or is empty
                    system("cls")
                    print("please enter a valid schdule")
                    sleep(4)
        elif inp == "c":
            # this is the main part
            while True:
                system("cls")
                assign_sch_as_var()
                print("enter the number of the schdule to delete it")
                print_all()
                #behind
                adding_to_dict()
                #test_dict_printall()
                while True:
                    del_inp = input(">> ")
                    del_choice = 1
                    for i in range(0, len(data_list)):
                        if del_inp == str(del_choice):
                            pass
                        del_choice += 1

        else:
            # this will run if the inp is not assigned
            system("cls")
            print("please enter an valid option")
            sleep(3)
            system("cls")
    
#main loop
if __name__ == "__main__":
    main()

#dont need but just in case i might use it later

#dict for all the schadule
# global sch_data
# sch_data = {

# }

# data_file = np.genfromtxt("todo.txt", delimiter =  ",")
# vari1 = 1
# for i in data_file:
#     # add data named "schdule"
#     sch_data["schedule".format(vari1)] = i
#     vari1 += 1

    # count = 1
# for i in sch_data:
#     print(str(count) + " " + str(i))
#     count += 1


# def adding(item):
#     data_dict.update({"sch" + str(count) : item})