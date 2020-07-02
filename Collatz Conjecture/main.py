#Pick any number. If that number is even, divide it by 2. If it's odd, multiply it by 
# 3 and add 1. Now repeat the process with your new number. If you keep going, you'll 
# eventually end up at 1. Every time.

def main():
    num = 1
    original_num = 1
    while True:
        while True:
            if(num%2)==0:  
                num = num / 2
            else:
                num = num * 3 + 1
        if num != 1:
            print("not 1 detected the number " + str(original_num))
    print(str(original_num))
    num += 1
    original_num += 1
        


if __name__ == "__main__":
    main()