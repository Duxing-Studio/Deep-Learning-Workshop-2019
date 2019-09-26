class Vehicle:

    def __init__(self, name, color):
        self.__name = name      # __name是私有数据字段
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getName(self):
        return self.__name


class Car(Vehicle):

    def __init__(self, name, color, model):
        # 调用父类的构造方法
        super().__init__(name, color)
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName())


class MySuperClass1():

    def method_super1(self):
        print("method_super1 method called")


class MySuperClass2():

    def method_super2(self):
        print("method_super2 method called")


class ChildClass(MySuperClass1, MySuperClass2):

    def child_method(self):
        print("child method")

c = ChildClass()
c.method_super1()
c.method_super2()


class A():

    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 from A")


class B(A):

    def __init__(self):
        self.__y = 1

    def m1(self):
        print("m1 from B")

c = B()
c.m1()
