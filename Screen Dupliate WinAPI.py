# This is a joke script which utilises the Winapi to duplicate and invert screen colour
# Screen flashing may be unsafe for people with photosensitivity / epilepsy 


import win32.win32api as win
import win32.win32gui as gui
import ctypes.wintypes as c 
import win32con as con
import math as m
import time as t

#Set the relevant dimensions for the screen
SM_CXSCREEN = 0
SM_CYFULLSCREEN = 17
sw =win.GetSystemMetrics(SM_CXSCREEN)
sh =win.GetSystemMetrics(SM_CYFULLSCREEN)
HDC = gui.GetDC(None)

while(1):
    gui.BitBlt(HDC,10,10,sw,sh,HDC,0,0,con.SRCCOPY)
    gui.BitBlt(HDC,-10,-10,sw,sh,HDC,0,0,con.NOTSRCCOPY)
    t.sleep(0.1)
input()