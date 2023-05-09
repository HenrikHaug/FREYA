from __future__ import division
from subprocess import Popen, PIPE, call
import os
import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress

Ex=[-4,-5,-6]
mean=[9,7,5]
sigma=[2,3,1]

print("Running FREYA with Smean: %.d  Ssigma %.d" % (mean[0], sigma[0]))
p = Popen('./events', stdin=PIPE)
p.communicate(os.linesep.join(["92", "235", "%f" % Ex[0], "100000", "Pu240.dat", "%d" % mean[0], "%d" % sigma[0]]))

#lese fra fil
infile=open('Pu240.dat','r')
lines=infile.readlines()

fissions=lines[0].split()           #total number of fissions
nr_of_fissions=float(fissions[3])   #total number of fissions

ex_induced=[]
initial_spin=[]
ex_lett=[]
spin_lett=[]
ex_tot1=[]
ex_tot2=[]
ex_tung=[]
spin_tung=[]
ex_tot=[]
JvsEx=[]
i=0
z=0
av_energi=np.zeros(17)
lengden=np.zeros(17)
spin_list=[]

for i in range(17):
    spin_list.append(i)
    #lengden[i]=1
    #av_energi[i]=1
i=0
while i<(len(lines)-3):
    v= lines[i].split()
    ex_induced.append(float(v[0]))
    initial_spin.append(float(v[1]))
    for k in range(3):
        i+=1
        #print(i)
        v= lines[i].split()
        if k==0:
            z=2
        if k==1:
            ex_lett.append(float(v[0]))
            spin_lett.append(float(v[1]))
            ex_tot1.append(float(v[0]))
        if k==2:
            ex_tung.append(float(v[0]))
            spin_tung.append(float(v[1]))
            #print(spin_tung)
            ex_tot2.append(float(v[0]))
#print(spin_tung)

#print(spin_tung)
for i in range(len(spin_tung)):
    ex_tot.append(float((ex_tot1[i]+ex_tot2[i])/2.0))
    if spin_tung[i]==0.0:
        av_energi[0]+=ex_tung[i]
        lengden[0]+=1.0
    if spin_tung[i]==1.0:
        av_energi[1]+=ex_tung[i]
        lengden[1]+=1.0
    if spin_tung[i]==2.0:
        lengden[2]+=1
        av_energi[2]+=ex_tung[i]
    if spin_tung[i]==3.0:
        lengden[3]+=1.0
        av_energi[3]+=ex_tung[i]
    if spin_tung[i]==4.0:
        lengden[4]+=1.0
        av_energi[4]+=ex_tung[i]
    if spin_tung[i]==5.0:
        lengden[5]+=1.0
        av_energi[5]+=ex_tung[i]
    if spin_tung[i]==6.0:
        lengden[6]+=1.0
        av_energi[6]+=ex_tung[i]
    if spin_tung[i]==7.0:
        lengden[7]+=1.0
        av_energi[7]+=ex_tung[i]
    if spin_tung[i]==8.0:
        lengden[8]+=1.0
        av_energi[8]+=ex_tung[i]
    if spin_tung[i]==9.0:
        lengden[9]+=1.0
        av_energi[9]+=ex_tung[i]
    if spin_tung[i]==10.0:
        lengden[10]+=1.0
        av_energi[10]+=ex_tung[i]
    if spin_tung[i]==11.0:
        lengden[11]+=1.0
        av_energi[11]+=ex_tung[i]
    if spin_tung[i]==12.0:
        lengden[12]+=1.0
        av_energi[12]+=ex_tung[i]
    if spin_tung[i]==13.0:
        lengden[13]+=1.0
        av_energi[13]+=ex_tung[i]
    if spin_tung[i]==14.0:
        lengden[14]+=1.0
        av_energi[14]+=ex_tung[i]
    if spin_tung[i]==15.0:
        lengden[15]+=1.0
        av_energi[15]+=ex_tung[i]
    if spin_tung[i]==16.0:
        av_energi[16]+=ex_tung[i]
        lengden[16]+=1.0

#print(lengden[6])
#print(av_energi)
#print(av_energi[6])
print(lengden[6],av_energi[6])
for i in range(17):
    av_energi[i]=av_energi[i]/lengden[i]

#print(av_energi)
#print(8020/2005)
plt.plot(spin_list,av_energi,'*')
plt.show()

#print(len(spin_tung),ex_tot)

plt.plot(spin_tung,ex_tot,'*')
plt.show()

#plt.hist(JvsEx, bins = 20 ,histtype='step')
#plt.show()

plt.hist(spin_tung, bins = 20 ,histtype='step')
plt.show()

#plt.plot()


#plt.plot(ex_tot[:-6],JvsEx,'*')
#plt.show()

#trying to committ Jeg er dum
