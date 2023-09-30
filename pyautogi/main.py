import random
import pyautogui
import keyboard
import time

list1=("yavrum ","canim "," bebeğim ","canimm ")
list2=("sana ","her türlü "," "," sana " , "  sana ")

def enter():
    pyautogui.moveTo(1200, 1050)
    pyautogui.click()
    
def message():
    messagemove = random.randint(900,1050)
    pyautogui.moveTo(messagemove, 1050)
    pyautogui.click()

def copypaste():
    text = random.choice(list1)
    text2= random.choice(list2)
    pyautogui.write("selam "+text+"o mini eteğin altini görmek istiyorsan birazcik para at ben garantisini "
                    + text2 + " veriyorum garanti iban :TR800006200042200006294217 ,papara=1427130794")

def wait():
    time.sleep(0.05)
    
def esc():
    
    pyautogui.press('esc')
def main():
    if keyboard.is_pressed('enter'):
        message()
        wait()
        copypaste()   
        wait()
        enter()
        wait() 
        esc()
        # if keyboard.is_pressed('e'):
            
         
while True:
    main()