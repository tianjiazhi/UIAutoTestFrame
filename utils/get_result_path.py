# coding = utf-8
"""
@Time      : 2020/3/17 0017 22:29
@Author    : YunFan
@File      : get_result_path.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

import os
from utils.get_time import get_format_time
from utils.project_root_path import make_path
from utils.read_config import ReadConfig


class GetPath:
    def __init__(self):
        self.read_config = ReadConfig()

    def get_screen_shot_path(self):
        screen_shot = self.read_config.get_filePath_config_var('ScreenShotPath')
        format_time = get_format_time('%Y-%m-%d-%H')
        screen_joint_path =  os.path.join(screen_shot, format_time)
        make_path(screen_joint_path)
        return screen_joint_path

    def get_logs_path(self):
        log_path = self.read_config.get_filePath_config_var('LogPath')
        format_time = get_format_time('%Y-%m-%d')
        log_joint_path = os.path.join(log_path, format_time)
        make_path(log_joint_path)
        return log_joint_path

    def get_report_path(self):
        report_path = self.read_config.get_filePath_config_var('ReportPath')
        format_time = get_format_time('%Y-%m-%d')
        log_joint_path = os.path.join(report_path, format_time)
        make_path(log_joint_path)
        return log_joint_path


if __name__ == '__main__':
    # 调用实例
    print(GetPath().get_screen_shot_path())
    print(GetPath().get_logs_path())
    print(GetPath().get_report_path())


