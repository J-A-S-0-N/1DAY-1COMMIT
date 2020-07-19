import random 
from os import system

answer = [" "," "," "," "," "," "]
words = ["hello", "bye", "python"]

def random_word_chooser():
    random_words = random.choice(words)
    return random_words

def main():
    checker = 0
    while True:
        random_words = random_word_chooser()
        random_words = list(random_words)
        while True:
            print(answer)
            print("guess")
            user_input = input(">>> ")
            random_word_list_lenght = len(random_words)
            for i in range(0,random_word_list_lenght):
                if user_input == random_words(checker):
                    answer[checker] = random_words[checker]
                    system("cls")
                    break
                checker += 1
                    





if __name__ == "__main__":
    main()