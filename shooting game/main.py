import random
from os import system
import keyboard
from time import sleep

grid1 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid2 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid3 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid4 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid5 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid6 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid7 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid8 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
grid9 = [" ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "]
chri = "#"
bullet = "*"
enemies = "@"
system("cls")

def player(player_xpos):
    if player_xpos == 1:
        grid1[14] = chri
    if player_xpos == 2:
        grid2[14] = chri
    if player_xpos == 3:
        grid3[14] = chri
    if player_xpos == 4:
        grid4[14] = chri
    if player_xpos == 5:
        grid5[14] = chri
    if player_xpos == 6:
        grid6[14] = chri
    if player_xpos == 7:
        grid7[14] = chri
    if player_xpos == 8:
        grid8[14] = chri
    if player_xpos == 9:
        grid9[14] = chri


def shooting(bullet_pos):
    pos = 13
    if bullet_pos == 1:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 2:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 3:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 4:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 5:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 6:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 7:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 8:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")
    if bullet_pos == 9:
        for i in range(0,14):
               pos -= 1
               grid1[pos] = bullet 
               sleep(0.1)
               print_board()
               grid1[pos] = " "
               system("cls")

        



def print_board():
    print(grid1)
    print(grid2)
    print(grid3)
    print(grid4)
    print(grid5)
    print(grid6)
    print(grid7)
    print(grid8)
    print(grid9)


def ai():
    pass

def main():
    defalutpos = 5
    while True:
        current_pos = defalutpos
        if defalutpos == 0:
            defalutpos += 1
        if defalutpos == 10:
            defalutpos -= 1
        #defalut pos open
        player(defalutpos)
        print_board()
        #defalut pos close
        while True:
            if keyboard.is_pressed("s") or keyboard.is_pressed("S"):
                sleep(0.1)
                defalutpos += 1
                break
            if keyboard.is_pressed("w") or keyboard.is_pressed("W"):
                sleep(0.1)
                defalutpos -= 1
                break
            if keyboard.is_pressed("l") or keyboard.is_pressed("L"):
                shooting(current_pos) 
        if grid1[14] == chri:
            grid1[14] = " "
        if grid2[14] == chri:
            grid2[14] = " " 
        if grid3[14] == chri:
            grid3[14] = " "
        if grid4[14] == chri:
            grid4[14] = " "
        if grid5[14] == chri:
            grid5[14] = " "
        if grid6[14] == chri:
            grid6[14] = " "
        if grid7[14] == chri:
            grid7[14] = " "
        if grid8[14] == chri:
            grid8[14] = " "
        if grid9[14] == chri:
            grid9[14] = " "



        system("cls")

if __name__ == "__main__":
    main()
    
