x1<-c(1,2,3,4)
x2<-c('a','b','c','d')
x3<-c(TRUE,FALSE,FALSE,TRUE)
x1<-c(2,3,4,5,6)
#說明文字 一起執行不會執行
x1<-c(1,2,3,4)
is.numeric(x1)
#is.numeric()測是否數值
rm(x2)
#remove
#all remove = rm(list = Is(all = Ture))
#ctrl+l clean console
data()
getwd()
setwd()
#getwd()查看當前工作位置
#setwd()設置(同上)
file.choose()
#file.choose()字面意思
#View要打下面 V要大寫
#conc <- CO2$conc (CO2中的conc)
is.numeric(conc)
is.numeric(CO2$conc)
#plot()畫圖 如果不設定圖形 他會自己用他偵測到的資料類型給圖
