from os import system
from time import sleep
from database_schedule import *
import keyboard
from message import message
import datetime

# "#" = need to add later

def main():
    while True:
        breakcheck = False
        database_schedule.print_schedule()
        print("press [n] to write an new schedule")
        print("press [d] to delete an schedule")
        print("press [r] to resume the schedule")
        while True:
            if breakcheck == True: break
            if keyboard.is_pressed("n"):
                system("cls")
                print("enter the name")
                new_name = input(">>> ")
                system("cls")
                print("enter the time which it executes * have to be hour")
                new_time = input(">>> ")
                system("cls")
                print("enter the message")
                new_message = input(">>> ")
                while True:
                    system("cls")
                    print("is this correct??\nname : " + new_name + "\ntime : " + new_time + " hour\n" + "message : " + new_message)
                    print("yes[y] no[n]")
                    new_check = input(">>> ")
                    if new_check == "y":
                        breakcheck = True
                        database_schedule.new_schedule(new_name, new_time, new_message)
                        break 
                    elif new_check == "n":
                        system("cls")
                    else:
                        system("cls")
                        print("please enter y or n")
                        sleep(3)
                        system("cls")
           
            if keyboard.is_pressed("d"):
                print("enter the name that you want to delete")
                delete_name = input(">>> ")
                while True:
                    system('cls')
                    print("is this correct???\nname : " + delete_name)
                    print("yes[y] no[n]")
                    delete_checker = input(">>> ")
                    if delete_checker == 'y':
                        breakcheck = True
                        database_schedule.delete(delete_name)
                    elif delete_checker == 'n':
                        system("cls")                        
                    else:
                        print("please enter y or n")
                        sleep(3)
                        system("cls")

            if keyboard.is_pressed("r"):
                dateabase_schedul.get_all_item()
                schedulelist = {

                }
                
                schedulelist_lenght = len(schedulelist)
                #add the time to the time list
                now = datetime.datetime.now()
                while True:
                    current_time = datetime.time(now.hour)
                    for i in range(0,timelist_lenght):
                        if time1 == time1:
                            message.message()
                    sleep(10)