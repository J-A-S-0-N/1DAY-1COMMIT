from time import sleep
from os import system
from  textmagic.rest import TextmagicRestClient
import os

os.chdir("C:\\Users\\jason\\Desktop\\o\\other\\python\\python\\else\\notifier")

username = "notifier"
#token = 
phone = "18560450065"
main_file = open("noti.txt", "w+")
def end(time):
	while True:
		print(str(time))
		time -= 1
		if time == 0:
			system("cls")
			quit()
u
def main():
	print("this is an notifier app")
	print("add[1] del[2] remind[3]")
	inp = input(">>> ")
	if inp == "1":
		while True:
			system("cls")
			print("add")
			print("name")
			add1 = input(">>> ")
			print("time")
			print("ex : 12,10")
			add2 = input(">>> ")
			print("are you sure : name : " + add1 + " time : " + add2)
			print("yes[y] no[n]")
			add3 = input(">>> ")
			if add3 == "y":
					main_file.write(add1+ " " +add2)
					break
			elif add3 == "n":
					pass
			else:
				print("retry")
				sleep(3)
				system("Cls")
	if inp == "2":
		data = main_file.readline()
		print(data)


if __name__ == '__main__':
	main()