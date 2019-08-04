# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:46:15 2018

@author: User
"""
import pyautogui 

pyautogui.FAIL_SAFE = True
pyautogui.PAUSE = 1  

# size cua man hinh
height,width = pyautogui.size()
# vi tri hien tai cua chuot
position = pyautogui.position()
#di chuyen chuot toi
pyautogui.moveTo(300,400)

pyautogui.moveTo(250,110)
pyautogui.click(x=250, y=110, clicks=1, interval=0, button='left')
pyautogui.click(x=350, y=110, clicks=1, interval=0, button='right')

pyautogui.click(x=250, y=690, clicks=1, interval=0, button='left')

keys = "hhh"
pyautogui.press(keys, presses=1, interval=0.0, pause=None, _pause=True)



from pynput.keyboard import Key, Controller


