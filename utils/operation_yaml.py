# coding = utf-8
"""
@Time      : 2020/3/17 0017 7:39
@Author    : YunFan
@File      : operation_yaml.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

import yaml

class GetData:
    def __init__(self,file_name):
        self.file_name = file_name
        self.get_file_data = self.load_yml_file_data()
        self.s = self.__class__.__name__

    def load_yml_file_data(self):
        '''读取yml文件中的全部数据'''
        file = open(self.file_name,encoding='utf-8')
        res = yaml.load(file,Loader=yaml.FullLoader)
        return res

    def get_class_data(self,class_name,var_name):
        self.class_data = self.get_file_data[class_name][var_name]
        return self.class_data


get_data = GetData("./a.yml")
a = get_data.get_class_data('class_name1','var_name1')
print(a)
t = get_data.s
print(t)
print(type(t))


