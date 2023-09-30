import pyautogui
import time
time.sleep(1)
def send():
    pyautogui.write("hello")
    pyautogui.press("enter")

x=0
# time.sleep(0.01)

while x<50:
    time.sleep(0.01)
    send()
   
