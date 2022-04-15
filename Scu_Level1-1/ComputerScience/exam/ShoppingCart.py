#1.建立一個販賣機的物件(class),其屬性需包含
# 1.每一項商品的名稱(用陣列儲存)
# 2.每一項商品的金額(用陣列儲存)
# 3.已賣出的累積金額
# 4.管理員的密碼
#功能需包含
# 1.顯示'quit'並退出程式
# 2.列出商品列表
# 3.選取商品編號並購買
# 4.輸入管理員密碼,顯示目前已賣出的累積金額,若不符合,顯示'wrong password'
#接著創建一個販賣機的物件,設定其中有三個商品
# 1.Shu run 2.Water 3.Cocoa
#價格分別為
# 1.35 2.25 3.40
#管理員密碼
# 'GoHomeAndVote'

##Prefix (input)
import hashlib
import sys

##Define Class & Function
#Class Vending Machine
class vending_machine(dict):
    menu = []
    cart = []
    total = []
    past = []

    def __repr__(self):
        return self.__class__.__name__ + super().__repr__()

    def add(self,good,price):
        self[good] = price
        self.menu.append(good)

    def rm(self,good):
        if good in self:
            del self[good]
            self.menu.remove(good)
            return True
        else:
            return False

    def empty_cart(self):
        for i in self.total:
            self.past.append(i)
        self.cart.clear()
        self.total.clear()

    def carted(self,good):
        self.cart.append(good)
        self.total.append(find(self, good))

#Function Define            
def find(ven,items):
    if items in ven.keys():
        return ven[items]

def pw_check():
    pw_input = input('please enter admin password:\n')
    if hashlib.sha1(bytearray(pw_input,'utf-8')).hexdigest() == pw_hash:
        print("password correct")
        return True
    else:
        print('wrong password')
        return False

##Program Setup
#Password hash value
pw_hash = 'ea626b3e3e90cc8fd155bc6f276c1a78954c243e'

### Online Vending Machine Setup####
onVen = vending_machine()
onVen.add('Shu run',35)
onVen.add('Water',25)
onVen.add('Cocoa',40)
#######i###############################

##Main Program
while True:
    opt_input = input("選擇功能: 1.Guest(訪客)| 2.Admin(管理員)| q:quit(離開)\n").lower()
    if opt_input == 'q' or opt_input == 'quit':
        print('system exit')
        break

####Guest
    elif opt_input == '1' or opt_input == 'guest':
        while True:
            for i in range(len(onVen.menu)):
                print(f'{i+1}. {onVen.menu[i]}: {find(onVen,onVen.menu[i])}')
            guest_input = input("請輸入要購買的商品編號(q:結束)：\n").lower()

            if guest_input == 'q':
                if len(onVen.cart) == 0:
                    print('不買還浪費我時間阿')
                else:
                    print(f"今天購買的產品有:\n{onVen.cart}\n總金額：{sum(onVen.total)}")
                    onVen.empty_cart()
                break                

            elif bool(guest_input) == True:
                try:
                    onVen.carted(onVen.menu[int(guest_input)-1])
                except IndexError:
                    print('Error: product does not exist!')
                except ValueError:
                    print('Error: integer input only')
                print(f'購物車:{onVen.cart}')
            else:
                continue

####Administrator
    elif opt_input == '2' or opt_input == 'admin':
        temp = pw_check()   
        while temp == True:
            ad_input = input("Function: 1. add product 2. delete product 3.past sells 4. change password Q: return menu\n")
            if ad_input == 'q' or ad_input == 'Q':
                break

            elif ad_input == '1':
                add_n = input('name of the product:\n').capitalize()
                try:
                    add_p = int(input('price of the product\n'))
                except TypeError:
                    print('interger input only')
                onVen.add(add_n,add_p)
                print('add successfully')
            elif ad_input == '2':
                print(onVen)
                rm_n = input('delete which product?\n').capitalize()
                if onVen.rm(rm_n) == True:
                    print('delete successfully')
                elif onVen.rm(rm_n) == False:
                    print('product is not in the list')

            elif ad_input == '3':
                    print(f'Total past profit is {sum(onVen.past)}')

            ### Change Password   
            elif ad_input == '4':
                if pw_check() == True:
                    pw_c = 0
                    new_pw1 = input('enter new password\n')
                    new_pw2 = input('enter new password again\n')
                    if new_pw1 == new_pw2:
                        pw_hash = hashlib.sha1(bytearray(new_pw1,'utf-8')).hexdigest()
                        print('new password has been set successfully')
                    
                    else:
                        print('inputs are different, please try again')
                        continue
            else:
                print('wrong command, try again')

### Wrong input
    elif bool(opt_input) == True and temp == True:
        print('Wrong command, please check your input')
    else:
        continue

##Google Spread Sheet (unused)
from google.colab import auth   #確認許可權
auth.authenticate_user()        #確認碼：4/1AX4XfWgoudtfS3Sk1Hnc5Xf4Rtyd9AU6-PALE6dAUIRxHJskVjmkulwmmF8
import gspread
from oauth2client.client import GoogleCredentials
#認證使用者
gc = gspread.authorize(GoogleCredentials.get_application_default())
sht1 = gc.open_by_key('1XzAuJsPHKSVfNTaMiGXAuD4QjOn5380TS13NxYIjz7k')