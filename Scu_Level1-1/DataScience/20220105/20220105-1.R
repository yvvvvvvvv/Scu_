mean(CO2$conc,na.rm=FALSE) ##435
median(CO2$conc,na.rm=FALSE)

range(CO2$conc,na.rm=FALSE)
sd(CO2$conc,na.rm=FALSE)

mean(CO2$conc,na.rm=FALSE,trim=0.1)##408
##差距不大 應該沒有極值

cor(CO2$conc,CO2$uptake)##0.4851774
##是連續型 合適
cor(CO2$conc,CO2$uptake,method='spearman')##0.5800041
##相較pearson pearson更好
cor(CO2$conc,CO2$uptake,method='kendall')##0.4490871
##不合適
