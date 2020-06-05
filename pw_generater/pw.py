import random 
from time import sleep



wordlo = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
wordup = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
wordnum = ["1","2","3","4","5","6","7","8","9"]

def main():
	word_count = input("how many letter? >> ")
	word_count = int(word_count)
	
	a = 1
	while True:
		if a - 1 == word_count:
			print("this is the password")
			sleep(3)
			break
		ch = random.randint(0,2)
		if ch == 0:
			ran = random.randint(0,25)
			print(wordlo[ran])
		elif ch == 1:
			ran = random.randint(0,25)
			print(wordup[ran])
		elif ch == 2:
			ran = random.randint(0,8)
			print(wordnum[ran])
		a = a + 1
if __name__ == '__main__':
	main()