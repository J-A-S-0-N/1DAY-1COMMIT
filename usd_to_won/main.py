from tkinter import *
from tkinter.simpledialog import askstring


def execute(): 
    won = 1199
    sum = usd * won

def main():
    root = Tk()
    w = Label(root, text="Usd to Won\n") 
    global usd 
    usd = askstring("usd", "enter the amount.....", command=execute)
    enterbotten = Button(root, text="Enter", command=execute)
    w.pack()
    enterbotten.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()