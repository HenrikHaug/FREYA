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


    Tot_Nm_energy_pr_fis_l=[]
    Gj_Nm_energy_l=[]
    Gj_Nm_pr_fis_l=[]
    Nm_E_T=[]
    Nm_multy_T=[]
    '''
    Nm_E=[]                 #Nmmma energy
    T_Nm_multy=0.0          #total Nmmma multiplisties
    Nm_multy=[]             #Nmmma multipliseties

    Tot_Nm_energy_pr_fis=[]
    Gj_Nm_energy=[]
    Gj_Nm_pr_fis=[]
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
        Nm_E=[]                 #Nmmma energy
        T_Nm_multy=0.0          #total Nmmma multiplisties
        Nm_multy=[]             #Nmmma multipliseties
        pfgm=[]                 #pre fission Nmmmas
        Nml=[]                  # gamma multiplisity lett fragment
        Nmt=[]                  # gamma multiplisity lett fragment
        Nel=[]
        Net=[]
        N_first_element=[]




        i=0
        ingen=0
        #for i in range(len(lines)-2):
        '''
        while i<(len(lines)-2):
            v= lines[i+1].split()
            if float(v[0])==0:
                i+=1
            elif float(v[0])>0:
                Nm_multy.append(float(v[0]))
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
                Nm_multy.append(float(v[0]))
                Nm_multy_T.append(float(v[0]))
                if k==0:
                    Nml.append(float(v[0]))
                if k==1:
                    Nmt.append(float(v[0]))
                if Nm_multy[-1]!=0:
                    v= lines[i+1].split()
                    ingen=int(Nm_multy[-1])
                    for j in range(ingen):
                        Nm_E.append(float(v[j]))
                        Nm_E_T.append(float(v[j]))
                        N_first_element.append(float(v[0]))
                        T_Nm_multy+=1.0
                        if k==0:
                            Nel.append(float(v[j]))
                        if k==1:
                            Net.append(float(v[j]))
                    i+=1


        Tot_Nm_energy=np.sum(Nm_E)
        #print(Tot_Nm_energy)
        Tot_Nm_energy_pr_fis=(Tot_Nm_energy/nr_of_fissions)
        print(Tot_Nm_energy_pr_fis)
        Tot_Nm_multy=np.sum(Nm_multy)

        Gj_Nm_energy=(Tot_Nm_energy/Tot_Nm_multy)
        Gj_Nm_pr_fis=(T_Nm_multy/nr_of_fissions)          #gjennomsnittlig antall Nmmmaer per fisjon
        print(Gj_Nm_pr_fis)

        Tot_Nm_energy_pr_fis_l.append(Tot_Nm_energy_pr_fis)
        Gj_Nm_energy_l.append(Gj_Nm_energy)
        Gj_Nm_pr_fis_l.append(Gj_Nm_pr_fis)


        print(np.sum(Nml)/len(Nml))
        print(np.sum(Nmt)/len(Nmt))
        print(np.sum(Nel)/len(Nml))
        print(np.sum(Net)/len(Nmt))
        print(np.sum(N_first_element)/len(N_first_element))
        #print(N_first_element)
        print(np.sum(Nm_E)/len(Nm_E))
        #print(np.shape(gml),np.shape(gmt),np.shape(gel),np.shape(get))
        #print(len(gml))
    return (Tot_Nm_energy_pr_fis_l,Gj_Nm_energy_l,Gj_Nm_pr_fis_l,Nm_E_T,Nm_multy_T)


Ex=[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.25,5.5,5.75,6.25,6.5,6.75,7.0,7.25] #input energy to FREYA-> neutron energy if neutron induced, excitation energy if spontaneous fission
Ex=[0.01,0.02,0.03,0.1]


Tot_Nm_energy_pr_fis_l, Gj_Nm_energy_l, Gj_Nm_pr_fis_l, Nm_E_T, Nm_multy_T=Fraya_kjore(Ex)
print(Gj_Nm_energy_l,Tot_Nm_energy_pr_fis_l)

'''
plt.plot(Ex,Tot_Nm_energy_pr_fis_l,'*',label="Total Nmmma energy per fission")
plt.title('Total Nmmma energy per fission')
plt.show()

plt.plot(Ex,Gj_Nm_energy_l,'*',label="Gjennomsnitt Nmmma energy")
plt.title('Gjennomsnitt Nmmma energy')
plt.show()

plt.plot(Ex,Gj_Nm_pr_fis_l,'*',label="Gjennomsnitt antall Nmmmaer pre fission")
plt.title('Gjennomsnitt antall Nmmmaer pre fission')
plt.show()

plt.hist(Nm_E_T, bins = 1000,histtype='step',log=True)
plt.title('Nmmma energi')
plt.show()

plt.hist(Nm_multy_T, bins = 16,histtype='step',log=True)
plt.title('Nmmma multiplisties')
plt.show()
'''
