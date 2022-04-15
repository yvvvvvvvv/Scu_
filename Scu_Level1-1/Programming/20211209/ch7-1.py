##For in 持續跑直到list為空 ##For var 
players=['curry','james','jordan']
for x in players:
    print(x.title(),'is a good player')
    ##Curry is a good player
    ##James is a good player 
    ##Jordan is a good player
files=['d1.c','d2.py','d3.py','d4.java']
py=[]
for file in files:
    if file.endswith('.py'): #end's'with
        py.append(file)
print(py)
#test uif a list is a 可迭代物件 iter('string')
