Sys.getlocale()
sessionInfo()
Sys.setlocale(category = 'LC_ALL', locale='UTF-8')
install.packages("quantmod")
library(quantmod)
getSymbols("AAPL",src="yahoo")