mean(CO2$conc,na.rm=FALSE) ##435
median(CO2$conc,na.rm=FALSE)

range(CO2$conc,na.rm=FALSE)
sd(CO2$conc,na.rm=FALSE)

mean(CO2$conc,na.rm=FALSE,trim=0.1)##408
##�t�Z���j ���ӨS������

cor(CO2$conc,CO2$uptake)##0.4851774
##�O�s�� �X�A
cor(CO2$conc,CO2$uptake,method='spearman')##0.5800041
##�۸�pearson pearson��n
cor(CO2$conc,CO2$uptake,method='kendall')##0.4490871
##���X�A