prime = [2,3] ; new_possible_prime = 3 ; N = 100000; Len = 2
infile = open("primes.txt","w")

def f():
	for i in prime:
		if i <= npp05:
			if new_possible_prime % i == 0:
				return 1
		else:
			return 0

while Len<N:
	new_possible_prime = new_possible_prime + 2
	npp05 = new_possible_prime**(0.5)
	if f() == 0:
		Len += 1
		prime.append(new_possible_prime)
		infile.write("%.f %6.f \n" %(Len, new_possible_prime))