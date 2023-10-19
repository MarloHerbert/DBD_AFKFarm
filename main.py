# -*- coding: utf-8 -*-

import pyautogui
import random
import time
import subprocess
import keyboard
import findMainWindow

def SetWindowForeground():
    #script_path = "findMainWindow.py"
    #output = subprocess.check_output(['python', script_path], text=True)
    #print(output)
    findMainWindow.GetDBDWindow()
    

def ClickONPlay(x= 1775, y= 917):
    SetWindowForeground()
    pyautogui.click(x, y)
    
def ClickONContinue(x=1775, y=1026):
    SetWindowForeground()
    pyautogui.click(x, y)
    
def ClickONPlayKiller(x=333, y=162):
    SetWindowForeground()
    pyautogui.click(x, y)
    
def ProceedGame():
    ClickONPlayKiller();
    ClickONPlay();
    ClickONContinue();

def holdKey(key= "w", duration = 0.45):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)
    
def DoRandomMovement():
    SetWindowForeground()
    actions = ["w", "a", "d", "mouse1"]
    # Number of random actions to perform

    action = random.choice(actions)  # Choose a random action
    if action == "w":
        holdKey("w")
    elif action == "a":
        holdKey("a")  # Simulate pressing the "A" key
    elif action == "d":
        holdKey("d")  # Simulate pressing the "D" key
    elif action == "mouse1":
        pyautogui.click()  # Simulate a left mouse button click

    
if __name__ == "__main__":
    counter = 0;
    limit = 6
    while(True):
        counter = counter + 1;
        if(counter == limit):
            ProceedGame();
            counter = counter - limit;
        else:
            DoRandomMovement();
        if keyboard.is_pressed('esc'):
            break;
        



