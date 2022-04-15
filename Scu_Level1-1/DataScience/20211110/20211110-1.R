data()##檢視內建資料夾
x1<-CO2$conc##呼叫CO2裡面的conc變數
x2<-Co2[,'conc']##呼叫CO2裡面的conc變數
x3<-CO2$conc[c(1,5,7,9)]##呼叫CO2裡面的conc變數1,5,7,9
##name(x3)<-c('a','b','c','d')
x4<-CO2$conc[c(1:10)]##呼叫CO2裡面的conc變數1~10筆
##view()

palette(rainbow(15)) ##R默認8種顏色 修改彩虹色
palette(heat.colors(15))##改紅到黃
palette(terrain.colors(15))##綠到棕到白
palette(topo.colors(15))##深藍到淺棕
palette(cm.colors(15))##淺藍到白到淺紫
palette(grey.colors(15))##灰

plot(CO2$conc[c(1:15)],col=1:15)##點圖
barplot(CO2$conc[c(1:15)],col=1:15)##柱狀圖
plot(CO2$conc,type='p',cex=3,col=1:15,type='l',lwd=3,lty=1,xlab='A',yalb='B')
##繪製p點圖 l折線圖 o點加折
lines(CO2$conc,col=1)##加上對比線

pie(table(CO2$Treatment))##餅圖
boxplot(AirPassengers)##箱型圖
table(CO2$Treatment)##數量
x6<-table(CO2$Treatment)
pie(x6)
pie(table(CO2$conc),col=5:10)

x1<-CO2$conc
x2<-CO2$uptake
x7<-c(x1,x2)##合併x1x2 x7<-c(CO2$conc,CO2uptake)
par(mfrow=c(2,2))#圖形排列行數
par(mfcol=c(2,3))#圖形排列列數
plot(x1,type='l',col='red')
plot(x1,type='l',col='green')
plot(x1,type='l',col='blue')
plot(x1,type='l',col='gray')
par(mfrow=c(1,2))##一行兩列(橫行直列)
