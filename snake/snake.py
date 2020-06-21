import random
import keyboard
from os import system
from time import sleep
#grid is 10x10

tf = 10

for i in range(0,10):
	print("'w' is up")
	print("'s' is down")
	print("'a' is left")
	print("'d' is right")
	print("closing in " + str(tf))
	tf = tf -1
	sleep(1)
	system("cls")
	if tf == 0:
		print("game start")
		sleep(4)
		system("cls")
		break

list = ["fasf"]

g1 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g2 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g3 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g4 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g5 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g6 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g7 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g8 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g9 = ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]
g10= ["[", " _", " _", " _", " _", " _", " _", " _", " _", " _", " _", " ]"]


	
def gridprint():
	print(g1)
	print(g2)
	print(g3)
	print(g4)	
	print(g5)
	print(g6)
	print(g7)
	print(g8)
	print(g9)
	print(g10)
	
def keyboardpress():
	if keyboard.is_pressed("w"):
		pass
def movement_changedir():
	pass
def applegen():
	apr = random.randint(0,9)
	apc = random.randint(0,9)
	print(apr)
	print(apc)

g6[5] = " X" 

gridprint()
while True:
	pass

