data()##�˵����ظ�Ƨ�
x1<-CO2$conc##�I�sCO2�̭���conc�ܼ�
x2<-Co2[,'conc']##�I�sCO2�̭���conc�ܼ�
x3<-CO2$conc[c(1,5,7,9)]##�I�sCO2�̭���conc�ܼ�1,5,7,9
##name(x3)<-c('a','b','c','d')
x4<-CO2$conc[c(1:10)]##�I�sCO2�̭���conc�ܼ�1~10��
##view()

palette(rainbow(15)) ##R�q�{8���C�� �ק�m�i��
palette(heat.colors(15))##������
palette(terrain.colors(15))##���Ĩ��
palette(topo.colors(15))##�`�Ũ�L��
palette(cm.colors(15))##�L�Ũ�ը�L��
palette(grey.colors(15))##��

plot(CO2$conc[c(1:15)],col=1:15)##�I��
barplot(CO2$conc[c(1:15)],col=1:15)##�W����
plot(CO2$conc,type='p',cex=3,col=1:15,type='l',lwd=3,lty=1,xlab='A',yalb='B')
##ø�sp�I�� l��u�� o�I�[��
lines(CO2$conc,col=1)##�[�W���u

pie(table(CO2$Treatment))##���
boxplot(AirPassengers)##�c����
table(CO2$Treatment)##�ƶq
x6<-table(CO2$Treatment)
pie(x6)
pie(table(CO2$conc),col=5:10)

x1<-CO2$conc
x2<-CO2$uptake
x7<-c(x1,x2)##�X��x1x2 x7<-c(CO2$conc,CO2uptake)
par(mfrow=c(2,2))#�ϧαƦC���
par(mfcol=c(2,3))#�ϧαƦC�C��
plot(x1,type='l',col='red')
plot(x1,type='l',col='green')
plot(x1,type='l',col='blue')
plot(x1,type='l',col='gray')
par(mfrow=c(1,2))##�@���C(��檽�C)