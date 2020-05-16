import time
import webbrowser
import pyautogui

URL = 'https://www.facebook.com/groups/python'
#Screen resolution. Cursor point
POS1 = (680, 260) 
POS2 = (680, 730)
#To open fb
url = 'www.facebook.com'
webbrowser.open(url)
time.sleep(4)
#To move cursor
pyautogui.moveTo(POS1)
pyautogui.click(POS1)
pyautogui.typewrite("atmanirbar bano. My python Bot posted this on fb not me")
pyautogui.moveTo(POS2)
time.sleep(3)
pyautogui.click(POS2)
