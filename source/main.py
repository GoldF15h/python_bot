from pyautogui import click
from pyautogui import screenshot as sc
from numpy import array
from cv2 import cvtColor,COLOR_RGB2GRAY,destroyAllWindows
from keyboard import is_pressed
from os import system

# game use in this porject
# https://poki.com/th/g/piano-tiles-2
# Top Left      609   ,  120
# Bottom Right  1021  ,  883
# SIZE ->       775   X  413
# old setting (473,0,-50)
def black_scan_click (screenshot,y_cord,time):
        # scan for black color
        for x in range(649,0,-50) :
            for y in y_cord :
                # if color is black
                if screenshot[x,y] < 10 :
                    click(609+y,109+x+time/5)
                    return

if __name__ == "__main__" :
    system('cls')
    print("BOT IS STANDBY \nPRESS 'P' TO START")
    
    # defind what x coordinate value we need to check
    y_cord = [50,150,250,350]

    # stand by
    while not is_pressed('p') :
       pass
    
    system('cls')
    print("BOT IS RUNNING")

    # how many time we click
    time = 0

    # start
    while not is_pressed('esc') :
        # take Screenshot
        screenshot = sc(region=(609,120, 413, 650))
        
        # convert screenshot to CV2 tpye
        screenshot = array(screenshot)
        screenshot = cvtColor(screenshot,COLOR_RGB2GRAY)

        # find tiles and click on it
        black_scan_click(screenshot,y_cord,time)
        time = time + 1
    
        # show image pfor debug
        # cv2.imshow('capture',screenshot) 
        # if cv2.waitKey(1) == ord('q'):
        #     break


    # end of the program
    destroyAllWindows
    system('cls')
    print("STOP!")