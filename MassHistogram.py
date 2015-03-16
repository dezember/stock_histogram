#%matplotlib inline
import pandas as pd
from glob import glob 
import urllib2, sys
import cookielib
from matplotlib.pylab import plot as plt
from matplotlib.pyplot import hist, show, savefig, title, clf
import timeit
from datetime import datetime
start=datetime.now()


#def pilotplot(highlow,comp_name):


flist=glob("./csv/*.csv")

for company in flist:
	df=pd.read_csv(company)
	highlow=df['High Price']-df['Low Price']
	comp_name=str(df['Symbol'][1])
	price=str(df['Open Price'][150])
	hist(highlow,100)
	title(str(comp_name)+" "+price)
	savefig('./pngs/'+comp_name+'.png')
	clf()

print datetime.now()-start
