#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: pyautogui_demo.py
@time: 2020/9/4 15:06
@desc: pyautogui 移动滑块 测试
'''

import pyautogui
from selenium import webdriver

import subprocess
import win32api
import time


# 1. 直接打开chrome 接口文档： https://www.cnblogs.com/111testing/archive/2019/04/23/10758817.html
# prs = subprocess.Popen(["C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"])
# time.sleep(1)
# pree = pyautogui.hotkey("ctrl", "shift", "n") # 进入无痕模式
# time.sleep(2)
# pyautogui.typewrite('http://geek.csdn.net/news/detail/86546', interval=0.25)
# pyautogui.press('enter')
# pyautogui.press('enter')
# time.sleep(2)

# 2. 通过selenium打开浏览器操作
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 不加载图片, 提升速度
# options.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=options)
# chrom在79版之后用这个
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
                   Object.defineProperty(navigator, 'webdriver', {
                     get: () => undefined
                   })
                 """
})

driver.get("https://www.qcc.com/user_login")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="normalLogin"]').click()
time.sleep(2)
slider = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')

print(slider.location)
pyautogui.moveTo(slider.location['x']+10,slider.location['y']+90,duration=1)
#  开始很慢，不断加速
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
#  开始很快，不断减速
# pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
#  开始和结束都快，中间比较慢
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)
#  一步一徘徊前进
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)
#  徘徊幅度更大，甚至超过起点和终点
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)
pyautogui.dragTo(slider.location['x'] + 360, slider.location['y'] + 90, 2, pyautogui.easeInQuad)
