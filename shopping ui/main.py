import keyboard
from os import system
import os
from time import sleep 

# "*" this means its important

def main():
	# change the directory because the "admin pw.txt"
	os.chdir("C:\\Users\\jason\\Desktop\\o\\other\\python\\python\\else\\shopping ui")

	#opening file
	file_obj = open("admin pw.txt", "r+")

	
	# the list for the items
	obj = []

	# the list for the amount
	amo = []
	# the list for the amount *the list "obj" and the "amo" will be parelle to each other
	
	# used for breaking the loop
	b1 = False
	
	print("*if you are the admin please press '0'")
	print("otherwise please press '1'")
	admin_or_user = input(">>> ")

	# admin
	if admin_or_user == "0":
		print("enter password")
		pw_admin = input(">> ")
		pw = file_obj.readline()
		pw = str(pw)
		while True:
			if b1 == True:
				break		
			if pw == pw_admin:
				print("welcome")
				print("wait for 4 seccond")
				sleep(4)
				system("cls")
				print("add_item[1] delete_item[2]")
				admin1 = input(">>> ")
				while True:
					# adding item
					if admin1 == "1":
						system("Cls")
						print("adding")
						print("item name")
						admin_itemname1 = input(">>> ")
						print("amount")
						admin_amount1 = input(">>> ")
						print("agian? yes[y] no[n]")
						breakyn1 = input(">>> ") 
						if breakyn1 == "y":
							system("Cls")
						elif breakyn1 == "n":
							system("cls")
							b1 = True
							break 
					# delteing item
					elif admin1 == "1":
						system("Cls")
						print("delete")
			else:
				print("the password is wrong exiting for safty reason")
				# ring the alarm for the it apartment somthing like that
				# close the surver
				sleep(3)
				quit()

	# user 
	if admin_or_user == "1":
		print("hello please enter what you want")


if __name__ == '__main__':
	main()