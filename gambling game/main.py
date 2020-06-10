import random
from time import sleep
from os import system

def end(time):
	while True:
		print(str(time))
		time -= 1
		sleep(1)
		if time == 0:
			sleep(2)
			system("cls")
			print("end")
			sleep(3)
			quit()

def main():
	atmp = 0
	money = 200

	print("gambling game")
	print("every time you dont get right you get -10$")
	sleep(5)
	system("cls")
	while True:
		print("you have " + str(money) + "$")
		print("enter an number from 1 to 10")
		ran = random.randint(1,10)
		user = input(">>> ")
		atmp += 1
		money -= 10
		sleep(2)
		print("the answer number is ")
		sleep(2)
		print(str(ran))
		print("")
		print("you did " + str(atmp) + " atempts")
		print("")
		if int(user) == int(ran):
			sleep(2)
			system("Cls")
			print("nice you win")
			end(5)
		elif money == 0:
			sleep(2)
			system("Cls")
			print("you dont have enough money")
			end(5)


if __name__ == "__main__":
	main()