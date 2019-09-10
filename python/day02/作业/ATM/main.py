from 作业.ATM.atm import ATM
import time


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
            ATM.suoka()
        elif num == "3":
            print("查询")
            ATM.search()
        elif num == "4":
            ATM.setmoney()
        elif num == "5":
            ATM.getmoney()
        elif num == "6":
            ATM.zhuanzhang()
        elif num == "7":
            ATM.gaimi()
        elif num == "8":
            ATM.zhuxiao()
        elif num == "9":
            ATM.jiesuo()
        else:
            print("选择有误请重新选择...")


'''
           **********************
           *  1.登陆   2.开户    *
           *  3.查询   4.取款    *
           *  5.存款   0.退出    *
           *  6.转账   7.改密    *
           *  8.锁卡   9.解锁    *
           **********************
'''
