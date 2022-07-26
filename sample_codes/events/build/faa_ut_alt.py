import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress
from scipy.interpolate import make_interp_spline


infile=open('Pu240.dat','r')
lines=infile.readlines()

#print(lines)

ge=[]       #gamma energy
tgm=0       #total gamma multiplisties
gm=[]       #gamma multipliseties
pfgm=[]
gml=[]
gmt=[]
gel=[]
get=[]

fissions=lines[0].split()           #total number of fissions
nr_fissions=float(fissions[3])

i=0
ingen=0
#for i in range(len(lines)-2):
while i<(len(lines)-3):
    i+=1
    v= lines[i].split()
    pfgm.append(float(v[0]))
    #print(pfgm)

    for k in range(2):
        i+=1
        v= lines[i].split()
        gm.append(float(v[0]))
        if k==0:
            gml.append(float(v[0]))
        if k==1:
            gmt.append(float(v[0]))
        if gm[-1]!=0:
            v= lines[i+1].split()
            ingen=int(gm[-1])
            #print(gm)
            for j in range(ingen):
                ge.append(float(v[j]))
                tgm+=1
                if k==0:
                    gel.append(float(v[j]))
                if k==1:
                    get.append(float(v[j]))

            i+=1
print(gml)
print(gmt)
print(gel)

plt.hist(gm, bins = 13,histtype='step')
plt.title('Gamma multiplisties')
plt.show()
