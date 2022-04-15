#def a(): 如果()內元素數量不定 a(*x)
#nested籤套函數:函數內可以有函數
def outer():
    b=10
    def inner(x):
        return 5*x+b #引用第三行的b
    return inner

b=2
f=outer() #回傳inner
print(f(b)) #f(2)建立了5*x+b