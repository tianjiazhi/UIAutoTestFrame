# coding = utf-8
"""
@Time      : 2020/3/19 0019 8:51
@Author    : YunFan
@File      : demopage1.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from selenium.webdriver.common.by import By
from base.page_base.factory_driver import WebUI

class DemoPage1(WebUI):
    _box1 = (By.ID,"area1")
    _kk = (By.ID,"box1")

    def move(self):
        self.drag_and_drop(self._kk,self._box1)
        self.sleep(6)
