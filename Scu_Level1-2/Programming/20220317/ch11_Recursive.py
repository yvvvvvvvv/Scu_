def factorial(n):
    #計算n階乘
    if n==1:
        return 1 ##終止
    else:
        return (n*factorial(n-1)) ##recursive fun.
