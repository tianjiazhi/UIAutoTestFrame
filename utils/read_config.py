# coding = utf-8
"""
@Time      : 2020/3/17 0017 21:01
@Author    : YunFan
@File      : read_config.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""


from configparser import ConfigParser
from utils.project_root_path import get_root_path

class ReadConfig:
    """读取配置文件"""
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(get_root_path() + "/config/config.ini", encoding='utf-8')

    def get_filePath_config_var(self,name):
        value = self.config.get('FILEPATH', name)
        return value

    def get_logger_config_var(self,name):
        value = self.config.get('LOGGER',name)
        return value


if __name__ == '__main__':
    # 调用实例
    read_config = ReadConfig()
    s1 = read_config.get_filePath_config_var('ScreenShotPath')
    s2 = read_config.get_filePath_config_var('LogPath')
    s3 = read_config.get_filePath_config_var('ReportPath')
    print(s1)
    print(s2)
    print(s3)

