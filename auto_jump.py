#import pyautogui
import random
#import cv2
import win32api
import win32con
from win32api import GetSystemMetrics
#from win32con import SM_CMONITORS, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN
import time
import ctypes
from ctypes import CDLL
from simple_pid import PID
import pynput
MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
num = 32

def mouse_move(driver,target_x,target_y):
    mouse = pynput.mouse.Controller()
    while True:
        if abs(target_x - mouse.position[0])<3 and abs(target_y - mouse.position[1])<3:
            break
        pid_x = PID(0.25, 0.01, 0.01, setpoint=target_x)
        pid_y = PID(0.25, 0.01, 0.01, setpoint=target_y)
        next_x,next_y = pid_x(mouse.position[0]),pid_y(mouse.position[1])
        driver.moveR(int(round(next_x)), int(round(next_y)), False) # 鼠标移动
        # print(mouse.position) # 打印鼠标位置

#screen_width, screen_height = win32api.GetSystemMetrics(win32con.SM_CXSCREEN),win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
#print(screen_width,screen_height)

try:
    gm = CDLL(r'ghub_device.dll')
    gmok = gm.device_open() == 1
    if not gmok:
        print('未安装ghub或者lgs驱动!!!')
    else:
        print('初始化成功!')
except FileNotFoundError:
    print('缺少文件')

def mouse_xy(x, y, abs_move = False):
    if gmok:
        gm.moveR(int(x), int(y), abs_move)
        
def sleep_time():
    random_time = random.randint(1,5)
    time.sleep(random_time)
    print("随机时间",random_time)
    return random_time

def seesomething():
    randomx = random.randint(2700,4300)
    randomy = random.randint(1,1200)
    #mouse_xy(randomx,randomy,abs_move=True)
    mouse_move(gm,randomx,randomy)
    #win32api.SetCursorPos([randomx,randomy])
    print("随机视角：",randomx,randomy)

def keydownup():
    time.sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), win32con.KEYEVENTF_KEYUP, 0)

while True:
    #seesomething()
    sleep_time()
    keydownup()
    #sleep_time()

