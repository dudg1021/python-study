#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: 转载补充
@file: str-demo.py
@time: 2020/8/26 17:02
@desc: selenium 滑块移动
'''


from selenium.webdriver import ActionChains
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
# chrom在79版之前用这个
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
# =>linux环境 为Chrome配置无头模式
# options.add_argument("--headless")
# 无头模式 设置ua
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
# 不加载图片, 提升速度
# options.add_argument('blink-settings=imagesEnabled=false')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
# chrom在79版之后用这个
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
                   Object.defineProperty(navigator, 'webdriver', {
                     get: () => undefined
                   })
                 """
})

driver.get("https://www.qichacha.com/user_login")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="normalLogin"]').click()
time.sleep(1)
slider = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')


def get_track(distance):  # distance为传入的总距离
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 1

    while current < distance:
        if current < mid:
            # 加速度为2
            a = 4
        else:
            # 加速度为-2
            a = -3
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))

    print(track)
    return track


def move_to_gap(slider, tracks):  # slider是要移动的滑块,tracks是要传入的移动轨迹
    ActionChains(driver).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()


if __name__ == '__main__':
    move_to_gap(slider, get_track(300))
