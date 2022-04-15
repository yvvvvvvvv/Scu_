class Myschool():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def a(self):
        return self.name
    def b(self):
        return self.score

x1=input('姓名:')
x2=input('成績')
x=Myschool(x1,x2)
print('Hi!%s的成績是%s'%(x.a(),x.b()))
