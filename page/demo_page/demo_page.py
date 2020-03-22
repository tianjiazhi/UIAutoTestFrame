# coding = utf-8
"""
@Time      : 2020/3/16 0016 16:46
@Author    : YunFan
@File      : demo_page.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from selenium.webdriver.common.by import By
from base.page_base.factory_driver import WebUI


class BaiDuPage(WebUI):
    _search_bar = (By.ID,"kw")
    _search_button = (By.ID,"su")

    def input_search_bar(self,content):
        '''搜索输入框中输入内容'''
        self.send_keys(content,self._search_bar)
        return self

    @property
    def click_search_button(self):
        '''点击搜索按钮'''
        self.click(self._search_button)
        return self

    def ctrl_a(self):
        '''全选'''
        self.tag_keys(self._search_bar,'CONTROL','a')
        return self

    def ctrl_c(self):
        '''复制'''
        self.tag_keys(self._search_bar,'CONTROL','c')
        return self

    def ctrl_v(self):
        '''粘贴'''
        self.tag_keys(self._search_bar,'CONTROL','v')
        return self

    def click_bar(self):
        '''点击输入输入框'''
        self.click(self._search_bar)
        return self

    def copy_text(self,content):
        self.input_search_bar(content).ctrl_a().ctrl_c().click_bar().ctrl_v().\
            ctrl_a().ctrl_c().click_bar().ctrl_v().sleep(7)
