from matplotlib.pyplot import *
from numpy import *


antall_kast = 15
x = linspace(1,antall_kast,antall_kast)
x2 = linspace(0,antall_kast-1,antall_kast)
y = 1-((1./2.)**(1./x))


X = []
Y = []
for x_,y_ in zip(x,y):
	X.append(x_-1)
	X.append(x_)
	Y.append(y_)
	Y.append(y_)
	print "%.d %.2f"% (x_,y_*100)

plot(X,Y,"r-")
ylim(0,0.51)
show()