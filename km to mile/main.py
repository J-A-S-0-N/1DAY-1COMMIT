def coversion(num):
    one_km = 1.609344
    sum = num * one_km
    return sum
    

def main():
    print("enter km")
    global inp
    inp = input(">>> ")
    inp = int(inp)
    sum = coversion(inp)
    print(sum)


if __name__ == "__main__":
    main()