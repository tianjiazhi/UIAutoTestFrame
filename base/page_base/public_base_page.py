# coding = utf-8
"""
@Time      : 2020/3/18 0018 20:57
@Author    : YunFan
@File      : public_base_page.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from utils.get_result_path import GetPath
from utils.get_time import get_format_time
from utils.logger import logger


class PublicBasePage:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,selector):
        '''定位单个元素的方法'''
        try:
            element = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*selector))
            logger.info("已成功定位到 {}".format(selector))
            return element
        except NoSuchElementException as e1:
            logger.error("Error details {}".format(e1.args[0]))
            self.get_screenShot("NoSuchElement")
        except TimeoutException as e2:
            logger.error("在当前页面通过 {} 查找元素对象时，出现超时错误，错误详细信息：{}".format(selector,e2))
            self.get_screenShot("Timeout")



    def find_elements(self,selector):
        '''定位多个元素的方法'''
        try:
            elements = WebDriverWait(self.driver,10).until(lambda driver:driver.find_elements(*selector))
            logger.info("已成功定位到 {}".format(selector))
            return elements
        except NoSuchElementException as e1:
            logger.error("Error details {}".format(e1.args[0]))
            self.get_screenShot("NoSuchElement")
        except TimeoutException as e2:
            logger.error("在当前页面通过 {} 查找元素对象时，出现超时错误，错误详细信息：{}".format(selector, e2))
            self.get_screenShot("Timeout")



    def elements_convert_element(self,selector,index):
        """通过多个元素去定位单个元素"""
        try:
            return self.find_elements(selector)[index]
        except IndexError as e:
            logger.error("列表的索引错误,详细错误：{}".format(e))
        except Exception as e:
            logger.error("引发不可知的错误,详细错误：{}".format(e))


    def get_screenShot(self,name = "ScreenShot"):
        """获取屏幕截图"""
        tim = get_format_time('%M_%S_%f')
        type = '.png'
        # 对截图文件进行命名并保存到指定的文件中
        filename = GetPath().get_screen_shot_path() + "\\" + tim + "_" + name + type
        return self.driver.get_screenshot_as_file(filename)



    def send_keys(self,content,selector,index=None):
        """输入文本到文本框"""
        if index:
            element = self.elements_convert_element(selector,index)
        else:
            element = self.find_element(selector)

        try:  # 清空
            element.clear()
            logger.info("在元素 {} 对应的文本框中已完成“清空”操作".format(selector))
        except AttributeError as e1:
            logger.error("元素 {} 对应的页面对象进行“清空”操作出现错误，错误详细信息：{}".format(selector, e1))
            self.get_screenShot("clear")

        try:  # 输入
            element.send_keys(content)
            logger.info("在元素 {} 对应的文本框中已完成 “{}” 的输入。".format(selector,content))
        except AttributeError as e1:
            logger.error("元素 {} 对应的文本框中 “输入”操作时出现错误。错误详细信息：{}".format(selector, e1))
            self.get_screenShot("send_keys")


    def clear(self,selector,index=None):
        '''清空'''
        if index:
            element = self.elements_convert_element(selector,index)
        else:
            element = self.find_element(selector)
        try:
            element.clear()
            logger.info("在元素 {} 对应的文本框中已完成“清空”操作".format(selector))
        except AttributeError as e1:
            logger.error("元素 {} 对应的页面对象进行“清空”操作出现错误，错误详细信息：{}".format(selector, e1))
            self.get_screenShot("clear")


    def click(self,selector,index=None):
        '''点击'''
        if index:
            element = self.elements_convert_element(selector,index)
        else:
            element = self.find_element(selector)
        try:
            element.click()
            logger.info("元素 {} 对应的页面对象已完成“点击”操作".format(selector))
        except AttributeError as e1:
            logger.error("元素 {} 对应的页面对象进行“点击”操作出现错误，错误详细信息：{}".format(selector,e1))



    def sleep(self,seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
        return self