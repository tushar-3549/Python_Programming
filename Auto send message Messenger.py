import pyautogui
import time
message = 10
while message > 0:
    time.sleep(4)
    pyautogui.typewrite("Hi , Toma . I am Tushar")
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1
