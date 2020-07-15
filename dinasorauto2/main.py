import pyautogui
import sys, os
from PIL import Image

# change directory for saveing the screen shots just incase someting goes wrong
os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\dinasorauto\\screenshots")

#y_c is the same for all except the flying objects
y_c = 340

#most far from trex
x_c1 = 400

#in between 
#x_c2 = 330

#x_c3 is the closes from the trex
x_c3 = 308

#the background color
bg_color = 247

def processing_img1():
    #loading the image that python will take with pyautogui
    im = Image.open("trex_sh.jpg")
    pix = im.load()
    #print("cactus finder1 : " + str(pix[x_c1,y_c]))
    # the rgb color of the positon x_c1 and y_c
    pixlist = list(pix[x_c1, y_c])
    #save the first vartible from the tuple which will compair later 
    global a_pix
    a_pix = pixlist[0]

    #pix2 = im.load()
    #print("cactus finder2 : " + str(pix2[x_c2,y_c]))
    #pixlist2 = list(pix2[x_c2, y_c])
    #global a_pix2
    #a_pix2 = pixlist2[0]
    pix3 = im.load()
    #print("cactus finder3 : " + str(pix3[x_c3, y_c]))
    pixlist3 = list(pix3[x_c3, y_c])
    global a_pix3
    a_pix3 = pixlist3[0]



def main():
    while True:
        #take the screnshot and save it as "trex_sh.jpg"
        sh1 = pyautogui.screenshot()
        sh1.save("trex_sh.jpg")
        #print("screenshot taken")

        #run the processing_img def 
        processing_img2()

        #press space if the a_pix3, a_pix2 or a_pix is not equal to the color of the background which is 247 
        if a_pix3 != bg_color:
            pyautogui.press("up")
        if a_pix != bg_color:
            pyautogui.press("up")
        #if a_pix2 != bg_color:
        #    pyautogui.keyUp("up")
        #    pyautogui.keyDown("up")
            
            
# runing the main loop
if __name__ == "__main__":
    main()