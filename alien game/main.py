from time import sleep
from os import system
import keyboard


staring_pos = 8


def sl():
    sleep(1)
    system("cls")
# row = 15
# col = 21


def ma(player_pos):
    global map1 
    map1 = [" "] * 15

    global map2
    map2 = [" "] * 15
    
    global map3
    map3 = [" "] * 15

    global map4
    map4 = [" "] * 15

    global map5
    map5 = [" "] * 15

    global map6
    map6 = [" "] * 15

    global map7
    map7 = [" "] * 15

    global map8
    map8 = [" "] * 15

    global map9
    map9 = [" "] * 15

    global map10
    map10 = [" "] * 15

    global map11
    map11 = [" "] * 15

    global map12
    map12 = [" "] * 15

    global map13
    map13 = [" "] * 15

    global map14
    map14 = [" "] * 15

    global map15
    map15 = [" "] * 15

    global map16
    map16 = [" "] * 15

    global map17
    map17 = [" "] * 15

    global map18
    map18 = [" "] * 15

    global map19
    map19 = [" "] * 15

    global map20
    map20 = [" "] * 15
    
    global player
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
    return (player, player_pos, map1, map2, map3, map4, map5, map6, map7, map8, map9, map10, map11, map12, map13, map14, map15, map16, map17, map17, map18, map19, map20)

def printall():  
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


def main():
    current_pos = 8
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

        if amo > 5 and amo <= 20:
            break
        else:
            system("cls")
            print("RETRY *THE NUMBER HAVE TO BE MORE THAN 5 AND LESS THAN 20")
            sleep(4)
            system("cls")
            
    system("cls")
    print("CONTROLL: A = LEFT D = RIGHT")
    sleep(5)
    system("cls")
    print("START")
    sleep(2)
    system("cls")

    # the first frame

    ma(current_pos)
    printall()
    sl()
    # the first frame 

    while True:
        # main code
        ma(current_pos)
        printall()
        sl()
        if keyboard.is_pressed("a") or keyboard.is_pressed("A"):
            if current_pos == 1:
                current_pos = current_pos + 1
            current_pos = current_pos - 1   
         
        if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
            if current_pos == 15:
                current_pos = current_pos - 1
            current_pos = current_pos + 1 
        
        if keyboard.is_pressed(

        # main code close

        # extra idea
        # if current pos = 1:
            # current pos = 1
        # if current pos = 15:
            # current pos = 15


if __name__ == "__main__":
    main()
