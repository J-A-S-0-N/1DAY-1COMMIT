def add(a1, a2):
	return int(a1) + int(a2)
def sub(s1, s2):
	return int(s1) - int(s2)
def mul(m1, m2):
	return int(m1) * int(m2)
def dev(d1, d2):
	return int(d1) / int(d2)
while True:
	print("slect one")
	print("add[a] subtract[s] multiply[m] devide[d]")
	sle = input(">> ")
	if sle == "a":
		print("enter the number")
		a3 = input("1st >> ")
		a4 = input("2nd >> ")
		addanswer = add(a3,a4)
		print(addanswer)
	elif sle == "s":
		print("enter the number")
		s3 = input("1st >> ")
		s4 = input("2nd >> ")
		subanswer = sub(s3,s4)
		print(subanswer)
	elif sle == "m":
		print("enter the number")
		m3 = input("1st >> ")
		m4 = input("2nd >> ")
		mulanswer = mul(m3,m4)
		print(mulanswer)
	elif sle == "d":
		print("enter the number")
		d3 = input("1st >> ")
		d4 = input("2nd >> ")
		devanswer = dev(d3,d4)
		print(devanswer)
