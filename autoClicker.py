import keyboard
import mouse
import pyautogui
import time

screenwidth, screenheight = pyautogui.size()
# while not keyboard.is_pressed('escape'):
keyboard.wait('space')
print('clicking started on the middle of the screen')
pyautogui.moveTo(screenwidth / 2, screenheight / 2)
while not keyboard.is_pressed('space'):
    # pyautogui.click()
    mouse.click(button='left')
    time.sleep(0.001)
