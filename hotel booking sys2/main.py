#all imports 
from keyboard import *
from os import system
from time import sleep


#rooms that are in the hotel 
rooms = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40]

#rooms that you can pay
avaleble_rooms1 = [1,2,3,4,5,6,7,8,9]
avaleble_rooms2 = [11,12,13,14,15,16,17,18,19]
avaleble_rooms3 = [21,22,23,24,25,26,27,28,29]

def timer(time):
	while True:
		print(time)
		time = time - 1
		sleep(1)
		if time == 0:
			system("cls")
			break

def main():
	r1 = 1
	r2 = 11
	r3 = 21
	print("hello this is the 'name' hotel")
	print("wellcome")
	timer(3)

	print("please enter what floor you want to be in.")
	if keyboard.is_pressed('1'):
		print(avaleble_rooms1)	
		print("this are avaleble")
		timer(10)
		system("Cls")
		print("please slect one")
		print(avaleble_rooms1)
	while True:
			if keyborad.is_pressed(str(r1)):
				Print("ok")
				avaleble_rooms1[r1] = "used"
				break
			else:
				pass
			r1 = r1 + 1	
		
if __name__ == '__main__':
	main()