# sameer saeed
# simple drawing on mspaint using pyautogui

import random
import subprocess
import time
import pyautogui


# bounds
def withinXY(xx, yy):  # x and y bounds of square
    return (ww <= xx <= wx) and (hh <= yy <= hy)


def withinX(xx):  # x bounds of square
    return ww <= xx <= wx


def withinY(yy):  # y bounds of square
    return hh <= yy <= hy


# draws white dots at random positions within the bounds of a square
def drxy(xx, yy):
    dx, dy = random.randrange(offset * 2), random.randrange(offset * 2)
    if withinXY(xx + dx, yy + dy):
        xx += dx
        yy += dy
        pyautogui.dragTo(xx, yy, button='right')
        time.sleep(0.1)


# boots up mspaint
subprocess.call(["cmd", "/c", "start", "/max", "C:\\Windows\\system32\\mspaint.exe"])

time.sleep(1)
# zooms into paint twice
pyautogui.hotkey("ctrl", "pageup", "ctrl", "pageup")
time.sleep(0.1)

w, h = pyautogui.size()  # screen size
# initializing bounds of square
offset = 200  # reduce this value if program is bugging out
ww = (w / 2) - offset  # left
wx = (w / 2) + offset  # right
hh = (h / 2) - offset  # top
hy = (h / 2) + offset  # bottom

# moves cursor to center of screen
x, y = w / 2, h / 2
pyautogui.moveTo(x, y)

# draws pixels in a pattern before deleting itself
aa = ww
bb = hh

for j in range(int(hy - hh)):  # square's range in the y direction
    if withinY(bb):
        pyautogui.moveTo(aa, bb)
        pyautogui.dragTo(aa + (wx - aa), bb)  # draws a line of square
        bb += 5  # moves down so that another line can be drawn

# randomly placing white lines
count = 0
while count <= 100:
    drxy(ww, hh)
    count += 1

# exiting out of ms paint
pyautogui.hotkey("alt", "f4")
time.sleep(0.5)
pyautogui.hotkey("right", "enter")  # doesn't save painting
