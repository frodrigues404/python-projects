from tracemalloc import StatisticDiff
import pyautogui
from time import sleep

sleep(2)

palavras = open("beemovie.txt", 'r')

for word in palavras:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


palavras.close()