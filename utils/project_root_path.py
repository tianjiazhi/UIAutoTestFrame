# coding = utf-8
"""
@Time      : 2020/3/21 0021 8:27
@Author    : YunFan
@File      : project_root_path.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import os

def get_root_path():
    '''获取项目的根路径'''
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("UIAutoTestFrame\\") + len("UIAutoTestFrame\\")]
    return rootPath

def make_path(fq):
    '''文件夹不存在时，先创建文件夹'''
    if not os.path.exists(fq):os.makedirs(fq)

