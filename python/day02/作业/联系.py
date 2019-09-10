class Animal():

    def __init__(self,color,kind,age,name,sex):
        self.color = color
        self.kind = kind
        self.age = age
        self.name = name
        self.sex = sex

    def eat(self,food):
        print("吃%s..."%food)

    def run(self):
        print("跑")



class Dog(Animal):

    def ruin(self):
        print("拆家")

class laoshu(Animal):

    def jiao(self,shengying):
        print("%s %s %s..."%shengying)



if __name__ == '__main__':
    # dog = Dog("黄色","123",3,"xiaoxi","公")
    # dog.run()
    pass


class Stack(list):
    pass



class Father():

    def __init__(self,name,car,house,money):
        self.name = name
        self.car =  car
        self.house = house
        self.__money = money

    def makemoney(self,money):
        print("会赚钱%s"%self.__money)

    def driver(self,name):
        print("%s会开车"%self.name)

    def sing(self):
        print("会唱歌")

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,mon):
        self.__money = mon

class Son(Father):

    def __init__(self,name):
        self.name = name



class Daughter(Father):

    def __init__(self,name,car,house,face):
        self.face = face
        super().__init__(name,car,house)

    def faces(self,name,face):
        print("%s的颜值为%d"%(self.name,self.face))

if __name__ == '__main__':
    son = Father("xiaowang","daben","beijing",1000000000)
    print(son.house)
    son.money -= 109
    print(son.money)
