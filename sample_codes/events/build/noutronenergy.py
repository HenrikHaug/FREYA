import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress
from scipy.interpolate import make_interp_spline

infile=open('stest35.dat','r')
lines=infile.readlines()

#print(lines)

ge=[]
it=0
tgm=0
fissions=lines[0].split()
print(fissions[3])
for i in range(len(lines)):
    v= lines[i].split()
    if float(v[0])==0:
        it+=1
    elif float(v[0])>0:
        ge.append(float(v[0]))
        tgm+=1
fission=float(fissions[3])
k=np.sum(ge)
gje=k/fission
print(gje)
gge=k/tgm
print(gge)

#print(ge[1:],tgm,fissions[3])

plt.hist(ge[1:], bins = 1000,histtype='step',log=True)
plt.show()
