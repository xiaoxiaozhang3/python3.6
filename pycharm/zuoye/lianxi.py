# def testFun():
#
#     temp = [lambda x: i*x for i in range(4)]
#     print(temp)
#     return temp
#
# for everyLambda in testFun():
#     print(everyLambda(2))
from functools import reduce
from operator import add
# import unittest
# from mysub import mysun
# from mysun import mysum
#
# def func(a):
#     return a
# list1 = [12,34,23,'334',42]
#
# class Test(unittest.TestCase):
#
#     def setUp(self):
#         print("开始测试...")
#
#     def tearDown(self):
#         print("结束测试")
#
#     def test_mysun(self):
#         self.assertEqual(mysum(1,4),5,"输出有误")
#
# if __name__ == '__main__':
#     unittest.main()
# print(list(reduce(add,map(int,list1))))

# data = [["raa",12,"无"],["adw",14,"chi"]]
# print(list(sorted(data,key = lambda x : x[1],reverse=False)))
#
# print(list(filter(lambda n: False if  n[-1] =="无" else True , d
import re
#
# str1 = input("请输入一串数字")
#
# if str1.isalnum():
#     list1 =list(str1)
#     if :
#         if len(str1) > 3 and len(str1)<12:
#             str(list1)
#             print("qq号合法")
#         else:
#             print("不合法")
#     else:
#         print("不合法")
import re

str1 = "you are good man, you are ai man, you are ui man, you are nice man"

# print(re.findall(r"you"))
# import socket
#
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 创建连接
# # address:ip地址[域名]  端口号
# sock.bind(("10.20.159.181",9011))
# sock.listen(5)
#
# while True:
#     s,adress = sock.accept()
#     print(s,adress)
#     sock.recv(1024*1000)
#     sock.sendto(b"hi")
# path = r"E:\pycharm\zuoye\新建文本文档.txt"
# with open(path, "r", encoding="utf-8") as f:
#     str1 = f.read()
# list1 = re.split("\n",str1)
# msg = input("请输入您要发送的内容：")
# list1 = re.split("\n", str1)

# for x in list1:
#     if msg in x:
#         print(x)
#     else:
#         continue
# msg = input("请输入您要发送的内容：")
# print(re.search(msg,list2))
# print(str1)
# print(list2)
# print(type(str1))

#创建线程的方式
import threading

def func(str1):
    print(str1)
    print(threading.current_thread().name)

def createThread():
    t = threading.current_thread()










