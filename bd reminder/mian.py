import time
import os
from time import sleep
from smtplib import SMTP
import smtplib
import ssl


os.chdir("C:\\Users\\jason\\Desktop\\o\\other\\python\\python\\else\\birthday reminder")

def time():
	from datetime import date
	today = date.today()
	tim = today.strftime("%m,%d")
	tim.split(",")
	mon = tim[1]
	day = tim[4]
	print(mon)
	print(day)

def email():
	port = 465
	bd = open("bd.txt", "r+")
	print("enter the password for the email")
	password = input(">>> ")
	context = ssl.create_default_context()
	sender_email = 
	reciver_email = 
	message = """\
	dear : reciver

	happy birthday 

	wish you luck
	from : Jason
	"""

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
		server.login(, password)
		#send email
		server.sendmail(sender_email, reciver_email, message)

def end(time):
	while True:
		print(time)
		sleep(1)
		time -= 1
		if time == 0:
			system("cls")

def main():
	#opening file
	file_obj = open("bd.txt", "r+")

	i1 = input("birthday[1] birthday check[2]")
	if i1 == "1":
		print("enter the month")
		mon_inp = input(">>> ")
		print("enter the day")
		day_inp = input(">>> ")
		file_obj.write()
		file_obj.write()
		end(3)
	elif i1 == "2":
		#send email
		email()
		time()



if __name__ == '__main__':
	#main()
	time()
