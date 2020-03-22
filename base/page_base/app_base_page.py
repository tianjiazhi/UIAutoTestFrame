# coding = utf-8
"""
@Time      : 2020/3/18 0018 20:52
@Author    : YunFan
@File      : app_base_page.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from appium.webdriver.common.touch_action import TouchAction
from base.page_base.public_base_page import PublicBasePage
from utils.logger import logger


class AppBasePage(PublicBasePage):
    def __init__(self,driver):
        super(AppBasePage,self).__init__(driver)
        self.driver = driver

    def back(self):
        '''按下返回键'''
        self.driver.keyevent(4)

    def close_app(self):
        self.driver.close_app()


    @property # 获取手机的屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    @property # 获取手机屏幕的高度
    def get_window_height(self):
        return self.get_window_size['height']

    @property # 获取手机屏幕的宽度
    def get_window_widths(self):
        return self.get_window_size['width']

    @property  # 获取手机屏幕宽度一半位置的坐标
    def __get_centre_window_widths(self):
        return self.get_window_widths * 0.5  # x坐标

    @property  # 获取手机屏幕0.2宽度位置的坐标
    def __get_left_window_widths(self):
        return self.get_window_widths * 0.2  # x坐标

    @property  # 获取手机屏幕0.8宽度位置的坐标
    def __get_right_window_widths(self):
        return self.get_window_widths * 0.8  # x坐标

    @property # 获取手机屏幕高度一半位置的坐标
    def __get_centre_window_height(self):
        return self.get_window_height * 0.5  # y坐标

    @property  # 获取手机屏幕0.2倍高度位置的坐标
    def __get_up_window_height(self):
        return self.get_window_height * 0.2  # y坐标

    @property  # 获取手机屏幕0.8倍高度位置的坐标
    def __get_down_window_height(self):
        return self.get_window_height * 0.8  # y坐标


    def __conversion_of_coordinates(self,x,y):
        '''坐标转换按照屏幕的比例进行换算后返回换算后的坐标'''
        width = self.get_window_widths
        height = self.get_window_height
        try:
            fx = float(x)
            fy = float(y)
        except ValueError as e:
            logger.error('坐标参数{}数据值错误，错误详细信息：{}'.format((x, y), e))
        except TypeError as e:
            logger.error('坐标参数{}数据类型错误，错误详细信息：{}'.format((x,y),e))
        else:
            x1 = int((fx / width) * width)
            y1 = int((fy / height) * height)
            return x1,y1


    def __data_conversion_process(self,selector,index,x,y):
        if selector and index and x is None and y is None:
            element = self.elements_convert_element(selector, index)
        elif selector and index is None and x is None and y is None:
            element = self.find_element(selector)
        else:
            element = None
        if x and y and selector is None and index is None:
            coordinates = self.__conversion_of_coordinates(x, y)
            xx = list(coordinates)[0]
            yy = list(coordinates)[1]
        else:
            xx = None
            yy = None
        return element,xx,yy

    def swipe_down(self,num = 1, t = 500):
        '''向下滑动，滑动时Y轴起点小于终点'''
        x1 = self.__get_centre_window_widths  # x坐标
        y1 = self.__get_up_window_height      # 起点y坐标
        y2 = self.__get_down_window_height    # 终点y坐标
        for i in range(num):self.driver.swipe(x1,y1,x1,y2,t)


    def swipe_up(self,num = 1, t = 500):
        '''向上滑动，滑动时Y轴起点大于终点'''
        x1 = self.__get_centre_window_widths  # x坐标
        y1 = self.__get_down_window_height    # 起点y坐标
        y2 = self.__get_up_window_height      # 终点y坐标
        for i in range(num):self.driver.swipe(x1,y1,x1,y2,t)


    def swipe_left(self,num = 1, t = 500):
        '''向左滑动，滑动时X轴起点小于终点'''
        y1 = self.__get_centre_window_height  # y坐标
        x1 = self.__get_right_window_widths   # 起点x坐标
        x2 = self.__get_left_window_widths    # 终点x坐标
        for i in range(num):self.driver.swipe(x1,y1,x2,y1,t)


    def swipe_right(self,num = 1, t = 500):
        '''向右滑动，滑动时X轴起点大于终点'''
        y1 = self.get_window_height * 0.5  # y坐标
        x1 = self.__get_left_window_widths  # 起点x坐标
        x2 = self.__get_right_window_widths  # 终点x坐标
        for i in range(num):self.driver.swipe(x1,y1,x2,y1,t)


    def touch_tap(self, x, y, duration=50):
        '''点击坐标'''
        coordinates = self.__conversion_of_coordinates(x, y)
        self.driver.tap([coordinates, coordinates], duration)


    def long_press(self,selector=None, index=None, x=None, y=None,duration=1000):
        '''
        长按一个元素或者坐标
        :param selector: 要长按的元素
        :param index: 采用多元素定位时所用的索引
        :param x: 要长按位置的X轴坐标
        :param y: 要长按位置的Y轴坐标
        :param duration: 长按时间（单位：ms）
        :return:
        '''
        param = list(self.__data_conversion_process(selector,index,x,y))

        try:
            ta = TouchAction(self.driver)
            ta.long_press(el=param[0], x=param[1], y=param[2], duration=duration).release().perform()
        except Exception as e:
            logger.error("Failed to long_press with %s" % e)


    def press(self,selector=None, index=None, x=None, y=None,pressure=None):
        """
        短按一个元素或者坐标
        :param selector: # 待短按的元素
        :param index: # 采用多元素定位时所用的索引
        :param x: # 待短按位置的X轴坐标
        :param y: # 待短按位置的Y轴坐标
        :param pressure: # 按下为强制触摸。阅读苹果UITouch类的“force”属性描述
        :return:
        """
        param = list(self.__data_conversion_process(selector, index, x, y))
        try:
            ta = TouchAction(self.driver)
            ta.press(el=param[0], x=param[1], y=param[2],pressure = pressure).release().perform()
        except Exception as e:
            logger.error("Failed to short_press with %s" % e)



    def tap(self,selector=None, index=None, x=None, y=None, count=1):
        '''
        :param selector: # 待要点击的元素
        :param index: # 采用多元素定位时所用的索引
        :param x: # 待要点击的X轴坐标
        :param y: # 待要点击的Y轴坐标
        :param count: # 点击的次数
        :return:
        '''
        param = list(self.__data_conversion_process(selector, index, x, y))

        try:
            ta = TouchAction(self.driver)
            ta.tap(element=param[0], x=param[1], y=param[2], count=count).perform()
        except Exception as e:
            logger.error("Failed to tap with %s" % e)


    def move_to(self,selector1=None,index1=None,x1=None,y1=None,selector2=None,index2=None,x2=None,y2=None):
        """
        将元素从A点移动至B点
        :param selector1: 移动前的位置的元素
        :param index1: 采用多元素定位时所用的索引
        :param x1: 移动前的位置的X轴坐标
        :param y1: 移动前的位置的Y轴坐标
        :param selector2: 移动至目标位置的元素
        :param index2: 采用多元素定位时所用的索引
        :param x2: 移动至目标位置的X轴坐标
        :param y2: 移动至目标位置的Y轴坐标
        """
        p1 = list(self.__data_conversion_process(selector1, index1, x1, y1))
        p2 = list(self.__data_conversion_process(selector2, index2, x2, y2))
        try:
            ta = TouchAction(self.driver)
            ta.long_press(el=p1[0], x=p1[1], y=p1[2]).move_to(el=p2[0], x=p2[1], y=p2[2]).release().perform()
        except Exception as e:
            logger.error("Failed to  move_to with %s" % e)