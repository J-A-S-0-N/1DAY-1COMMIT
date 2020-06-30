number = input("enter the number >> ")

def DecimalToBinary(num): 
    num = int(num)
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
  

def BinaryReversal(num):
    #main open
    DecimalToBinary(num)

# keep this function call here 
print (BinaryReversal(number))