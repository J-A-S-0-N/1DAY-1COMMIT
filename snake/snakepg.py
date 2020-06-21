import pygame 
from time import sleep
import random
from os import system

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("snake")

x = 250
y = 250 #- 15
width = 20
hight = 20
vel = 5
white =(255, 255,255)

rx = 0
ry = 0

l = [0,40,80,120,160,200,240,280,320,360,400,440,480]

a1 = random.choice(l)
b1 = random.choice(l)

ab1 = True

a2 = random.choice(l)
b2 = random.choice(l)
ab2 = True

a3 = random.choice(l)
b3 = random.choice(l)

ab3 = True

a4 = random.choice(l)
b4 = random.choice(l)

ab4 = True

a5 = random.choice(l)
b5 = random.choice(l)

ab5 = True

a6 = random.choice(l)
b6 = random.choice(l)

ab6 = True

t1 = a1 <= 20
g1 = b1 <= 20

t2 = a2 <= 20
g2 = b2 <= 20
	
t3 = a3 <= 20
g3 = b3 <= 20
	
t4 = a4 <= 20
g4 = b4 <= 20

t5 = a5 <= 20
g5 = b5 <= 20

t6 = a6 <= 20
g6 = b6 <= 20


def eat():
	if x == t1 or x == t1 - 10 or y == g1 or y == g1 - 10:
		while True:
			print("nice")
	if x == t2  or y == g2:
		while True:
			print("nice")
	if x == t3  or y == g3:
		while True:
			print("nice")
	if x == t4  or y == g4:
		while True:
			print("nice")
	if x == t5 or y == g5:
		while True:
			print("nice")
	if x == t6 or y == g6:
		while True:
			print("nice") 

def printa():
	print(a1)
	print(b1)
	print("")
	print(a2)
	print(b2)
	print("")
	print(a3)	
	print(b3) 
	print("")
	print(a4)
	print(b4)
	print("")
	print(a5)
	print(b5)
	print("")
	print(a6)
	print(b6)
	print("")



run = True
while run:
	pygame.time.delay(200)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	check = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and check == False:
		x -= vel + 16
		check = True
	if keys[pygame.K_RIGHT] and check == False:
		x += vel + 16
		check = True
	if keys[pygame.K_UP] and check == False:
		y -= vel + 16
		check = True
	if keys[pygame.K_DOWN] and check == False:
		y += vel + 16
		check = True
	print("apple corrd")
	printa()
	print("")
	print("your corrd")
	print(x)
	print(y)
	print("")
	system("cls")
	win.fill((0,0,0))
	
	eat()

	pygame.draw.rect(win,(255, 0,0),(a1,b1,width, hight))

	pygame.draw.rect(win,(255, 0,0),(a2,b2,width, hight))

	pygame.draw.rect(win,(255, 0,0),(a3,b3,width, hight))

	pygame.draw.rect(win,(255, 0,0),(a4,b4,width, hight))

	pygame.draw.rect(win,(255, 0,0),(a5,b5,width, hight))

	pygame.draw.rect(win,(255, 0,0),(a6,b6,width, hight))
	
	pygame.draw.rect(win, (0, 250,0),(x ,y, width, hight))

	pygame.display.update()
pygame.quit()