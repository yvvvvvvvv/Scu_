class a():
    def na(self,name):
        return name
    def gen(self,gender):
        if gender=='F' or 'f':
            gender='Female'
        elif gender=='M' or 'm':
            gender='Male'
        else:
            gender='gender need F/M'
        return gender
    def de(self,department):
        x=department.title()
        return x
    def idd(self,id):
        return id
    def sk(self,skill):
        Ge=['C','C++','C#','JAVA']
        St=['Python','R']
        En=['Matlab','Fortran']
        if skill in Ge:
            sk='General_Programming'
        elif skill in St:
            sk='Statics_Programming'
        elif skill in En:
            sk='Engineering_Programming'
        else:
            sk='Other'
        return sk
while True:
    x1=input('請輸入姓名:')
    x2=input('請輸入性別(F/M):')
    x3=input('請輸入系所:')
    x4=input('請輸入學號:')
    x5=input('請輸入資訊專長(字首大寫):')
    y=a()
    print('Name:%s Gender:%s Department:%s ID:%s \nSkill:%s(%s)'%(y.na(x1),y.gen(x2),y.de(x3),y.idd(x4),y.sk(x5),x5))
    s=input('是否繼續(y/n):')
    if s == 'y' or s == 'Y':
        continue
    elif s == 'n' or s == 'N':
        break
    else:
        print('ERROR')
        break