import pyautogui


import pyperclip
from time import sleep

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

link = 'www.youtube.com'

pyperclip.copy(link)

pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

sleep (4)

pyautogui.click(x=800, y=120)
pyautogui.write('DONJGA')
pyautogui.press('enter')
