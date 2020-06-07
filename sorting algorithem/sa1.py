#l = [2,3,2,5,3,7,4]
#a = 0
#b = 1

#z = 0
#x = 1

#def swapPositions(l, a, b): 
    #l[a],l[b] = l[b],l[a] 

#for i in range(0,6):
	#aa = l[a]
	#bb = l[b]
	#if aa > bb:
		#swapPositions(l, a, b)
		#a = a + 1
		#b = b + 1
	#else:
		#a = a + 1
		#b = b + 1

#for i in range(0,6):
	#zz = l[z]
	#xx = l[x]
	#if zz > xx:
		#swapPositions(l, z, x)
		#z = z + 1
		#x = x + 1
	#else:
		#z = z + 1
		#x = x + 1
#print(l)

#l = [1,3,2,4,9,3,4,1,1]



#def when_start():
#	for i in range(0,8):
#		a = 0
#		b = 1
#		for x in range(0,8):
#			if l[a] > l[b]:
#				l[a],l[b] = l[b],l[a]
#			a = a+1
#			b = b+1
#	print(l)

#when_start()

from time import sleep
from os import system



def when_start(): 
	c = 0
	d = 0
	e = 5
	l = [1,5,2,4,7,8,9,1,4]
	for i in range(0,5):
		print("staring in " + str(e))
		sleep(1)
		e = e - 1
		if e == 0:
			system("Cls")
			break
	for i in range(0,8):
		a =0 
		b =1
		for i in range(0,8):
			if l[a] > l[b]:
				# change a and b
				l[a],l[b] = l[b],l[a]
			a = a + 1
			b = b + 1
	f = 0
	for i in range(0,9):
		print(l[f])
		sleep(2)
		system("cls")

		f = f + 1
when_start()

