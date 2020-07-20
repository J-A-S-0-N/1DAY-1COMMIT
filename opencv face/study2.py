import cv2
from os import system
from time import sleep
import numpy as np
import subprocess

face_cascade = cv2.CascadeClassifier('C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\opencv face\\cascades\\data\haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

break1 = False

while True:
    if break1 == True:
        break
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        break1 = True
        break
        #img_item = "face-image.png"
        #cv2.imwrite(img_item, roi_color)

        #color = (255, 0, 0)
        #stroke = 2
        #end_cord_x = x + w
        #end_cord_y = y + h
        #cv2.rectangle(frame, (x,y),(end_cord_x, end_cord_y),color,stroke)
        
    #cv2.imshow('main frame', frame)
        
cap.release()
cv2.destroyAllWindows()

subprocess.call(["C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\opencv face\\dist\\when_started.exe"])
