import os
from time import sleep
import keyboard
from os import system, sys

os.chdir(path="C:\\all\\guessing")
data = open("data.txt", "r")

q = 1 and False
r = 1 and False 
w = 0 and False 
e = 0 and False 
t = 0 and False 
y = 0 and False 

s = 1 and False
d = 1 and False
g = 1 and False
a = 0 and False 
f = 0 and False 
h = 0 and False 

z = 0 and False 
x = 0 and False 
c = 0 and False 
b = 0 and False 
v = 1 and False
n = 1 and False

name = "nt"

print(q)

grid = '''
q w e r t y
a s d f g h
z x c v b n
'''
l1 = ["q ", "w ", "e ", "r ", "t ", "y "]
l2 = ["a ", "s ", "d ", "f ", "g ", "h "]
l3 = ["z ", "x ", "c ", "v ", "b ", "n "]
answer = '''
1 0 0 1 0 0
0 1 1 0 1 0
0 0 0 1 0 1
'''

time = 7
trys = 6

print("try to avoid 0")
print("O = '1' , X = '0'")
print("you have "+ str(trys)+ " trys")
sleep(5)
print(answer)
sleep(time)
system("cls")
print(grid)
    #l1
while True:
    if keyboard.is_pressed('q'):
        if q == 1:
            l1[0] = "1  "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            q = True
        else:
            l1[0] = "0 " 
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('w'):
        if w == 1:
            l1[1] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            w = True
        else:
            l1[1] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('e'):
        if e == 1:
            l1[2] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            e = True
        else:
            l1[2] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('r'):
        if r == 1:
            l1[3] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            r = True
        else:
            l1[3] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('t'):
        if t == 1:
            l1[4] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            t = True
        else:
            l1[4] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('y'):
        if y == 1:
            l1[5] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            y = True
        else:
            l1[5] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1


    if keyboard.is_pressed('a'):
        if a == 1:
            l2[0] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            a = True
        else:
            l2[0] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('s'):
        if s == 1:
            l2[1] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            s = True
        else:
            l2[1] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('d'):
        if d == 1:
            l2[2] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            d = True
        else:
            l2[2] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('f'):
        if f == 1:
            l2[3] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            f = True
        else:
            l2[3] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('g'):
        if g == 1:
            l2[4] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            g = True
        else:
            l2[4] = "0 "
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('h'):
        if h == 1:
            l2[5] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            h = True
        else:
            l2[5] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
        
    if keyboard.is_pressed('z'):
        if z == 1:
            l3[0] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            z = True
        else:
            l3[0] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('x'):
        if x == 1:
            l3[1] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            x = True
        else:
            l3[1] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('c'):
        if c == 1:
            l3[2] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            c = True
        else:
            l3[2] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)  
            trys = trys - 1     
    if keyboard.is_pressed('v'):
        if v == 1:
            l3[3] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            v = True
        else:
            l3[3] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('b'):
        if b == 1:
            l3[4] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            b = True
        else:
            l3[4] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if keyboard.is_pressed('n'):
        if n == 1:
            l3[5] = "1 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            n = True
        else:
            l3[5] = "0 "
            system("cls")
            print(l1)
            print(l2)
            print(l3)
            trys = trys - 1
    if trys == 0:
        print("you lost")
        sleep(4)
        exit()
    if q == True and r == True and s == True and d == True and g == True and c == True and n == True:
        time = time - 1 
        print('now to level ' + time)
        sleep(3)
        system("cls")            
        
        #q r s d g v n
        #q r s d g v n
    #if correct:
        #time = time - 1
    
#gamedata.txt = {
    #how many is 1  from easy
    #how many is 1 from hard
    #how many is 1 from midium
    #the amout of trys you get #
    #the amout of life you get #
#}
#changedir to the main game folder
#make a function that check if the user get all correct

#while loop: 
    #seletion of easy midium or hard
    #assingn keyboard to 1 or 0
    #1 is correct
    #show the answer for couple seccond
    #cover the grid with the keyboard pattern
    #6  by 3 grid 
    #if you hit q the first one appers :
        #the grid on q appers

    #do that with 18 keys

    #if the grid that the user hit is 1:
        #s#how the correct one that the user hit
    #if the grid that thee user hit is 0:
        #minus one from the data 
    #if all the one is founded :
        #print("you won")
        #print("[Y] [N]")
        #retry = ("do you want to retry >> ")
        #if retry == Y:
            #pass
        #else : 
            #quit()
        
