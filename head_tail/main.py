import random

def main():
    tail = 0
    head = 0
    head_tail = ["head", "tail"]
    print("how many coin tos do you want?")
    c = input(">>> ")
    c = int(c)
    for i in range(0, c):
        ran = random.choice(head_tail)
        print(ran)
        if ran == head_tail[0]:
            head += 1
        if ran == head_tail[1]:
            tail += 1
    print("head : " + str(head))
    print("\n" * 4)
    print("tail : " + str(tail))
    sum_head = head / int(c) * 100
    sum_tail = head / int(c) * 100
    print("\n" * 4) 
    print("head percentage : " + str(sum_head))
    print("\n" * 4)
    print("tail percentage : " + str(sum_tail))

            

        

    
    


if __name__ == "__main__":
    main()