# coding = utf-8
"""
@Time      : 2020/3/16 0016 17:22
@Author    : YunFan
@File      : test_001.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import time
import unittest
from base.case_base.web_init import WebInit
from page.demo_page.demo_page import BaiDuPage
from utils.get_time import get_format_time


class TestBaiDuCase(WebInit,BaiDuPage):

    def test_0(self):
        """搜索“虚竹”"""
        print(get_format_time())
        a = self.get_current_url
        b = self.input_search_bar("虚竹").click_search_button
        self.assertEqual(a,'https://www.baidu.com/')

    def test_1(self):
        """搜索“乔峰”"""
        print(get_format_time())
        a = self.get_current_url
        b = self.input_search_bar("乔峰").click_search_button
        self.assertEqual(a, 'https://www.baidu.com/')

    def test_2(self):
        """搜索“段誉”"""
        a = self.get_current_url
        b = self.input_search_bar("段誉").click_search_button
        self.assertEqual(a, 'https://www.baidu.com/')

    def test_3(self):
        """搜索“小龙女”"""
        a = self.get_current_url
        b = self.input_search_bar("小龙女").click_search_button
        self.assertEqual(a, 'https://www.baidu.com/')

    def test_4(self):
        b = self.input_search_bar("小龙女").ctrl_a().sleep(4)

    def test_5(self):
        self.copy_text("张三丰")



if __name__ == '__main__':
    unittest.main(verbosity=2)
