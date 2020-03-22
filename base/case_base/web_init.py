# coding = utf-8
"""
@Time      : 2020/3/16 0016 17:17
@Author    : YunFan
@File      : web_init.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

import unittest
from selenium import webdriver

class WebInit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\PycharmProjects\\UIAutoTestFrame\\driver\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com')
        # self.driver.get('D:\\text3.html')
        # self.driver.get('D:\\demo_clicks.html')


    def tearDown(self):
        self.driver.quit()

