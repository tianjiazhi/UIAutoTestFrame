# coding = utf-8
"""
@Time      : 2020/3/16 0016 17:17
@Author    : YunFan
@File      : app_init.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import unittest
from appium import webdriver

class Init(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 测试平台名称
        # 真机配置参数
        desired_caps['platformVersion'] = '8.0.0'  # 测试平台版本号
        desired_caps['deviceName'] = '华为Nova2'  # 手机设备名称
        # 手机微信APP
        desired_caps['appPackage'] = 'com.tencent.mm'  # 安卓应用程序包名
        desired_caps['appActivity'] = '.ui.LauncherUI'  # 安卓应用程序入口名称

        desired_caps['unicodeKeyboard'] = True  # 启用unicode编码方式输入字符，默认为False
        desired_caps['resetKeyboard'] = True    # 隐藏软键盘
        desired_caps['noReset'] = True          # 在本次会话之前，不重置应用程序状态。
        desired_caps['newCommandTimeout'] = 240
        desired_caps['automationName'] = 'Uiautomator2'  # 使用的自动化引擎名称
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        ac = self.driver.current_activity  # 获取主页面的activity
        self.driver.wait_activity(ac, 10)  # 等主页面activity出现后，才开始进行正式操作，最大超时时间设置为10s。
        self.driver.implicitly_wait(15)  # 设置隐形等待

    def tearDown(self):
        self.driver.quit()

