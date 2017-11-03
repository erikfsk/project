# -*- coding: utf-8 -*-
from numpy import *

def sure_bets(odds):
	odds = [float(i) for i in odds]

	sannsynlighet = 0
	for i in range (len(odds)):
		sannsynlighet += 1/odds[i]

	if sannsynlighet < 1:
		bet = zeros(len(odds))
		nevner = sum(odds)
		for i in range (len(odds)):
			teller = 1.
			for j in range(len(odds)):
				if i != j:
					teller *= odds[j]
			bet[i] = teller/nevner

		for i in range(len(odds)):
			summen = odds[i]*bet[i] - sum(bet)
			print "Oddsen er %.2f --- Sats %.3fx --- Profit %.3fx" % (odds[i],bet[i],summen)

		print "Totalt satset %.3f. Totalt vunnet %.3f. Prosent profit %.3f / %.3f" % (sum(bet),odds[0]*bet[0],100*summen/sum(bet), 100*(1/sannsynlighet - 1))

	else:
		print "Oddsene er for dårlig. Du tjener ikke penger.", sannsynlighet

if __name__ == '__main__':
	sure_bets([	1.65,4.54,8.16])