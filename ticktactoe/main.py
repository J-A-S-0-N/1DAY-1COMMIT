import random
import keyboard
from time import sleep
from os import system
import sys

gr1 = ["_ ", "_ ", "_ "]
gr2 = ["_ ", "_" , "_ "]
gr3 = ["_ ", "_ ", "_ "]

#gr1
g1a = False
g1b = False
g1c = False

#gr2 
g2a = False 
g2b = False
g2c = False

#gr3
g3a = False
g3b = False 
g3c = False

r0c0 = "a"
r0c1 = "a"
r0c2 = "a"
r1c0 = "a"
r1c1 = "a"
r2c2 = "a"
r2c0 = "a"
r2c1 = "a"
r2c2 = "a"

c1 = [0,1,2]
c2 = [0,1,2]


def row_check():# call later
	if r0c0 == "u" and r0c1 == "u" and r0c2 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)
	if r0c0 == "u" and r1c0 == "u" and r2c0 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)
	if r2c0 == "u" and r2c1 == "u" and r2c2 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)
	if r0c2 == "u" and r1c2 == "u" and r2c2 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)
	if r0c1 == "u" and r1c1 == "u" and r2c1 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)
	if r1c0 == "u" and r1c1 == "u" and r1c2 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)
	if r0c0 == "u" and r1c1 == "u" and r2c2 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)
	if r0c2 == "u" and r1c1 == "u" and r2c0 == "u":
		t = 10
		for i in range(0,10):
			print("nice you won")
			print("closing in " + str(t))
			t = t - 1
			sleep(1)
			system("cls")
			if t == 0:
				sys.exit(0)

	
	



def ai():
	global g1a
	global g1b
	global g1c

	global g2a
	global g2b
	global g2c

	global g3a
	global g3b
	global g3c

	cc1 = str(random.choice(c1))
	cc2 = str(random.choice(c2))
	# cc1 is the row
	# cc2 is collem
	ai1 = cc1 + cc2
	ail = list(ai1)
	row = ail[0]
	collem = ail[1]
	row = int(row)
	collem = int(collem)
	#first row
	if row == 0 and collem == 0 and g1a == False:
		sleep(0.2)
		gr1[0] = "X "
		print(gr1)
		print(gr2)
		print(gr3)
		g1a = True
		r0c0 = "a"
	else:
		pass
	if row == 0 and collem == 1 and g1b == False:
		sleep(0.2)
		gr1[1] = "X " 
		print(gr1)
		print(gr2)
		print(gr3)

		g1b = True
		r0c1 = "a"
	else:
		pass
	if row == 0 and collem == 2 and g1c == False:
		sleep(0.2)
		gr1[2] = "X "
		print(gr1)
		print(gr2)
		print(gr3)
		g1c = True
		r0c2 = "a"
	else:
		pass

	#seccond row
	if row == 1 and collem == 0 and g2a == False:
		sleep(0.2)
		gr2[0] = "X "
		print(gr1)
		print(gr2)
		print(gr3)
		g1c = True
		r1c0 = "a"
	else:
		pass
	if row == 1 and collem == 1 and g2b == False:
		sleep(0.2)
		gr2[1] = "X "
		print(gr1)
		print(gr2)
		print(gr3)
		g1c = True
		r1c1 = "a"
	else:
		pass
	if row == 1 and collem == 2 and g2c == False:
		sleep(0.2)
		gr2[2] = "X "
		print(gr1)
		print(gr2)
		print(gr3)
		g1c = True
		r1c2 = "a"
	else:
		pass
	#third row
	if row == 2 and collem == 0 and g3a == False:
		sleep(0.2)
		gr3[0] = "X "
		print(gr1)
		print(gr2)
		print(gr3)
		g1c = True
		r2c0 = "a"
	else:
		pass
	if row == 2 and collem == 1 and g3b == False:
		sleep(0.2)
		gr3[1] = "X "
		print(gr1)
		print(gr2)
		print(gr3)
		g1c = True
		r2c1 = "a"
	else:
		pass
	if row == 2 and collem == 2 and g3b == False:
		sleep(0.2)
		gr3[2] = "X "
		print(gr1)
		print(gr2)	
		print(gr3)
		g1c = True
		r2c2 = "a"
	else:
		pass



while True:
	print("you are O the ai is X")
	print("enter")
	sleep(0.2)
	ai()
	row_check()
	while True:
		#line 1
		if keyboard.is_pressed("q") and g1a == False:
			sleep(0.2)
			gr1[0] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g1a = True
			r0c0 = "u"
			row_check()
			break
		if keyboard.is_pressed("w") and g1b == False:
			sleep(0.2)
			gr1[1] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g1b = True
			r0c1 = "u"
			row_check()
			break
		if keyboard.is_pressed("e") and g1c == False:
			sleep(0.2)
			gr1[2] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g1c = True
			r0c2 = "u"
			row_check()
			break


		#line 2
		if keyboard.is_pressed("a") and g2a == False:
			sleep(0.2)
			gr2[0] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g2a = True
			r1c0 = "u"
			row_check()
			break
		if keyboard.is_pressed("s") and g2b == False:
			sleep(0.2)
			gr2[1] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g2b = True
			r1c1 = "u"
			row_check()
			break
		if keyboard.is_pressed("d") and g2c == False:
			sleep(0.2)
			gr2[2] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g2c = True
			r1c2 = "u"
			row_check()
			break

		#line 3
		if keyboard.is_pressed("z") and g3a == False:
			sleep(0.2)
			gr3[0] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g3a = True
			r2c0 = "u"
			row_check()
			break	
		if keyboard.is_pressed("x") and g3b == False:
			sleep(0.2)
			gr3[1] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g3b = True
			r2c1 = "u"
			row_check()
			break
		if keyboard.is_pressed("c") and g3c == False:
			sleep(0.2)
			gr3[2] = "O "
			print(gr1)
			print(gr2)
			print(gr3)
			g3c = True
			r2c2 = "u"
			row_check()
			break