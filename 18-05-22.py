class Component:
    def __init__(self):
        print('Component class object created...')

    def m1(self):
        print('Component class m1() method executed...')


class Composite:
    def __init__(self):
        self.obj1 = Component()
        print('Composite class object also created...')

    def m2(self):
        print('Composite class m2() method is executed...')
        self.obj1.m1()


obj2 = Composite()
obj2.m2()
