'''class Myschool():
    title = '東吳大學'
    def departments(self,a):
        self.name = a
        print('系所是',self.name,'喔')
x=Myschool()
print(x.title)
y=input('輸入系所:')
x.departments(y)'''

class Myschool():
    title = "東吳大學"
    def department(self, list):
        self.list = list
        print("屬性:", self.title, "系所:", self.list)

x = input("請輸入系所:")
y = Myschool()
y.department(x)
