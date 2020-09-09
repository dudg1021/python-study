# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
@author: diange.du
@file: pyautogui_demo.py
@time: 2020/9/4 15:06
@desc: pynput 移动滑块 测试
'''
import time
import random
from selenium import webdriver
from pynput.keyboard import Key, Controller as c2
from pynput.mouse import Button, Controller as c1


def login_taobao(username, userpass):
    # 打开本地chrome，同时打开直通车登录页面，需要提前配置环境变量path
    url = 'https://www.qichacha.com/user_login'
    # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # 不加载图片, 提升速度
    # options.add_argument('blink-settings=imagesEnabled=false')
    browser = webdriver.Chrome(options=options)
    # chrom在79版之后用这个
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                       Object.defineProperty(navigator, 'webdriver', {
                         get: () => undefined
                       })
                     """
    })

    browser.get(url)
    browser.refresh()
    time.sleep(1 + random.random())

    mouse = c1()
    key_word = c2()

    zuobiao = browser.find_element_by_xpath(
        '//div[@class="login-panel"]/div[@class="login-panel-head clearfix"]/div[2]').location
    daxiao = browser.find_element_by_xpath(
        '//div[@class="login-panel"]/div[@class="login-panel-head clearfix"]/div[2]').size
    print(zuobiao)

    # 此处是点击密码登录,需要根据你的电脑分辨率调整坐标
    mouse.position = (int(zuobiao['x']) + daxiao['width'] / 2, int(zuobiao['y']) + daxiao['height'] + 45)

    print(mouse.position)
    mouse.click(Button.left, 1)
    time.sleep(1 + random.random())
    guidao = browser.find_element_by_xpath(
        '//div[@class="nc-container"]//div[@class="nc_scale"]//div[@class="scale_text slidetounlock"]')
    spider_location = browser.find_element_by_xpath(
        '//div[@class="nc-container"]//div[@class="nc_scale"]//span[@class="nc_iconfont btn_slide"]').location
    spider_size = browser.find_element_by_xpath(
        '//div[@class="nc-container"]//div[@class="nc_scale"]//span[@class="nc_iconfont btn_slide"]').size
    trace = get_trace(guidao.size['width'])
    print(str(spider_location['x']) + ',' + str(spider_location['y']))
    while True:
        browser.refresh()
        time.sleep(1 + random.random())

        # 此处是把鼠标移动到滑块上,需要根据你的电脑分辨率调整坐标
        mouse.position = (1150, 540)
        print(mouse.position)
        print('开始移动')
        mouse.press(Button.left)
        time.sleep(1 + random.random())
        # for d in trace:
        #     mouse.move(d, 0)
        #     time.sleep(random.random() / 10)
        mouse.move(350, 0)
        time.sleep(0.5)
        mouse.release(Button.left)
        time.sleep(3)
        try:
            browser.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span/b[contains(text(),"验证通过")]')
            print('验证通过')
            break
        except:
            continue
    time.sleep(random.random())
    browser.find_element_by_xpath('//input[contains(@name,"nameNormal")]').send_keys(username)
    time.sleep(random.random())
    browser.find_element_by_xpath('//input[contains(@name,"pwdNormal")]').send_keys(userpass)
    time.sleep(random.random())
    browser.find_element_by_xpath(
        '//form[@id="user_login_normal"]//button[@class="btn btn-primary btn-block m-t-md login-btn"]/strong[contains(text(),"立即登录")]').click()
    time.sleep(10)
    browser.quit()


# 构造滑动轨迹
def get_trace(distance):
    '''
    计算滑动
    '''
    lu = [0.7, 0.3]
    # 创建存放轨迹信息的列表
    trace = []
    # 设置加速的距离
    # distance += 20
    faster_distance = distance + 50

    print('--------开始计算偏移量-------')
    for i in lu:
        the_distance = i * faster_distance
        # 设置初始位置、初始速度、时间间隔
        start, v0, t = 0, 0, 0.2
        # 当尚未移动到终点时
        while start < the_distance:
            # 如果处于加速阶段
            if start < the_distance:
                # 设置加速度为2
                a = 30
            # 如果处于减速阶段
            else:
                # 设置加速度为-3
                a = -30
            # 移动的距离公式
            move = v0 * t + 1 / 2 * a * t * t
            # 此刻速度
            v = v0 + a * t
            # 重置初速度
            v0 = v
            # 重置起点
            start += move
            # 将移动的距离加入轨迹列表
            trace.append(round(move, 2))
    print(trace)
    # 返回轨迹信息
    return trace


if __name__ == '__main__':
    username = '你的账号'
    userpass = '你的密码'
    login_taobao(username, userpass)
