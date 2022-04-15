class Banks():
    title = 'Taipei Bank'
    def __init__(self,uname):
        self.__name = uname
        self.__balance = 0
    
    def save_money(self,money):
        self.__balance += money
        print('存款',money,'完成')

    def withdraw_money(self,money):
        self.__balance -= money
        print('提款',money,'完成')

    def get_balance(self):
        print(self.__name.title(),'目前餘額:',self.__balance)
    sc=property(get_balance,save_money)
h=Banks('h')
print(h.sc)
h.sc=80
print(h.sc)