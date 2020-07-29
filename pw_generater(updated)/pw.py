import random 
from time import sleep


PASS = []
wordlo = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
wordup = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
wordnum = ["1","2","3","4","5","6","7","8","9"]
namelist= ["wordlo", "wordup", "wordnum"]

def main():
	word_count = input("how many letter? >> ")
	for i in range(0, int(word_count)):
		rand1 = random.choice(namelist)
		if rand1 == "wordlo":
			rand2 = random.choice(wordlo)
			PASS.append(rand2)
		if rand1 == "wordup":
			rand2 = random.choice(wordup)
			PASS.append(rand2)
		if rand1 == "wordnum":
			rand2 = random.choice(wordnum)
			PASS.append(rand2)	
	print("".join(PASS))


if __name__ == '__main__':
	main()