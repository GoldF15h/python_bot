import pyautogui
import time
import numpy as np
import cv2
import keyboard
import os

if __name__ == "__main__" :
    os.system('cls')
    print("BOT IS RUNNING")

    while not keyboard.is_pressed('esc') :
        # take Screenshot
        screenshot = pyautogui.screenshot()
        
        # convert screenshot to CV2 tpye
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
        # show image for debug
        cv2.imshow('capture',screenshot) 
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows
            break

        # time.sleep(2)
