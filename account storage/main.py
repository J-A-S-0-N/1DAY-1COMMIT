import os
from os import system
from time import sleep

os.chdir("C:\\Users\\jason\\Desktop\\o\\other\\python\\python\\else\\account storage")
def main():
	# later used for breaking the loop
	b2 = False
	#open file
	file_obj = open("account.txt", "r+")
	while True:
		print("login[1] or signup[2]")
		sl = input("enter >> ")
		if sl == "2":	
			print("email")
			email = input(">> ")
			print("password")
			pas = input(">> ")
			print("name")
			name = input(">> ")
			#write the input in this format
			#"email:abc password:abc"
			file_obj.write(email + " , ")
			file_obj.write(pas + " , ")
			file_obj.write(name)
			e_p_n = file_obj.readline()
			em,pa,na = e_p_n.split(" , ")

		elif sl == "1":
			#used for breaking the loop 
			if b2 == True:
				break
			while True:
				print("enter email")
				email = input(">> ")
				print("password")
				pas = input(">> ")
				# cut the unaccesery part to compair with the email and the password
				print(em)
				print(pa)
				print(na)
				#compairing the em,oa with email and pas
				if em == email and pa == pas:
					print("wellcome " + name)
					b2 = True
					break
				else:
					print("retry")
					sleep(2)
		else:
			print("error please enter 1 or 2")
if __name__ == '__main__':
	main()