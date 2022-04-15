#分布分析
hist(CO2$uptake, freq = F)##頻率分配直方圖
hist(CO2$uptake, freq = T)##次數分配直方圖

pie(table(CO2$Treatment))##餅圖

#對比分析
plot(Orange$circumference,cex = 3,col=1:15,type='l',lwd=3,lty=1,xlab='A',ylab="B")
##繪製p點圖 l折線圖 o點加折
lines(BJsales,col=2)##加上對比線

#統計量分析
mean(AirPassengers)
mean(AirPassengers, trim = 0)##trim:從排序的向量的兩端刪除觀測值,trim=0.3:10個刪除三個
mean(AirPassengers, trim = 0, na.rm = FALSE)##na.rm:移除na

median(AirPassengers,na.rm=FALSE)##中位數

as.numeric(names(table(CO2$conc)))[which.max(table(conc))]##眾數

range(AirPassengers)##全距
range(AirPassengers,na.rm=FALSE)

sd(AirPassengers)##標準差
sd(AirPassengers,na.rm = FALSE)

cv<-100*sd(AirPassengers)/mean(AirPassengers)##變異係數
cv
cv1<-100*sd(BJsales)/mean(BJsales)
cv1

#週期性分析_時間序列趨勢
apts<-ts(AirPassengers, frequency = 12)
f<-decompose(apts)##季節性分解
print(f$figure)
plot(f$figure,type='b',xaxt='n',xlab='')

plot(f)

#相關性分析_相關係數
cor(CO2$conc, CO2$uptake)##conc和uptake的相關係數(pearson)
cor(CO2$conc, CO2$uptake, method = 'spearman')
cor(CO2$conc, CO2$uptake, method = 'kendall')


