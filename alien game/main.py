from time import sleep
from os import system
import keyboard

def sl():
    sleep(1)
    system("cls")
staring_pos = 8
# row = 15
# col = 21
def printall(player_pos): 
    map1 = [" "] * 15

    map2 = [" "] * 15
    
    map3 = [" "] * 15

    map4 = [" "] * 15

    map5 = [" "] * 15

    map6 = [" "] * 15

    map7 = [" "] * 15

    map8 = [" "] * 15

    map9 = [" "] * 15

    map10 = [" "] * 15

    map11 = [" "] * 15

    map12 = [" "] * 15

    map13 = [" "] * 15

    map14 = [" "] * 15

    map15 = [" "] * 15

    map16 = [" "] * 15

    map17 = [" "] * 15

    map18 = [" "] * 15

    map19 = [" "] * 15

    map20 = [" "] * 15

    player = [" "] * 15

    if player_pos == 1:
        player[0] = "#"
    if player_pos == 2:
        player[1] = "#"
    if player_pos == 3:
        player[2] = "#"
    if player_pos == 4:
        player[3] = "#"
    if player_pos == 5:
        player[4] = "#"
    if player_pos == 6:
        player[5] = "#"
    if player_pos == 7:
        player[6] = "#"
    if player_pos == 8:
        player[7] = "#"
    if player_pos == 9:
        player[8] = "#"
    if player_pos == 10:
        player[9] = "#"
    if player_pos == 11:
        player[10] = "#"
    if player_pos == 12:
        player[11] = "#"
    if player_pos == 13:
        player[12] = "#"
    if player_pos == 14:
        player[13] = "#"
    if player_pos == 15:
        player[14] = "#"

    print(map1)
    print(map2)
    print(map3)
    print(map4)
    print(map5)
    print(map6)
    print(map7)
    print(map8)
    print(map9)
    print(map10)
    print(map11)
    print(map12)
    print(map13) 
    print(map14)
    print(map15)
    print(map16)
    print(map17)
    print(map18)
    print(map19)
    print(map20)
    print(player)
    return (player, current_pos, player_pos)

def main():
    system("cls")
    print("THIS IS AN ALIAN GAME")
    sleep(2) 
    system("Cls")
    print("YOUR OBJECTIVE IS TO ALUMATE ALL THE ALIAN WITH THE SPACE CRAFT")
    sleep(5)
    system("cls")
    while True:
        print("HOW MANY ALIAN DO YOU WANT *IT HAVE TO BE MORE THAN 5 LESS THAN 20")
        amo = input(">>> ")
        amo = int(amo)
        if type(amo) == str:
            print("SORRY THERE IS AN ERROR PLESE RESTART : AMO SHOULD BE A INT RATHER THAN AN STR")
            sleep(4)
            quit()
        if amo < 5 and amo < 20:
            break
        else:
            print("RETRY *THE NUMBER HAVE TO BE MORE THAN 5")
            system("cls")
    system("cls")
    print("CONTROLL: A = LEFT D = RIGHT")
    sleep(5)
    system("cls")
    print("START")
    sleep(2)
    system("cls")

    # the first frame

    printall(staring_pos)
    sl()
    # the first frame 
    while True: 
        # main code 
        if keyboard.is_pressed("a") or keyboard.is_pressed("A"): 

            current_pos = staring_pos - 1
            printall(current_pos)
            sl()
        elif keyboard.is_pressed("d") or keyboard.is_pressed("D"):
            current_pos = staring_pos + 1
            printall(current_pos)
            sl()
        else:
            while True:
                printall(current_pos)
                sl()
                if keyboard.is_pressed("a") or keyboard.is_pressed("A"):
                    break
                elif keyboard.is_pressed("d") or keyboard.is_pressed("D"):
                    break
        # main code
 
if __name__ == "__main__":
    main()
