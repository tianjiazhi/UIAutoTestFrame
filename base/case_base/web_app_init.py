# coding = utf-8
"""
@Time      : 2020/3/20 0020 13:51
@Author    : YunFan
@File      : web_app_init.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import unittest
from appium import webdriver as app_driver
from selenium import webdriver as web_driver


class WebAppInit(unittest.TestCase):
    def setUp(self):

        # 启动android平台的driver
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 测试平台名称
        # 真机配置参数
        desired_caps['platformVersion'] = '8.0.0'  # 测试平台版本号
        desired_caps['deviceName'] = '华为Nova2'  # 手机设备名称
        # 手机微信APP
        desired_caps['appPackage'] = 'com.tencent.mm'  # 安卓应用程序包名
        desired_caps['appActivity'] = '.ui.LauncherUI'  # 安卓应用程序入口名称

        desired_caps['unicodeKeyboard'] = True  # 启用unicode编码方式输入字符，默认为False
        desired_caps['resetKeyboard'] = True  # 隐藏软键盘

        desired_caps['noReset'] = True  # 在本次会话之前，不重置应用程序状态。
        desired_caps['newCommandTimeout'] = 240
        desired_caps['automationName'] = 'Uiautomator2'  # 使用的自动化引擎名称
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

        self.app_driver = app_driver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


        # 启动web端driver
        self.web_driver = web_driver.Chrome(
            executable_path="C:\\Users\\Administrator\\PycharmProjects\\UIAutoTestFrame\\driver\\chromedriver.exe")

        ac = self.app_driver.current_activity  # 获取主页面的activity
        self.app_driver.wait_activity(ac, 10)  # 等主页面activity出现后，才开始进行正式操作，最大超时时间设置为10s。

        self.web_driver.maximize_window()
        self.web_driver.get('https://www.baidu.com')

        # 设置隐形等待
        self.app_driver.implicitly_wait(15)
        self.web_driver.implicitly_wait(15)


    def tearDown(self):

        # 关闭android平台的driver
        self.app_driver.quit()

        # 关闭web端的driver
        self.web_driver.quit()
