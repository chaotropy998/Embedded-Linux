import pyautogui as pag
import time

# Search (417, 157)
# More (436, 276)
# Mark as read (518, 306)

pag.hotkey('win')
time.sleep(1)
pag.typewrite("edge")
time.sleep(1)
pag.hotkey("enter")
time.sleep(2)
pag.typewrite("https://mail.google.com/mail/u/0")
time.sleep(1)
pag.hotkey("enter")
time.sleep(3)
pag.click(x= 417, y=157)
time.sleep(2)
pag.typewrite("label:unread")
time.sleep(2)
pag.hotkey("enter")
time.sleep(2)
pag.click(x=436,y=276)
time.sleep(2)
pag.click(x=518,y=306)

