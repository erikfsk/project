def combinasions_with_symmetric_letters(max_length):
	#bokstaver = ["I","O","X"] #x and y symmetric
	#bokstaver = ["B","C","D","E","H","I","K","O","X"] #x symmetric
	bokstaver = ["A","H","I","M","O","T","U","V","W","X","Y"] #y symmetric
	#bokstaver = ["A","B","C","D","E","H","I","K","M","O","T","U","V","W","X","Y"] #x symmetric and y symmetric
	all_combinasions = {}
	for i in range(1,max_length*2 - 1):
		all_combinasions[i] = []

	def rekur(maks_antall_tegn,text):
		if maks_antall_tegn == 0:
			x,y = text+text[::-1],text[:-1]+text[::-1]
			x_length = len(x)
			y_length = x_length-1
			if x not in all_combinasions[x_length]:
				all_combinasions[x_length].append(x)
			if y not in all_combinasions[y_length]:
				all_combinasions[y_length].append(y)
		else:
			for j in bokstaver:
				rekur(maks_antall_tegn-1,text+j)

	for i in range(1,max_length):
		rekur(i,"")

	return all_combinasions

if __name__ == '__main__':
	alle_komboer = combinasions_with_symmetric_letters(5)
	with open("surnames.txt","r") as infile:
		lines = infile.readlines()
		for line in lines:
			name = line.split()[0].strip()
			name_length = len(name)
			if name_length <= 8:
				if name in alle_komboer[name_length]:
					print name

"""
$ time python symmetriske_navn.py 
11
11
121
121
1331
1331
14641
14641
161051
161051
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

real	6m50.333s
user	6m45.243s
sys		0m1.577s
"""