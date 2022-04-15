def substract (x1,x2,x3):
    if x3 =="+":
        result=x1 + x2
    if x3 =="-":
        result=x1 - x2
    if x3 =="*":
        result=x1 * x2
    if x3 =="/":
        result=x1 / x2
    print(result)


while True:
    x=input("輸入1進行+-*/ 的運算，輸入其他都會結束本程式:")
    if x !="1":
        print("結束本程式")
        break
    a=int(input("a = "))
    b=int(input("b = "))
    c=input("運算子(+-*/) = ")
    if c == "+" or "-" or "*" or "/":
        print(a,c,b,"= ",end='')
        substract(a,b,c)