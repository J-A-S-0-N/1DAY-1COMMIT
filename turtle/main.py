import turtle
import random
from time import sleep
import keyboard

def speed():
    global t1speed
    t1speed = random.randint(100, 300)
    global t2speed
    t2speed = random.randint(100, 300)
    global t3speed
    t3speed = random.randint(100, 300)

def main():
    s = turtle.getscreen()
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("red")
    t2 = turtle.Turtle()
    t2.shape("turtle")
    t2.color("blue")
    t3 = turtle.Turtle()
    t3.shape("turtle")
    t3.color("green")
    t1.penup()
    t2.penup()
    t3.penup()
    t1.goto(-100, 100)
    t2.goto(-100, 0)
    t3.goto(-100, -100)

    sleep(2)
    t1.goto(500,100)
    sleep(1)
    
    t2.goto(500, 0)
    sleep(2)
    
    t3.goto(500, -100)
    t1.speed(t1speed)
    t2.speed(t2speed)
    t3.speed(t3speed)
    s.mainloop()
    
    
    
        


if __name__ == "__main__":
    main()