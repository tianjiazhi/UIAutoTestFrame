# coding = utf-8
"""
@Time      : 2020/2/29 0029 9:30
@Author    : YunFan
@File      : get_time.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import time
from datetime import datetime

def get_now_timestamp():
    """获取秒级时间戳"""
    timestamp = int(time.time())
    return timestamp


def get_format_time(strftime = None):
    """
    格式化时间戳为本地的时间
    # '%Y-%m-%d %H:%M:%S.%f'
    """
    dn = datetime.now()
    if strftime is None:
        format_time = dn.strftime('%Y-%m-%d %H:%M:%S')
    else:
        format_time = dn.strftime(strftime)
    return format_time


if __name__ == '__main__':
    print(get_format_time())
