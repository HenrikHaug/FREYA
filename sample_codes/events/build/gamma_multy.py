import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress
from scipy.interpolate import make_interp_spline

infile=open('stest40.dat','r')
lines=infile.readlines()

#print(lines)
gmult=np.zeros((len(lines)))
nrfission=(lines[0].split())
print(nrfission[3])
for i in range(len(lines)):
    v= lines[i].split()
    gmult[i]=float(v[0])

nrf=float(nrfission[3])
k=np.sum(gmult)
gg=k/nrf                        #gjennomsnittlig antall gammaer per fisjon
print(gg)

#print(ge[1:],tgm,fissions[3])

plt.hist(gmult[1:], bins = [1,2,3,4,5,6,7,8,9,10,11,12],histtype='step',log=True)
plt.show()
