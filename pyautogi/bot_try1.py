import pyautogui
import keyboard

x = 960

def enter():
    pyautogui.moveTo(x, 300)
    pyautogui.click()


while True:
    if keyboard.is_pressed('enter'):
        enter()
        
    