import pyautogui as pg
import time
import sys
import cv2
import numpy as np


x, y = 1415, 837

def pres(x, y):
    pg.click(x, y)

class roundsys:
    def clockIn(roundsys):
        time.sleep(1)
        pres(x, y)
        time.sleep(0.3)
        pg.keyDown('shift')
        pg.press('tab')
        time.sleep(0.2)
        pg.press('n')
        time.sleep(0.2)
        pg.keyUp('shift')
        time.sleep(0.1)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('enter', 8, 0.4)
        print(f"{roundsys + 1} clock in/out's have been done")

    def clockOut(roundsys):
        time.sleep(2)
        pg.click(x, y)
        time.sleep(0.5)
        pg.click(x,  y)
        time.sleep(0.3)
        pg.keyDown('shift')
        pg.press('tab')
        time.sleep(0.2)
        pg.press('n')
        time.sleep(0.2)
        pg.keyUp('shift')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('enter', 6, 0.4)
        print(f"{roundsys + 1} clock in/out's have been done")

    def write(roundsys: str):
        writable_file = str(sys.argv[2]) + '.txt'
        with open(writable_file, 'w') as file:
            file.write(f"Total of {roundsys + 1} clock in/out's have been completed")          