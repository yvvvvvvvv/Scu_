n=eval(input("請輸入三角形的高度:"))
for i in range(n):  # 以range()函數產生的整數序列
    for a in range(n-i-1):  # 使用for迴圈，產生從n-i-1到0的整數序列
        print(" ",end="")  # 根據不同層數，讓第一個數字前方增加指定的空字串
    for w in range(i+1,1,-1): # 產生從i+1到1的整數序列，並由大到小的迴圈 
        print (w,end='')  # 在1的左邊印出數字
    for s in range(1,i+2):  # 產生從1到i+2的整數序列迴圈
        print(s, end='')  # 在1的右邊印出數字
    print("\n", end="")    # 執行換行