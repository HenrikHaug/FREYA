from __future__ import division
from subprocess import Popen, PIPE, call
import os
import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress
#from scipy.interpolate import make_interp_spline


def Fraya_kjore(Ex):
    Ex=Ex


    Tot_Ga_energy_pr_fis_l=[]
    Gj_Ga_energy_l=[]
    Gj_Ga_pr_fis_l=[]
    Ga_E_T=[]
    Ga_multy_T=[]
    '''
    Ga_E=[]                 #gamma energy
    T_Ga_multy=0.0          #total gamma multiplisties
    Ga_multy=[]             #gamma multipliseties

    Tot_Ga_energy_pr_fis=[]
    Gj_Ga_energy=[]
    Gj_Ga_pr_fis=[]
    '''
    print(len(Ex))
    for i in range(len(Ex)):

        p = Popen('./events', stdin=PIPE)
        p.communicate(os.linesep.join(["92", "235", "%f" % Ex[i], "100000", "Pu240.dat"]))


        #lese fra fil
        infile=open('Pu240.dat','r')
        lines=infile.readlines()

        #total number of fissions
        fissions=lines[0].split()           #total number of fissions
        nr_of_fissions=float(fissions[3])   #total number of fissions
        #print(nr_of_fissions)
        Ga_E=[]                 #gamma energy
        T_Ga_multy=0.0          #total gamma multiplisties
        Ga_multy=[]             #gamma multipliseties
        pfgm=[]                 #pre fission gammas
        gml=[]                  # gamma multiplisity lett fragment
        gmt=[]                  # gamma multiplisity lett fragment
        gel=[]
        get=[]


        i=0
        ingen=0
        #for i in range(len(lines)-2):
        '''
        while i<(len(lines)-2):
            v= lines[i+1].split()
            if float(v[0])==0:
                i+=1
            elif float(v[0])>0:
                Ga_multy.append(float(v[0]))
                Ga_multy_T.append(float(v[0]))
                i+=1
                v= lines[i+1].split()
                ingen=int(Ga_multy[-1])
                for j in range(ingen):
                    Ga_E.append(float(v[j]))
                    Ga_E_T.append(float(v[j]))
                    T_Ga_multy+=1.0
                i+=1
        '''
        while i<(len(lines)-3):
            i+=1
            v= lines[i].split()
            pfgm.append(float(v[0]))        #pre fission gammas

            for k in range(2):
                i+=1
                v= lines[i].split()
                Ga_multy.append(float(v[0]))
                Ga_multy_T.append(float(v[0]))
                if k==0:
                    gml.append(float(v[0]))
                if k==1:
                    gmt.append(float(v[0]))
                if Ga_multy[-1]!=0:
                    v= lines[i+1].split()
                    ingen=int(Ga_multy[-1])
                    for j in range(ingen):
                        Ga_E.append(float(v[j]))
                        Ga_E_T.append(float(v[j]))
                        T_Ga_multy+=1.0
                        if k==0:
                            gel.append(float(v[j]))
                        if k==1:
                            get.append(float(v[j]))
                    i+=1


        Tot_Ga_energy=np.sum(Ga_E)
        #print(Tot_Ga_energy)
        Tot_Ga_energy_pr_fis=(Tot_Ga_energy/nr_of_fissions)
        print(Tot_Ga_energy_pr_fis)
        Tot_Ga_multy=np.sum(Ga_multy)

        Gj_Ga_energy=(Tot_Ga_energy/Tot_Ga_multy)
        Gj_Ga_pr_fis=(T_Ga_multy/nr_of_fissions)          #gjennomsnittlig antall gammaer per fisjon
        print(Gj_Ga_pr_fis)

        Tot_Ga_energy_pr_fis_l.append(Tot_Ga_energy_pr_fis)
        Gj_Ga_energy_l.append(Gj_Ga_energy)
        Gj_Ga_pr_fis_l.append(Gj_Ga_pr_fis)


        #til jorgen
        print(np.sum(gml)/len(gml))
        print(np.sum(gmt)/len(gmt))
        print(np.sum(gel)/len(gml))
        print(np.sum(get)/len(gmt))
        print(np.shape(gml),np.shape(gmt),np.shape(gel),np.shape(get))
        print(len(gml))
        print(np.sum(Ga_E)/len(Ga_E))
    return (Tot_Ga_energy_pr_fis_l,Gj_Ga_energy_l,Gj_Ga_pr_fis_l,Ga_E_T,Ga_multy_T)


Ex=[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.25,5.5,5.75,6.25,6.5,6.75,7.0,7.25] #input energy to FREYA-> neutron energy if neutron induced, excitation energy if spontaneous fission
Ex=[0.01,0.02,0.03,0.1]


Tot_Ga_energy_pr_fis_l, Gj_Ga_energy_l, Gj_Ga_pr_fis_l, Ga_E_T, Ga_multy_T=Fraya_kjore(Ex)
print(Gj_Ga_energy_l,Tot_Ga_energy_pr_fis_l)


plt.plot(Ex,Tot_Ga_energy_pr_fis_l,'*',label="Total Gamma energy per fission")
plt.title('Total Gamma energy per fission')
plt.show()

plt.plot(Ex,Gj_Ga_energy_l,'*',label="Gjennomsnitt Gamma energy")
plt.title('Gjennomsnitt Gamma energy')
plt.show()

plt.plot(Ex,Gj_Ga_pr_fis_l,'*',label="Gjennomsnitt antall gammaer pre fission")
plt.title('Gjennomsnitt antall gammaer pre fission')
plt.show()

plt.hist(Ga_E_T, bins = 1000,histtype='step',log=True)
plt.title('Gamma energi')
plt.show()

plt.hist(Ga_multy_T, bins = 16,histtype='step',log=True)
plt.title('Gamma multiplisties')
plt.show()
