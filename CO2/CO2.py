from numpy import * 
from matplotlib.pyplot import *

def pust(measurements = [2,2,2],breath_per_min = 12.,time = 8.,n_persons = 1,O2_dead=0.06
		,O2_prosent = 0.209,CO2_prosent = 0.0004,Others_prosent = 0.7906,Liters_of_air_per_breath = 0.4):

	if len(measurements) % 3 != 0 or len(measurements) == 0:
		print "measurements should be a list of measurements in meters. \
				example: [length1,width1,heigth1,length2,width2,heigth2,...]"
		quit()

	Liters_of_air = 0;

	for i in range(0,len(measurements),3):
		Liters_of_air += 1000*measurements[i]*measurements[i+1]*measurements[i+2]

	CO2_omdannelse_per_min = 0.25*n_persons*Liters_of_air_per_breath*breath_per_min*O2_prosent
	print "----------------------"
	print CO2_omdannelse_per_min,O2_prosent*Liters_of_air

	t = linspace(0,time,time*60*12 +1)
	O2= (O2_prosent*Liters_of_air - t*60*12*CO2_omdannelse_per_min)/float(Liters_of_air)
	CO2= (CO2_prosent*Liters_of_air + t*60*12*CO2_omdannelse_per_min)/float(Liters_of_air)
	Others = (Others_prosent + t*0)
	Dead = t*0 + O2_dead

	if O2[-1] <= O2_dead:
		print "The O2 procentage is below %.1f. You are dead!" % (O2_dead*100)

	return t,O2,CO2,Others,Dead


if __name__ == '__main__':
	#room BS measurements = [2.3,3.6,2.8,1.8,0.6,2.8,0.8,1.6,2.8]
	t,O2,CO2,Others,Dead = pust(measurements = [2.3,3.6,2.8,1.8,0.6,2.8,0.8,1.6,2.8],
	 	n_persons=2,breath_per_min=12)
	print O2[0]*100,O2[-1]*100
	t,O2,CO2,Others,Dead = pust(measurements = [2.3,3.6,2.8,1.8,0.6,2.8,0.8,1.6,2.8],
		n_persons=2,breath_per_min=10)
	print O2[0]*100,O2[-1]*100
	plot(t,O2,"g-",t,CO2,"r-",t,Others,"b-",t,Dead,"k-")
	legend(["$O_2$","$CO_2$","Other gases","Dead"])
	show()


"""
17 percent = mental abilities become impaired. 
16 percent = noticeable changes to your beings 
14 percent = extreme exhaustion from physical activity. 
10 percent = very nauseous or lose consciousness. 
6 percent  = humans won't survive
"""