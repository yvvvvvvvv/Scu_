N=int(input("請輸入欲排序之數字個數:")) 
a=int(input("請輸入整數值域最小值:"))
b=int(input("請輸入整數值域最大值:"))
z=[] # 隨機產生的數字，儲存在串列裡

while (b+1-a)<N:    # 當(b+1-a)小於N時，就執行while迴圈，大於N時就跳出迴圈
    N=int(input("請輸入欲排序之數字個數:"))
    a=int(input("請輸入整數值域最小值:"))
    b=int(input("請輸入整數值域最大值:"))
else:
    import random # 匯入random模組

    z=random.sample(range(a,b+1),N) # 從a到b中隨機取出N筆資料
    print("隨機產生之數列為:",z)
    def qsort(z,left,right): # 定義快速排序遞迴的主函式，輸入資料從左右兩邊開始
        if left >= right:  # 如果左邊大於等於右邊，就跳出function
            return
        i=left  # 把i儲存起來,上面的主函式的left不變
        j=right  # 把j儲存起來,上面的主函式的right不變
        key=z[left]  # 基準點
    
        while i!=j: # 當左右指標未碰頭時就一直比較移動下去
            while z[j]>= key and i<j: # 從右邊開始,如果大於等於Key:
                j-=1  #right左移一位,繼續比較
            while z[i]<= key and i<j: # 從左邊開始,如果小於等於Key:
                i+=1  #left右移一位,繼續比較
            if i <j:  # 若移動完，二者仍未碰頭則交換對應的值
                w=z[i]
                z[i]=z[j]
                z[j]=w

        z[left]=z[i]  # 將基準點與與相遇點互換
        z[i]=key
        
        qsort(z,left,i-1)  # 遞迴處理左半部
        qsort(z,i+1,right)  # 遞迴處理右半部
    
qsort(z,0,len(z)-1) 
print("排序後之數列為:",z)