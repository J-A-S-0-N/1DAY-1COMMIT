def coversion(num):
    one_kg = 2.20462262185
    sum = num * one_kg
    return sum
    

def main():
    print("enter gm")
    global inp
    inp = input(">>> ")
    inp = int(inp)
    sum = coversion(inp)
    print(sum)


if __name__ == "__main__":
    main()