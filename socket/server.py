from socket import *
from time import ctime

HOST = ""
PORT = 21597
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcs = socket(AF_INET, SOCK_STREAM)
tcs.bind(ADDR)
tcs.listen(5)

while True:
    print("wating for connection...")
    tcs, ADDR = tcs.accept()
    print("...conneted from " + ADDR)

    while True:
        data = tcs.recv(BUFSIZ)
        if not data:
            break
        tcs.send([%s] %s % (bytes(ctime(), 'utf-8'), data))
    tcs.close()