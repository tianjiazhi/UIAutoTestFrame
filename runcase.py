# coding = utf-8
"""
@Time      : 2020/3/16 0016 18:43
@Author    : YunFan
@File      : runcase.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import os
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from utils.get_result_path import GetPath
from utils.get_time import get_format_time
from utils.project_root_path import get_root_path


class RunCase:

    def run(self):
        report_title = '测试报告标题'
        report_desc = '测试报告描述'

        report_path = GetPath().get_report_path()
        strfTime = get_format_time("%Y-%m-%d-%H-%M-%S")
        report_file = os.path.join(report_path,'report-' + strfTime +'.html')

        with open(report_file, 'wb') as report:

            case_path = get_root_path() + '/case/'
            suite = unittest.TestSuite()
            case_list = []

            # 使用os.walk方法遍历得到所有文件名称filename的列表集合
            for dir_path, dir_name, filename in os.walk(case_path):
                for file in filename:
                    # 判断文件以.py结尾且不以__开始，为去除__init.py文件和.pyx后缀的文件
                    if file.endswith(".py") and not file.startswith("__"):
                        case_list.append(file)

            # 得到有效的用例文件列表后传值给discover方法的pattern匹配方式，可拿到所有testcase
            # 此处注意，要想拿到所有的testcase必须在每个文件夹中有一个__init__.py文件引导，否则无法获取。
            for case in case_list:
                discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern=case)
                suite.addTest(discover)

            runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
            runner.run(suite)
        report.close()


if __name__ == '__main__':
    RunCase().run()
