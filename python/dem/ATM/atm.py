#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import random
import json
from ATM.user import User
from ATM.card import Card
from ATM.user import User
# from day02.atm.card import Card
# from E.python.

class ATM:

    userDict={}
    islogin = None

    @staticmethod
    def welcome():
        print('''
           **********************
           *                    *
           *  welcome to bank   *
           *                    *
           **********************
           ''')

    @staticmethod
    def select():
        print('''
           **********************
           *  1.登陆   2.开户    *
           *  3.查询   4.取款    *
           *  5.存款   0.退出    *
           *  6.转账   7.改密    *
           *  8.锁卡   9.解锁    *
           **********************
           ''')
        num = input("请选择服务项目：")
        return num

    @staticmethod
    def getcardnum():
        cardnum = ""
        for x in range(6):
            cardnum += str(random.randrange(0,10))
        return cardnum

    @classmethod
    def openUser(cls):
        name = input("请输入您的姓名：")
        idcard = input("请输入您的身份证号码：")
        phonenum = input("请输入您的电话号码：")
        psd = input("请设置您的密码：")
        psd2 = input("请确认您的密码：")
        if psd == psd2:
            mon = int(input("请输入您的预存余额："))
            if mon>0:
                cardnum = cls.getcardnum()
                card = Card(cardnum,psd,mon)
                user = User(name,idcard,phonenum,card)
                cls.userDict[cardnum] = user
                print("开卡成功，您的卡号为%s,请牢记..."%cardnum)

            else:
                print("预存余额非法，开卡失败...")

        else:
            print("两次输入密码不一致，开卡失败...")


    @classmethod
    def login(cls):
        cardnum = input("请输入您的卡号：")
        user = cls.userDict.get(cardnum)
        if user:
            psd = input("请输入您的密码:")
            if psd == user.card.password:
                print("恭喜你，登录成功！！！")
                cls.islogin = cardnum
            else:
                print("密码错误，登录失败。。。")
        else:
            print("卡号不存在，请查证后登录。。。")


    @classmethod
    def search(cls):
        if cls.islogin:
            print("您当前的余额为%d"%(cls.userDict.get(cls.islogin).card.money))

        else:
            print("请登录后查询")
    @staticmethod
    def setmoney(cls):
        money = int(input("请输入您要取的金额："))
        if cls.userDict.get(cls.islogin).card.money - money >= 0:
            print("取款%d成功！"%money)
            cls.userDict.get(cls.islogin).card.money -= money
            print("您卡里的余额为%s"%cls.userDict.get(cls.islogin).card.money - money)
        else:
            print("余额不足，取款失败！")


    # def dict2per(d):
    #     return (d["name"], d["age"])
    # @classmethod
    # def cunchu(cls):
    #     with open("per.txt", "w", encoding="utf-8") as f:
    #         for per in cls.userDict:
    #             str1 = json.dumps(per, default=)
    #             f.write(str1 + "\n")
    #             json.dump(per, f)