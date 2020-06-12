from os import system
words = ["the", "at",	"there", "some", "my", "of", "be", "use", 'her', 'than', 'and', 'this' ,'an', 'would', 'first', "a", 'have', 'each', 'make', 'water' ,'to' ,'from', 'which', 'like', 'been', 'in', 'or', 'she', 'him', 'call', 'is', 'one', 'do', 'into', 'who',"you" ,'had', 'how', 'time', "oil", "that" ,"by" ,"their", "has", "its", "it", "word",	"if", "look" ,"now", "he", "but", "will" ,"two", "find", "was", "not", "up", "ore", "long", "for", "what", "other", "write", "down", "on", "all", "about", "go", "day", "are",	 "were" ,"out", "see", "did", "as", 'we', "many", "number", "get", "with", "when", "then", "no", "come", "his", "your", "them", "way", "made", "they", "can", "these", "could", "may", "I", "said", "so", "people", "part"]
import os

wrong = 0

while True:
	a = 0
	for i in range(0,100):
		print(words[a])
		enter = input("> ")
		if enter == words[a]:
			print("correct next")
			a += 1
			system("cls")
		else:
			wrong += 1
		if wrong == 9:
			print("you go 9 wrong game over")
			exit()