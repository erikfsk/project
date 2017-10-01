def bilskilt(opptil,lengde):
	antall_bilskilt_med_like_sifre = {}
	for i in range(lengde):
		antall_bilskilt_med_like_sifre[i] = 0

	for i in range(opptil):
		i = str(i)
		bil = ((lengde-len(i))*"0"+i)
		counter = 0 
		for i in range(lengde):
			for j in range(i+1,lengde):
				if bil[i] == bil[j]:
					counter += 1
			if counter > 0:
				break
		antall_bilskilt_med_like_sifre[counter] += 1
	print lengde,antall_bilskilt_med_like_sifre

if __name__ == '__main__':
	for i in range(1,7):
		bilskilt(10**i,i)