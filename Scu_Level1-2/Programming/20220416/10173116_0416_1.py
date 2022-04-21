class Banks():
    def __init__(self,uname,money):
        self.name = uname
        self.balance = money
    
    def save_money(self,money):
        self.balance += money
        print('存款',money,'完成')

    def withdraw_money(self,money):
        self.balance -= money
        print('提款',money,'完成')

    def get_balance(self):
        print(self.name.title(),'目前餘額:',self.balance)
    
    def us_dollars(self,money):
        self.m = int(money)
        self.balance -= self.m*30.3
        print('購買',money,'元 美金')
        print('提款',self.m*30.3,'完成')

x1=input('User Name:')
user=Banks(x1,0)
while True:
    x=eval(input('請選擇 1.存款 2.提款 3.查餘額 4.購買美金 5.結束程式:'))
    if x == 1:
        x2=int(input('請輸入存款金額:'))
        user.save_money(x2)
        user.get_balance()
    elif x == 2:
        x3=int(input('請輸入提款金額:'))
        user.withdraw_money(x3)
        user.get_balance()
    elif x == 3:
        user.get_balance()
    elif x == 4:
        x4=input('欲購買美金金額:')
        user.us_dollars(x4)
        user.get_balance()
    else:
        break