import random 
from time import sleep
from os import system
import keyboard

# row = 15
# col = 21
def printall(player_pos):
    current_pos = player_pos
    map1_1 = [" " + " " + " " + " " + " " + " " + " "] 
    map1_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map1 = map1_1 + map1_2


    map2_1 = [" " + " " + " " + " " + " " + " " + " "]
    map2_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map2 = map2_1 + map2_2
    

    map3_1 = [" " + " " + " " + " " + " " + " " + " "]
    map3_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map3 = map3_1 + map3_2


    map4_1 = [" " + " " + " " + " " + " " + " " + " "]
    map4_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map4 = map4_1 + map4_2


    map5_1 = [" " + " " + " " + " " + " " + " " + " "]
    map5_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map5 = map5_1 + map5_2


    map6_1 = [" " + " " + " " + " " + " " + " " + " "]
    map6_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map6 = map6_1 + map6_2


    map7_1 = [" " + " " + " " + " " + " " + " " + " "]
    map7_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map7 = map7_1 + map7_2

    map8_1 = [" " + " " + " " + " " + " " + " " + " "]
    map8_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map8 = map8_1 + map8_2 

    map9_1 = [" " + " " + " " + " " + " " + " " + " "]
    map9_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map9 = map9_1 + map9_2

    map10_1 = [" " + " " + " " + " " + " " + " " + " "]
    map10_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map10 = map10_1 + map10_2

    map11_1 = [" " + " " + " " + " " + " " + " " + " "]
    map11_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map11 = map11_1 + map11_2

    map12_1 = [" " + " " + " " + " " + " " + " " + " "]
    map12_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map12 = map12_1 + map12_2

    map13_1 = [" " + " " + " " + " " + " " + " " + " "]
    map13_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map13 = map13_1 + map13_2

    map14_1 = [" " + " " + " " + " " + " " + " " + " "]
    map14_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map14 = map14_1 + map14_2

    map15_1 = [" " + " " + " " + " " + " " + " " + " "]
    map15_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map15 = map15_1 + map15_2

    map16_1 = [" " + " " + " " + " " + " " + " " + " "]
    map16_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map16 = map16_1 + map16_2

    map17_1 = [" " + " " + " " + " " + " " + " " + " "]
    map17_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map17 = map17_1 + map17_2

    map18_1 = [" " + " " + " " + " " + " " + " " + " "]
    map18_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map18 = map18_1 + map18_2

    map19_1 = [" " + " " + " " + " " + " " + " " + " "]
    map19_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map19 = map19_1 + map19_2

    map20_1 = [" " + " " + " " + " " + " " + " " + " "]
    map20_2 = [" " + " " + " " + " " + " " + " " + " " + " "]
    map20 = map20_1 + map20_2

    player_1 = [" " + " " + " " + " " + " " + " " + " "]
    player_2 = [" " + " " + " " + " " + " " + " " + " " + " "] 
    player = player_1 + player_2
    return player

    if player_pos == 1:
        player[0] == "#"
    if player_pos == 2:
        player[1] == "#"
    if player_pos == 3:
        player[2] == "#"
    if player_pos == 4:
        player[3] == "#"
    if player_pos == 5:
        player[4] == "#"
    if player_pos == 6:
        player[5] == "#"
    if player_pos == 7:
        player[6] == "#"
    if player_pos == 8:
        player[7] == "#"
    if player_pos == 9:
        player[8] == "#"
    if player_pos == 10:
        player[9] == "#"
    if player_pos == 11:
        player[10] == "#"
    if player_pos == 12:
        player[11] == "#"
    if player_pos == 13:
        player[12] == "#"
    if player_pos == 14:
        player[13] == "#"
    if player_pos == 15:
        player[14] == "#"

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
    return player

    return current_pos
    return player_pos
def main():
    print("THIS IS AN ALIAN GAME")
    sleep(2) 
    system("Cls")
    print("YOUR OBJECTIVE IS TO ALUMATE ALL THE ALIAN WITH THE SPACE CRAFT")
    sleep(2)
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
    while True: 
        # main code

        printall(7)
        sleep(1)
            # if keyboard.is_pressed("a"):

                # printall(current_pos-1)
                # player = [" " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " "] 
    
            # if keyboard.is_pressed("l"):

                # printall(current_pos-1)
         # player = [" " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " "] 
         # main code
 
if __name__ == "__main__":
    main()
