# coding = utf-8
"""
@Time      : 2020/3/19 0019 10:17
@Author    : YunFan
@File      : actionchain_page.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from selenium.webdriver.common.by import By
from base.page_base.factory_driver import WebUI

class ActionChainsPage(WebUI):
    _s1 = (By.XPATH,'//input[@value="清除"]')
    _s2 = (By.XPATH, '//input[@value="双击"]')
    _s3 = (By.XPATH, '//input[@value="单击"]')
    _s4 = (By.XPATH,'//input[@value="右击"]')
    _s5 = (By.XPATH, '//input[@value="点住不放开"]')
    _s6 = (By.XPATH, '//input[@value="鼠标一进来"]')



    def double(self):
        self.double_click(self._s2)
        return self


    def context(self):
        self.context_click(self._s4)
        return self


    def move(self):
        self.move_to_element(self._s6)
        return self


    def click_clear(self):
        self.click(self._s1)
        return self




