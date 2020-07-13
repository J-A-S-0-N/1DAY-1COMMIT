import itchat
import random
import sys


chatname = ""

def ran():
    global temp
    temp = random.radint(0,7)

def time():
    time = ctime()
    time = list(time)
    htime = str(time[11]) + str(time[12])
    daytime = str(time[0]) + str(time[1]) + str(time[2])



def main():
    while True:
        if htime == "09":
            if datetime == "Sat":
                itchat.auto_login()
                author = itchat.search_friends(nickName=chatname)
                ran()
                author.send('채준성 36.' + str(temp))
            if datetime == "Sun":
                itchat.auto_login()
                author = itchat.search_friends(nickName=chatname)
                ran()
                author.send('채준성 36.' + str(temp))

if __name__ == "__main__":
    main()