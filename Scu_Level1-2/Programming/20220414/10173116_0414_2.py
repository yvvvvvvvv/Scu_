class Grandmother():
    def __init__(self):
        self.grandmothermoney = 20000
        super().__init__()
    def get_info0(self):
        print("Grnadmother's information")

class Grandfather():
    def __init__(self):
        self.grandfathermoney = 10000
        super().__init__()
    def get_info1(self):
        print("Grnadfather's information")

class Father(Grandmother, Grandfather):
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()
    def get_info2(self):
        print("Father's information")

class Ivan(Father):
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):
        print('\nIvan資產:', self.ivanmoney, '\n父親資產:', self.fathermoney, '\n祖父資產:', self.grandfathermoney, '\n祖母資產:', self.grandmothermoney)

ivan = Ivan()
ivan.get_info3()
ivan.get_info2()
ivan.get_info1()
ivan.get_info0()
ivan.get_money()