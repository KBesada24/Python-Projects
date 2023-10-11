import pyautogui as pag
import random
import time
while True:
    x = random.randint(900,1500)
    y = random.randint(400,800)
    pag.moveTo(x,y,0.2)
    time.sleep(2)