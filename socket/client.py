from socket import *

HOST = 'localhost'
PORT = 21597
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcs = socket(AF_INET, SOCK_STREAM)
tcs.connect(ADDR)

while True:
    data = raw_input(">> ")
    if not data:
        break
    tcs.send(data)
    data = tcs.recv(BUFSIZ)
    if not data:
        break
    print(data)
tcs.close()
