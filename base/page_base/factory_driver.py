# coding = utf-8
"""
@Time      : 2020/3/16 0016 16:06
@Author    : YunFan
@File      : factory_driver.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from base.page_base.app_base_page import AppBasePage
from base.page_base.web_base_page import WebBasePage

class WebUI(WebBasePage):
    def __str__(self):
        return 'WebUI'


class AppUI(AppBasePage):
    def __str__(self):
        return 'AppUI'


class Factory:
    """
    Factory类生成AutoDriver对象，定义Factory类创建不同的WebDriver对象。
    WebUI类和AppUI类继承了AutoDriver类。WebUI和AppUI可以看做是具体的测
    试对象（Web和App）。在Factory类中定义了工厂方法createDriver，工具字
    符串型driver的值，生成不同的AutoDriver对象。如果driver对象是“web”，
    则调用WebUI，返回WebUI类的实例；如果driver对象是“app”，则调用AppUI，
    返回AppUI类的实例。
    """
    def __init__(self,driver):
        self.driver = driver

    def create_driver(self,driver):
        if driver == 'web':
            return WebUI(self.driver)
        elif driver == 'app':
            return AppUI(self.driver)
