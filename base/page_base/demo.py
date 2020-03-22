# coding = utf-8
"""
@Time      : 2020/3/21 0021 18:04
@Author    : YunFan
@File      : demo.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
# def fn(*a):
#     print("a = ",a)
#     print(type(a))
# fn(1,2,3,"张三丰")
#
#
# def fn1(a,b,*c):
#     print("a = ", a)
#     print("b = ", b)
#     print("c = ", c)
# fn1(1,2,3,"张三丰")
#
#
# def fn2(a,*b,c):
#     print("a = ", a)
#     print("b = ", b)
#     print("c = ", c)
# fn2(1,2,3,c="张三")
#
# def fn3(*a,b,c):
#     print("a = ", a)
#     print("b = ", b)
#     print("c = ", c)
# fn3(1,2,b=3,c="hhh")


def ss(a,b,c=None,*args,**kwargs):
    print('a=', a, type(a))
    print('b=', b, type(b))
    print('c=', c, type(c))
    print('args=', args, type(args))
    print('kwargs=', kwargs, type(kwargs))

# s = ss(11,22,33,44,55,haha=66,hehe=77)
# print(s)


kwarg = {'haha': 66, 'hehe': 77}
s = {'haha': None, 'hehe': None}
s.update(kwarg)
print(s)



# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Sex': 'female' }
#
# dict.update(dict2)
# print(dict)