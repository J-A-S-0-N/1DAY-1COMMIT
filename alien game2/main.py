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
    chri = "#"
    x = 1
    y = 0
    for i in range(0,15):
        if player_pos == x:
            player[y] = chri
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
    print("CONTROLL: A = LEFT D = RIGHT K = SHOOTING") 
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
            current_pos = current_pos + 1
        if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
            if current_pos == 15:
                current_pos = current_pos - 1
            current_pos = current_pos - 1 
        if keyboard.is_pressed("k") or keyboard.is_pressed("K"):
            bullet_pos = currrent_pos 
            pos = 0  
            for i in range(0,15):
                if bullet_pos == pos: 

        


        # main code close

        # extra idea
        # if current pos = 1:
            # current pos = 1
        # if current pos = 15:
            # current pos = 15


if __name__ == "__main__":
    main()