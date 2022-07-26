import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress
from scipy.interpolate import make_interp_spline


def denne(fil):
    fail=fil

    infile=open(fail,'r')
    lines=infile.readlines()

    #print(lines)

    ge=[]       #gamma energy
    tgm=0       #total gamma multiplisties
    gm=[]       #gamma multipliseties

    fissions=lines[0].split()           #total number of fissions
    nr_fissions=float(fissions[3])

    i=1
    ingen=0
    #for i in range(len(lines)-2):
    while i<(len(lines)-2):
        v= lines[i+1].split()
        if float(v[0])==0:
            i+=1
        elif float(v[0])>0:
            gm.append(float(v[0]))
            i+=1
            v= lines[i+1].split()
            ingen=int(gm[-1])
            for j in range(ingen):
                ge.append(float(v[j]))
                tgm+=1
            i+=1

    #print(ge)
    #print(gm)
    ###ttgm=np.sum(gm)
    k=np.sum(ge)            # total gamma energi
    tge=k/nr_fissions       # total gamma energi pr fission
    #print(tge)
    gge=k/tgm               ##gjennomsnitt gamma energi
    #print(gge)

    k_m=np.sum(gm)
    gag=k_m/nr_fissions          #gjennomsnittlig antall gammaer per fisjon
    print(gag)

    #print(ge[1:],tgm,fissions[3])

    #plt.hist(ge[1:], bins = 1000,histtype='step',log=True)
    #plt.show()

    return (tge,gge,gag)

liste=['U0.dat','U01.dat','U02.dat','U1.dat','U2.dat','U3.dat','U4.dat','U5.dat','U6.dat','U7.dat','U8.dat','U9.dat','U10.dat','U11.dat','U12.dat','U13.dat',]
win=[]
energier=[25e-9,1,3,5.5,5.6,5.8,6,6.2,6.4,6.6,6.8,7,7.2,7.4,7.6,7.8]

for i in range(len(liste)):
    win.append(denne(liste[i]))
totge=[]
gjenge=[]
gjag=[]

for i in range(len(liste)):
    totge.append(win[i][0])
    gjenge.append(win[i][1])
    gjag.append(win[i][2])

plt.plot(energier,totge,'*')
plt.show()
plt.plot(energier,gjenge,'+')
plt.show()
plt.plot(energier,gjag)
plt.show()
