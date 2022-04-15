a={'tag':'red','score':3,'speed':'slow'}
b=[]
for x in range(50):
    b.append(a)
    #print(b)
d=35
for y in range(3):
    b[d]={'tag':'blue','score':5,'speed':'medium'}
    #b['tag']='blue'
    #b['score']=5
    #b['speed']='medium'
    d+=1
#print(b[35:39])
print(b[19:40])