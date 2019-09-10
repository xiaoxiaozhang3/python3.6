#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
from ATM.atm import ATM
import time
from ATM.user import User
from ATM.card import Card


if __name__ == '__main__':
    ATM.welcome()
    while True:
        time.sleep(1)
        print(ATM.userDict)
        num = ATM.select()
        if num == "2":
            print("开户")
            ATM.openUser()
        elif num == "0":
            print("退出")
            break
        elif num == "1":
            print("登录")
            ATM.login()
        elif num == "3":
            print("查询")
            ATM.search()
        else:
            print("选择有误请重新选择...")
