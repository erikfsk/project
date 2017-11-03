from numpy import *
def sure_bets(odds):
	odds = array([float(i) for i in odds])
	sannsynlighet = sum(1./odds)
	bet = 1./(sannsynlighet*odds)
	for bet_i,odds_i in zip(bet,odds):
		print "Oddsen er %.2f --- Sats %.5f --- Vunnet %.5f" % (odds_i,bet_i,odds_i*bet_i)
	print "Totalt satset %.5fx. \nTotalt vunnet %.5fx. \nProsent vunnet %.3f / %.3f" % (sum(bet),odds[0]*bet[0],100*odds[0]*bet[0]/sum(bet), 100*(1/sannsynlighet))
if __name__ == '__main__':
	sure_bets([1.9,2.3,20])