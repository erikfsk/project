from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def plot_3d_catch():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	X = np.linspace(2,70,690)
	Y = np.linspace(1,10,90)
	X, Y = np.meshgrid(X, Y)
	Z = 1-((100-X)/100.)**Y
	ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
	plt.show()

def write_to_file(filename="catch_chance.txt"):
	X = np.linspace(2,20,19)
	Y = np.linspace(1,10,10)
	X, Y = np.meshgrid(X, Y)
	Z = 1-((100-X)/100.)**Y
	outfile = open(filename,"w")
	print 
	print "  ",
	outfile.write("     ")
	for x in X[0]:
		print "%.5d"% x,
		outfile.write("%.6d  "% x)
	print
	outfile.write("\n")
	for y,z in zip(Y,Z):
		print "%.2d"%y[0],
		outfile.write("%.2d   "%y[0])
		for z_ in z:
			print "%.3f" % z_ ,
			outfile.write("%.4f  " % z_ )
		print
		outfile.write("\n")

if __name__ == '__main__':
	plot_3d_catch()
	write_to_file()
