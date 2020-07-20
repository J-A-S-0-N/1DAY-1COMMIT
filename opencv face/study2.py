import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\opencv study\\cascades\\data\haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        
        
    cv2.imshow('main frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.distroyAllWindows()