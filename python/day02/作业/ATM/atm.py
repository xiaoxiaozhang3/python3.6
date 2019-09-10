from 作业.ATM.card import Card
from 作业.ATM.user import User

import random


class ATM:

    userDict={}
    islogin = None
    changshicishu = 0

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
           *  8.注销   9.解锁    *
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
    #开户
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

    #登录
    @classmethod
    def login(cls):

        cardnum = input("请输入您的卡号：")
        user = cls.userDict.get(cardnum)
        if user:
            while True:
                psd = input("请输入您的密码:")
                if psd == user.card.password:
                    print("恭喜你，登录成功！！！")
                    cls.changshicishu = 0
                    cls.islogin = cardnum
                    break
                else:
                    cls.changshicishu += 1
                    if cls.changshicishu >= 3:
                        print("卡已被锁，请先解锁")
                        cls.islogin = False
                        print(cls.islogin)
                        break
                    else:
                        print("密码错误，请重新输入，还有%d次将锁卡"%(3-cls.changshicishu))
        else:
            print("卡号不存在，请查证后登录。。。")

    # 查询
    @classmethod
    def search(cls):
        print(cls.islogin)
        if cls.islogin:
            print("您当前的余额为%d"%(cls.userDict.get(cls.islogin).card.money))

        else:
            print("请先登录")
    #取钱
    @classmethod
    def setmoney(cls):
        if cls.islogin:
            money = int(input("请输入您要取的金额："))
            print(cls.userDict.get(cls.islogin).card.money)
            if cls.islogin:
                if cls.userDict.get(cls.islogin).card.money - money >= 0 :
                    print("取款%d成功！"%money)
                    cls.userDict.get(cls.islogin).card.money -= money
                    print("您卡里的余额为%d"%cls.userDict.get(cls.islogin).card.money)
                else:

                    print("余额不足，取款失败！")
            else:
                print("未登录，请登录后再试")
        else:
            print("请先登录")

    #存钱
    @classmethod
    def getmoney(cls):
        if cls.islogin:
            while True:
                gmoney = int(input("请输入您要存储的款项："))
                if gmoney > 0 :
                    cls.userDict.get(cls.islogin).card.money += gmoney
                    print("您卡上的余额为%d"%cls.userDict.get(cls.islogin).card.money)
                    return cls.userDict.get(cls.islogin).card.money
                else:
                    print("输入有误，请重新输入金额")
        else:
            print("请先登录！")
    #转账
    @classmethod
    def zhuanzhang(cls):
        if cls.islogin:
            while 1:
                kahao = input("您需要转到的卡号为：")
                for x in cls.userDict.keys():
                    if x == kahao :
                        print("您要转的卡号为%s,持卡人为%s"%(x,cls.userDict[x].name))
                        amoney = int(input("您需要转的金额为"))
                        #转账人卡内余额减少
                        cls.userDict.get(cls.islogin).card.money -= amoney
                        #被转账人卡内余额增加
                        cls.userDict.get(x).card.money += amoney

                    else:
                        continue
                print("卡号有误，请重新输入")

                break
        else:
            print("请先登录！")
     #改密码
    @classmethod
    def gaimi(cls):
        if cls.islogin:
            mima1 = input("请输入您需要修改的密码：")
            mima2 = input("请再次输入修改的密码：")
            if mima1 == mima2:
                cls.userDict.get(cls.islogin).card.password = mima1
                print("您的新密码为%s"%mima1)
        else:
            print("请先登录")
    #锁卡
    @classmethod
    def suoka(cls):
        if  cls.changshicishu >=3:
            print("卡以被锁，请先解锁")
    #解锁
    @classmethod
    def jiesuo(cls):
        print("请输入您的卡号和密码")
        kahao1 = input("请输入卡号：")
        mima3 = input("请输入密码：")
        for x in cls.userDict.keys():
            if kahao1 == x:
                if mima3 == cls.userDict.get(x).card.password:
                    print("解锁成功")
                    cls.islogin = cls.userDict.get(x).card.cardnum

                else:
                    print("账号或者密码不正确，请重试")
            else:
                print("账号或者密码不正确，请重试")

    #注销
    @classmethod
    def zhuxiao(cls):
        cls.islogin = False
        print("注销成功")
