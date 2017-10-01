from matplotlib.pyplot import *

def bilskilt(opptil,lengde):
	antall_bilskilt_med_like_sifre = {}
	bilskilt = []
	for i in range(opptil):
		i = str(i)
		bilskilt.append(((lengde-len(i))*"0"+i))

	for i in range(lengde):
		antall_bilskilt_med_like_sifre[i] = 0

	for bil in bilskilt:
		counter = 0 
		for i in range(len(bil)):
			for j in range(i+1,len(bil)):
				if bil[i] == bil[j]:
					counter += 1
			if counter > 0:
				break
		antall_bilskilt_med_like_sifre[counter] += 1

	print lengde,antall_bilskilt_med_like_sifre

if __name__ == '__main__':
	None
	for i in range(1,7):
		bilskilt(10**i,i)
"""
listen = []
listen.append({0: 10})
listen.append({0: 90, 1: 10})
listen.append({0: 720, 1: 270, 2: 10})
listen.append({0: 5040, 1: 4590, 2: 360, 3: 10})
listen.append({0: 30240, 1: 61560, 2: 7740, 3: 450, 4: 10})
listen.append({0: 151200, 1: 708930, 2: 127620, 3: 11700, 4: 540, 5: 10})
listen.append({0: 604800, 1: 7371900, 2: 1777590, 3: 228600, 4: 16470, 5: 630, 6: 10})
listen.append({0: 1814400, 1: 71976150, 2: 22092930, 3: 3721950, 4: 371790, 5: 22050, 6: 720, 7: 10})

for dicts in listen:
	summen = 100./sum(dicts.values())
	for key in sorted(dicts.keys()):
		value = dicts[key]
		dicts[key] = value*summen


for dicts in listen:
	plot(dicts.keys(),dicts.values(),"o-")
grid("on")
show()
"""