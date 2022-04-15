#�������R
hist(CO2$uptake, freq = F)##�W�v���t�����
hist(CO2$uptake, freq = T)##���Ƥ��t�����

pie(table(CO2$Treatment))##���

#�����R
plot(Orange$circumference,cex = 3,col=1:15,type='l',lwd=3,lty=1,xlab='A',ylab="B")
##ø�sp�I�� l��u�� o�I�[��
lines(BJsales,col=2)##�[�W���u

#�έp�q���R
mean(AirPassengers)
mean(AirPassengers, trim = 0)##trim:�q�ƧǪ��V�q����ݧR���[����,trim=0.3:10�ӧR���T��
mean(AirPassengers, trim = 0, na.rm = FALSE)##na.rm:����na

median(AirPassengers,na.rm=FALSE)##�����

as.numeric(names(table(CO2$conc)))[which.max(table(conc))]##����

range(AirPassengers)##���Z
range(AirPassengers,na.rm=FALSE)

sd(AirPassengers)##�зǮt
sd(AirPassengers,na.rm = FALSE)

cv<-100*sd(AirPassengers)/mean(AirPassengers)##�ܲ��Y��
cv
cv1<-100*sd(BJsales)/mean(BJsales)
cv1

#�g���ʤ��R_�ɶ��ǦC�Ͷ�
apts<-ts(AirPassengers, frequency = 12)
f<-decompose(apts)##�u�`�ʤ���
print(f$figure)
plot(f$figure,type='b',xaxt='n',xlab='')

plot(f)

#�����ʤ��R_�����Y��
cor(CO2$conc, CO2$uptake)##conc�Muptake�������Y��(pearson)
cor(CO2$conc, CO2$uptake, method = 'spearman')
cor(CO2$conc, CO2$uptake, method = 'kendall')

