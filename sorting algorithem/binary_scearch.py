l = [1,2,3,4,5,6,7,8,9,10,11]
targestr = input("target : ")
midpoint = 6
targe = int(targestr)


if targe == midpoint:
	print("the targe is " + str(midpoint))
if targe < midpoint:
	l_Left = [l[0],l[1],l[2],l[3],l[4]]
	print(l_Left)
	midpoint_left = l_Left[2]
	if targe < midpoint:
		if targe == l_Left[0]:
			print("the target is " + str(l_Left[0]))
		else:
			print("the target is " + str(l_Left[1]))
	elif midpoint_left == 3:
		print("the target is " + str(l_Left[2]))
	elif targe > midpoint:
		if targe == l_Left[3]:
			print("the target is " + str(l_Left[3]))
		else:
			print("the target is " + str(l_Left[4]))
	


if targe > midpoint:
	l_right = [l[6],l[7],l[8],l[9],l[10]]	
	print(l_right)
	midpoint2 = l_right[2]
	if targe < midpoint2 :
		if targe == l_right[0]:
			print("the target is " + str(l_right[0]))
		else:
			print("the taget is " + str(l_right[1]))
	elif targe > midpoint2:
		if targe == l_right[3]:
			print("the target is " + str(l_right[3]))
		else:
			print("the target is " + str(l_right[4]))
	elif targe == 9:
		print("the target is " + str(l_right[2]))