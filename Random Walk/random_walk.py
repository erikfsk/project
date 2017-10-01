from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import * 
from random import * 
from numpy import *

def random_walk(M,d2=False,d3=True):
	x = zeros(M)
	y = zeros(M)

	if d2:
		for i in xrange(1,int(M)):
			a = randint(1,2)
			if a == 1:
				x[i] = x[i-1] + randrange(-1,2,2)
				y[i] = y[i-1]
			else:
				x[i] = x[i-1]
				y[i] = y[i-1] + randrange(-1,2,2)
		plot(x,y,"k-")
		show()
		return x,y

	if d3:
		z = zeros(M)
		for i in xrange(1,int(M)):
			a = randint(1,3)
			if a == 1:
				x[i] = x[i-1] + randrange(-1,2,2)
				y[i] = y[i-1]
				z[i] = z[i-1]
			elif a == 2:
				x[i] = x[i-1]
				y[i] = y[i-1] + randrange(-1,2,2)
				z[i] = z[i-1]
			else:
				x[i] = x[i-1]
				y[i] = y[i-1]
				z[i] = z[i-1] + randrange(-1,2,2)
		fig = figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_wireframe(x,y,z)
		show()
		return x,y,z


if __name__ == '__main__':
	random_walk(1e2)