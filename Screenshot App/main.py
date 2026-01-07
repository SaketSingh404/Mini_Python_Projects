import time
import pyautogui

def screenshot():
    name = int(round(time.time()*100))
    name = '{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()