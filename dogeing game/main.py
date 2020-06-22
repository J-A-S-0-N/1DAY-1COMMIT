from time import sleep
from os import system
import keyboard

# goals:
    # set all the chri on line 10
    # set external detection sys:
        # if the player is in the out1, out2, or all the map 0 and 9



def map(ypos, xpos):
    chri = "@"
    global out1
    out1 = [" "] * 9
    global map1
    map1 = [" "] * 9
    global map2
    map2 = [" "] * 9 
    global map3
    map3 = [" "] * 9  
    global map4
    map4 = [" "] * 9  
    global map5
    map5 = [" "] * 9  
    global map6
    map6 = [" "] * 9 
    global map7
    map7 = [" "] * 9
    global out2
    out2 = [" "] * 9
    # y = 1
    if ypos == 1 and xpos == 1:
        map1[0] = chri
        
    if ypos == 1 and xpos == 2:
        map1[1] = chri 
        
    if ypos == 1 and xpos == 3:
        map1[2] = chri 

    if ypos == 1 and xpos == 4:
        map1[3] = chri 

    if ypos == 1 and xpos == 5:
        map1[4] = chri 

    if ypos == 1 and xpos == 6:
        map1[5] = chri 

    if ypos == 1 and xpos == 7:
        map1[6] = chri 

    # Y = 2 
    if ypos == 2 and xpos == 1:
        map2[0] = chri 

    if ypos == 2 and xpos == 2:
        map2[1] = chri 

    if ypos == 2 and xpos == 3:
        map2[2] = chri 

    if ypos == 2 and xpos == 4:
        map2[3] = chri 

    if ypos == 2 and xpos == 5:
        map2[4] = chri 

    if ypos == 2 and xpos == 6:
        map2[5] = chri 

    if ypos == 2 and xpos == 7:
        map2[6] = chri 

    # y = 3
    if ypos == 3 and xpos == 1:
        map3[0] = chri

    if ypos == 3 and xpos == 2:
        map3[1] = chri

    if ypos == 3 and xpos == 3:
        map3[2] = chir 

    if ypos == 3 and xpos == 4:
        map3[3] = chri 

    if ypos == 3 and xpos == 5:
        map3[4] = chri

    if ypos == 3 and xpos == 6:
        map3[5] = chri 

    if ypos == 3 and xpos == 7:
        map3[6] = chri 

    # y = 4
    if ypos == 4 and xpos == 1:
        map4[0] = "@"

    if ypos == 4 and xpos == 2:
        map4[1] = "@"

    if ypos == 4 and xpos == 3:
        map4[2] = "@"

    if ypos == 4 and xpos == 4:
        map4[3] = "@"

    if ypos == 4 and xpos == 5:
        map4[4] = "@"

    if ypos == 4 and xpos == 6:
        map4[5] = "@" 

    if ypos == 4 and xpos == 7:
        map4[6] = "@"

    # y = 5
    if ypos == 5 and xpos == 1:
        map5[0] = "@"

    if ypos == 5 and xpos == 2:
        map5[1] = "@"

    if ypos == 5 and xpos == 3:
        map5[2] = "@"

    if ypos == 5 and xpos == 4:
        map5[3] = "@"

    if ypos == 5 and xpos == 5:
        map5[4] = "@"
    
    if ypos == 5 and xpos == 6:
        map5[5] = "@"

    if ypos == 5 and xpos == 7:
        map5[6] = "@"

    # y = 6
    if ypos == 6 and xpos == 1:
        map6[0] = "@"

    if ypos == 6 and xpos == 2:
        map6[1] = "@"

    if ypos == 6 and xpos == 3:
        map6[2] = "@" 

    if ypos == 6 and xpos == 4:
        map6[3] = "@"

    if ypos == 6 and xpos == 5:
        map6[4] = "@"

    if ypos == 6 and xpos == 6:
        map6[5] = "@"

    # y = 7
    if ypos == 7 and xpos == 1:
        map7[0] = "@" 

    if ypos == 7 and xpos == 2:
        map7[1] = "@"

    if ypos == 7 and xpos == 3:
        map7[2] = "@"

    if ypos == 7 and xpos == 4:
        map7[3] = "@"

    if ypos == 7 and xpos == 5:
        map7[4] = "@"

    if ypos == 7 and xpos == 6:
        map7[5] = "@"

    if ypos == 7 and xpos == 7:
        map7[6] = "@"

    return (map1, map2, map3, map4, map5, map6, map7)


def printall():
    print(map1)
    print(map2)
    print(map3)
    print(map4)
    print(map5)
    print(map6)
    print(map7)


def main():
    defalut_posx = 4
    defalut_posy = 4
    while True:
        map(defalut_posx, defalut_posy)
        printall()
        if keyboard.is_pressed("a"):
            sleep(0.1)
            # defalut_posx not changed
            defalut_posy -= 1 
        if keyboard.is_pressed("d"):
            # defalt_posx not changed 
            defalut_posy += 1
            sleep(0.1)
        if keyboard.is_pressed("s"):
            defalut_posx += 1
            # defalt_posy not changed
            sleep(0.1)
        if keyboard.is_pressed("w"):
            defalut_posx -= 1
            # dedalt_posy not changed 
            sleep(0.2)
        system("cls")
        if defalut_posx == 7:


if __name__ == "__main__":
    main()
