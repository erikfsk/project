# -*- coding: utf-8 -*-

def sure_bets(odds):
	odds = [float(i) for i in odds]
	sannsynlighet = 0
	
	for i in range (len(odds)):
		sannsynlighet += 1/odds[i]

	bet = []
	for i in range (len(odds)):
		bet.append(1./(sannsynlighet*odds[i]))
		print "Oddsen er %.2f --- Sats %.5f --- Vunnet %.5f" % (odds[i],bet[i],odds[i]*bet[i])

	print "Totalt satset %.5fx. Totalt vunnet %.5fx. Prosent vunnet %.3f / %.3f" % (sum(bet),odds[0]*bet[0],100*odds[0]*bet[0]/sum(bet), 100*(1/sannsynlighet))

if __name__ == '__main__':
	sure_bets([	1.65,4.54,8.16])

print 1.0/7