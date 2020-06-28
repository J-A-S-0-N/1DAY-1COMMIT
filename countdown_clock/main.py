from time import sleep
from os import system

def main():
    print("how much time do you want?")
    time = input(">>> ")
    system("cls")
    for i in range(0, int(time)):
        system("cls")
        print(str(time))
        sleep(1)
        time = int(time)
        time -= 1
        if time == 0:
            quit()
        
        
    
    

if __name__ == "__main__":
    main()