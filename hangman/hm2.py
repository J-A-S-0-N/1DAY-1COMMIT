import random
from os import system
from time import sleep

trys = 10

def end():
	a = 10
	for i in range(0,10):
		print("closing in " + str(a))
		a = a - 1
		sleep(1)
		system("cls")
		if a == 0:
			quit()

def main():
	trys = 10
	w0 = False
	w1 = False
	w2 = False
	w3 = False
	w4 = False

	w = "hello"
	word = ["h","e","l","l","o"]
	blank = ["_","_","_","_","_"]
	while True:
		if trys == 0:
			system("cls"
			print("sorry you got wrong more than 5 trys")
			sleep(2)
			system("cls")
			end()
		system("cls")
		print(blank)
		if w0 == True and w1 == True and w2 == True and w3 == True and w4 == True:
			system("cls")
			print("nice the word was " + '"' + w + '"')
			sleep(4)
			system("cls")
			end()
		print(str(trys)+ " trys left")
		inp = input("enter > ")
		if inp == "quit":
			quit()
		if inp == word[0]:
			blank[0] = word[0]
			w0 = True
		elif inp == word[1]:
			blank[1] = word[1]
			w1 = True
		elif inp == word[2]:
			blank[2] = word[2]
			w2 = True
			blank[3] = word[3]
			w3 = True
		elif inp == word[4]:
			blank[4] = word[4]
			w4 = True
		else:
			trys = trys - 1
if __name__ == '__main__':
	main()