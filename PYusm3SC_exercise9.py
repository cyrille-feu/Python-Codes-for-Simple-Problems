"""this program compute an plot two graph with given formula"""


import numpy as np                            # import numpy library
import pylab as pl                            # import pylab library
kmax1=6
kmax2=26
y1=np.zeros(200)                              # create two vectors with 200 zeros elements                   
y2=np.zeros(200)
x=np.linspace(-2,2,200)                       # create a vector x with 200 elements belong [-2,2]
for k in range(1,kmax1,2):
	y1+=(4/(k*np.pi))*(np.sin((k*np.pi*x)/2)) # compute our formula with the two values of kmax
for k in range(1,kmax2,2):
	y2+=(4/(k*np.pi))*(np.sin((k*np.pi*x)/2))
pl.grid()                                     # grid our figure
pl.plot( x, y1,'r',label="$k_{max}=6$")       # plot our first graph
pl.plot( x, y2,'g',label="$k_{max}=26$")      # plot the second graph
pl.xlabel(' x axis')                          # name x axis
pl.ylabel(' y axis')                          # name y axis
pl.legend(loc='best')                         # locate legend
pl.title( "plot over somation")               # name title
pl.show()                                     # show the two graph in same figure




