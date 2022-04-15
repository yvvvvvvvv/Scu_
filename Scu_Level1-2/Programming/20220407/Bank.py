class Banks():
    title = 'Taipei Bank'
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
while True:
    x=eval(input('請選擇1.開戶 2.存款 3.提款 4.查餘額 5.結束程式(必須先開戶):'))
    if x == 1:
        x1=input('User Name:')
        user=Banks(x1,10000)
        print('已完成動作:開戶,起始金額為:10000元')
    elif x == 2:
        x2=int(input('請輸入存款金額:'))
        user.save_money(x2)
    elif x == 3:
        x3=int(input('請輸入提款金額:'))
        user.withdraw_money(x3)
    elif x == 4:
        user.get_balance()
    else:
        break