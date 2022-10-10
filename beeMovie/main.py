import pyautogui
from time import sleep

sleep(5)

forLoop = open("beemovie", 'r')

for word in forLoop:
    pyautogui.typewrite(word)
    pyautogui.press("enter")