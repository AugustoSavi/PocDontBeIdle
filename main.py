from random import randint
import pyautogui, time

while True:
    x_init, y_init = pyautogui.position()
    time.sleep(3)
    x_after, y_after = pyautogui.position()
    if x_init == x_after and y_init == y_after: 
        pyautogui.moveTo(randint(x_init - 50, x_init + 50), randint(y_init - 50, y_init + 50), 1, pyautogui.easeOutQuad)