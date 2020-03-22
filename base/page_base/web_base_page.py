# coding = utf-8
"""
@Time      : 2020/3/17 0017 12:15
@Author    : YunFan
@File      : web_base_page.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from base.page_base.public_base_page import PublicBasePage
from utils.logger import logger



class WebBasePage(PublicBasePage):
    def __init__(self,driver):
        super(WebBasePage, self).__init__(driver)
        self.driver = driver


    def back(self):
        self.driver.back()
        logger.info("在当前页面上点击“后退”操作")


    def forward(self):
        self.driver.forward()
        logger.info("在当前页面上点击“前进”操作")


    def open_url(self,url):
        '''打开一个网页链接'''
        self.driver.get(url)
        logger.info("成功打开网址：{}".format(url))


    def maximize_window(self):
        self.driver.maximize_window()
        logger.info("浏览器已完成最大化操作")


    def minimize_window(self):
        self.driver.minimize_window()
        logger.info("浏览器已完成最小化操作")



    def move_to_element(self,selector,index=None):
        '''鼠标悬停事件'''
        if index:
            mouse = self.elements_convert_element(selector,index)
        else:
            mouse = self.find_elements(selector)
        try:
            ActionChains(self.driver).move_to_element(mouse).perform()
        except Exception as e:
            logger.error("Failed to move_to_element with %s" % e)


    def left_click(self,selector = None,index = None):
        '''鼠标单击事件'''
        if selector and index:
            on_element = self.elements_convert_element(selector,index)
        elif selector and index == None:
            on_element = self.find_element(selector)
        else:
            on_element = None
        try:
            ActionChains(self.driver).click(on_element).perform()
        except Exception as e:
            logger.error("Failed to left_click with %s" % e)


    def context_click(self,selector = None,index = None):
        '''鼠标右击事件'''
        if selector and index:
            on_element = self.elements_convert_element(selector,index)
        elif selector and index == None:
            on_element = self.find_element(selector)
        else:
            on_element = None
        try:
            ActionChains(self.driver).context_click(on_element).perform()
        except Exception as e:
            logger.error("Failed to context_click with %s" % e)


    def double_click(self,selector = None,index = None):
        '''鼠标双击事件'''
        if selector and index:
            on_element = self.elements_convert_element(selector,index)
        elif selector and index == None:
            on_element = self.find_element(selector)
        else:
            on_element = None
        try:
            ActionChains(self.driver).double_click(on_element).perform()
        except Exception as e:
            logger.error("Failed to double_click with %s" % e)


    def drag_and_drop(self,source_selector,target_selector,s_index=None,t_index=None):
        '''
        鼠标拖动事件
        :param source:鼠标拖动的源元素。
        :param target:鼠标释放的目标元素。
        '''
        if s_index:
            source_element = self.elements_convert_element(source_selector,s_index)
        else:
            source_element = self.find_element(source_selector)

        if t_index:
            target_element = self.elements_convert_element(target_selector,t_index)
        else:
            target_element = self.find_element(target_selector)

        try:
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
        except Exception as e:
            logger.error("Failed to double_click with %s" % e)


    @property
    def get_current_url(self):
        current_url = self.driver.current_url
        logger.info("已成功获取当前网页的网址:{}".format(current_url))
        return current_url

    @property
    def drag_scroll_bottom_bar(self):
        '''将浏览器的滚动条滑动到最底部'''
        js = "var q=document.documentElement.scrollTop=10000"
        drag_to_bottom = self.driver.execute_script(js)
        self.sleep(1)
        return drag_to_bottom

    @property
    def drag_scroll_top_bar(self):
        """将浏览器的滚动条滑动到最顶部"""
        js = "var q=document.documentElement.scrollTop=0"
        drag_to_top = self.driver.execute_script(js)
        self.sleep(1)
        return drag_to_top


    def drag_scroll_down_bar(self,drag_num:int=1):
        '''将浏览器的滚动条向下滑动200px'''
        for i in range(drag_num):
            js = 'window.scrollBy(0,250)'
            self.driver.execute_script(js)
            self.sleep(0.1)


    def drag_scroll_up_bar(self,drag_num:int=1):
        '''将浏览器的滚动条向上滑动200px'''
        for i in range(drag_num):
            js = 'window.scrollBy(0,-250)'
            self.driver.execute_script(js)
            self.sleep(0.1)


    def drag_scroll_left_bar(self,drag_num:int=1):
        '''将浏览器的滚动条向左滑动200px'''
        for i in range(drag_num):
            js = 'window.scrollBy(0,-250)'
            self.driver.execute_script(js)
            self.sleep(0.1)


    def drag_scroll_right_bar(self,drag_num:int=1):
        '''将浏览器的滚动条向右滑动200px'''
        for i in range(drag_num):
            js = 'window.scrollBy(0,250)'
            self.driver.execute_script(js)
            self.sleep(0.1)


    def __get_key_value(self,parm:str):
        """
        获取键名对应的值
        :parm的取值取以下值中的任意一个或者小写字母
        'BACKSPACE', 'ENTER', 'SHIFT', 'CONTROL', 'TAB', 'ALT', 'PAGE_UP', 'PAGE_DOWN',
        'LEFT', 'UP', 'RIGHT', 'DOWN', 'HOME', 'BACK_SPACE', 'LEFT_SHIFT', 'LEFT_CONTROL',
        'LEFT_ALT', 'ARROW_LEFT', 'ARROW_RIGHT', 'ARROW_DOWN', 'ARROW_UP', 'NULL', 'CANCEL',
        'HELP', 'CLEAR', 'RETURN','PAUSE', 'ESCAPE', 'SPACE', 'END', 'INSERT', 'SEMICOLON',
        'EQUALS', 'NUMPAD0', 'NUMPAD1', 'NUMPAD2', 'NUMPAD3', 'NUMPAD4', 'NUMPAD5', 'NUMPAD6',
        'NUMPAD7', 'NUMPAD8', 'NUMPAD9', 'MULTIPLY', 'ADD', 'SEPARATOR', 'SUBTRACT', 'DECIMAL',
        'DIVIDE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
        'META', 'COMMAND'
        """

        dic = {# 常用按键
            'BACKSPACE': Keys.BACKSPACE, 'ENTER': Keys.ENTER, 'SHIFT': Keys.SHIFT, 'CONTROL': Keys.CONTROL,
            'TAB': Keys.TAB, 'ALT': Keys.ALT, 'PAGE_UP': Keys.PAGE_UP, 'PAGE_DOWN': Keys.PAGE_DOWN,
            'LEFT': Keys.LEFT, 'UP': Keys.UP, 'RIGHT': Keys.RIGHT, 'DOWN': Keys.DOWN, 'HOME': Keys.HOME,
            # 双键（一般不用，底层和常用键的值相等）
            'BACK_SPACE': Keys.BACK_SPACE, 'LEFT_SHIFT': Keys.LEFT_SHIFT, 'LEFT_CONTROL': Keys.LEFT_CONTROL,
            'LEFT_ALT': Keys.LEFT_ALT, 'ARROW_LEFT': Keys.ARROW_LEFT, 'ARROW_RIGHT': Keys.ARROW_RIGHT,
            'ARROW_DOWN': Keys.ARROW_DOWN,'ARROW_UP': Keys.ARROW_UP,
            # 其他键
            'NULL': Keys.NULL, 'CANCEL': Keys.CANCEL, 'HELP': Keys.HELP, 'CLEAR': Keys.CLEAR,
            'RETURN': Keys.RETURN, 'PAUSE': Keys.PAUSE, 'ESCAPE': Keys.ESCAPE, 'SPACE': Keys.SPACE,
            'END': Keys.END, 'INSERT': Keys.INSERT, 'SEMICOLON': Keys.SEMICOLON, 'EQUALS': Keys.EQUALS,
            # 数字小键盘键
            'NUMPAD0': Keys.NUMPAD0, 'NUMPAD1': Keys.NUMPAD1, 'NUMPAD2': Keys.NUMPAD2, 'NUMPAD3': Keys.NUMPAD3,
            'NUMPAD4': Keys.NUMPAD4, 'NUMPAD5': Keys.NUMPAD5, 'NUMPAD6': Keys.NUMPAD6, 'NUMPAD7': Keys.NUMPAD7,
            'NUMPAD8': Keys.NUMPAD8, 'NUMPAD9': Keys.NUMPAD9, 'MULTIPLY': Keys.MULTIPLY, 'ADD': Keys.ADD,
            'SEPARATOR': Keys.SEPARATOR, 'SUBTRACT': Keys.SUBTRACT, 'DECIMAL': Keys.DECIMAL, 'DIVIDE': Keys.DIVIDE,
            # 功能键
            'F1': Keys.F1, 'F2': Keys.F2, 'F3': Keys.F3, 'F4': Keys.F4, 'F5': Keys.F5, 'F6': Keys.F6,
            'F7': Keys.F7, 'F8': Keys.F8, 'F9': Keys.F9, 'F10': Keys.F10, 'F11': Keys.F11, 'F12': Keys.F12,
            'META': Keys.META, 'COMMAND': Keys.COMMAND
        }

        dic_key_list = list(dic.keys())
        print(dic_key_list)
        if parm in dic_key_list:
            return dic.get(parm)
        else:
            return parm

        
    def tag_keys(self,selector,index=None,*loc):
        '''点击键盘上的按键'''
        if index:
            element = self.elements_convert_element(selector,index)
        else:
            element = self.find_element(selector)
        lis = []
        for i in loc:
            lis.append(self.__get_key_value(i))
        keys = tuple(lis)
        try:  # 输入
            element.send_keys(*keys)
            logger.info("在{}对应的元素中已成功按下键盘：{}".format(selector,loc))
        except Exception as e1:
            logger.error("在元素{}中键盘出现错误，错误详细信息：{}".format(selector, e1))
            self.get_screenShot("send_keys_key")
