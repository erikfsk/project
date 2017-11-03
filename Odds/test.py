from matplotlib.pyplot import *

atoms = [1,13,55,147,309,561,923,1415,2057,2869,3861,5083,49000,404000,1380000,3280000]
shell = [1,2,3,4,5,6,7,8,9,10,11,12,25,50,75,100]

for i in range(len(atoms)):
	atoms[i] = atoms[i]**0.333

print atoms

plot(shell,atoms)
show()

