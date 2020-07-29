from os import system
from database import newschedule
import keyboard
import mysql.connector as mysql

#to call other script in this case database i need to enter database.blablas

#my data base information
dbusername = "root"
dbname = "schedule"
dbppasswd = "Jason671404"
dbhost = "localhost"

#connecting to to the my sql
db = mysql.connect(host=dbhost,
                    user=dbusername,
                    passwd=dbppasswd,
                    db=dbname)

def main():
    while True:
        new_schedule_breakcheck = False
        #creating cursor to execut sqlcommand 
        database.printall()
        cur = db.cursor()
        print('press "n" to make new shedule')
        print('press "d" to delete the schedule')
        if keyboard.is_pressed("n"):#new shedule
            while True:
                #break if the new_schedule_breakcheck is true, default : False
                if new_schedule_breakcheck == True: break
                system("cls")
                print("enter the name of the new shedule")
                new_schedule_name = input(">>> ")
                system("cls")
                print("enter the time which this will execute")
                new_schedule_time = input(">>> ")
                system("cls")
                print("enter what the message is")
                new_scheduraw_message = input(">>> ")
                system("cls")
                print("is this corre\nthe name : " + new_schedule_name + "\nthe time : " + new_schedule_time + "\ntge message : " + new_scheduraw_message)
                while True:
                    print("yes[y] no[n]")
                    new_schedule_yes_no = input(">>> ")
                    if new_schedule_yes_no == "y":
                        system("cls")
                        print("great")
                        new_schedule_breakcheck = True
                        database.newschedule(new_schedule_time, new_schedule_name, new_scheduraw_message)
                        break
                    else:
                        system("cls")
                        print("please enter y or n")
                        sleep(3)
                        system("cls")
    
        elif keyboard.is_pressed("d"):
            pass
        else:
            #main loop
            while True:
                pass
                

if __name__ == "__main__":
    main()
    


