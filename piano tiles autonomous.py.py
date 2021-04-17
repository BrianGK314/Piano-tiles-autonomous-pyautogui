from pyautogui import*
import pyautogui
import random
import time
import win32api, win32con
import keyboard

#position 1 = X:  696 Y:  520 RGB: (  0,   0,   0)
#position 1 = X:  794 Y:  520 RGB: (  0,   0,   0)
#position 1 = X:  866 Y:  520 RGB: (  0,   0,   0)
#position 1 = X:  961 Y:  520 RGB: (  0,   0,   0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if (pyautogui.pixel(742,480)[0] in range(10)):
        click(742,480)
    if (pyautogui.pixel(888,480)[0] in range(10)):
        click(888,480)
    if (pyautogui.pixel(890,480)[0] in range(10)):
        click(890,480)
    if (pyautogui.pixel(1163,480)[0] in range(10)):
        click(1163,480)

        
