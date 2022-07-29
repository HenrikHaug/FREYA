from __future__ import division
from subprocess import Popen, PIPE, call
import os
import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress
#from scipy.interpolate import make_interp_spline


def Fraya_kjore(Ex,mean,sigma):
    Ex=Ex
    mean=mean
    sigma=sigma
    print(mean)


    Tot_Ga_energy_pr_fis_l=[]
    Gj_Ga_energy_l=[]
    Gj_Ga_pr_fis_l=[]
    Ga_E_T=[]
    Ga_multy_T=[]
    Total_spin_mother=[]
    Total_spin_l=[]
    Total_spin_t=[]
    Tspinm=[]
    Tspinl=[]
    Tspint=[]
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

        print("Running FREYA with Smean: %.d  Ssigma %.d" % (mean[i], sigma[i]))
        p = Popen('./events', stdin=PIPE)
        p.communicate(os.linesep.join(["92", "235", "%f" % Ex[i], "10", "Pu240.dat", "%d" % mean[i], "%d" % sigma[i]]))

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
        gmt=[]                  # gamma multiplisity tungt fragment
        gel=[]                  # gamma energy lett fragment
        get=[]                  # gamma energy tungt fragment
        spin_initial=[]         # initial spin mother
        spin_lett=[]            # initial spin dougther lett
        spin_tung=[]            # initial spin dougther tung



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
            spin_initial.append(float(v[1]))
            Total_spin_mother.append(float(v[1]))
            for k in range(2):
                i+=1
                v= lines[i].split()
                Ga_multy.append(float(v[0]))
                Ga_multy_T.append(float(v[0]))
                if k==0:
                    gml.append(float(v[0]))
                    spin_lett.append(float(v[1]))
                    Total_spin_l.append(float(v[1]))
                if k==1:
                    gmt.append(float(v[0]))
                    spin_tung.append(float(v[1]))
                    Total_spin_t.append(float(v[1]))
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
        #print(Tot_Ga_energy_pr_fis)
        Tot_Ga_multy=np.sum(Ga_multy)

        Gj_Ga_energy=(Tot_Ga_energy/Tot_Ga_multy)
        Gj_Ga_pr_fis=(T_Ga_multy/nr_of_fissions)          #gjennomsnittlig antall gammaer per fisjon
        #print(Gj_Ga_pr_fis)

        Tot_Ga_energy_pr_fis_l.append(Tot_Ga_energy_pr_fis)
        Gj_Ga_energy_l.append(Gj_Ga_energy)
        Gj_Ga_pr_fis_l.append(Gj_Ga_pr_fis)

        #utregning spin
        #print(np.sum(spin_initial))
        #print(len(spin_initial))
        Tspinm.append((np.sum(spin_initial)/len(spin_initial)))
        Tspinl.append((np.sum(spin_lett)/len(spin_lett)))
        Tspint.append((np.sum(spin_tung)/len(spin_tung)))

        #til jorgen
        #print(np.sum(gml)/len(gml))
        #print(np.sum(gmt)/len(gmt))
        #print(np.sum(gel)/len(gml))
        #print(np.sum(get)/len(gmt))
        #print(np.shape(gml),np.shape(gmt),np.shape(gel),np.shape(get))
        #print(len(gml))
        #print(np.sum(Ga_E)/len(Ga_E))

        #print(np.sum(spin_lett),np.sum(spin_tung))
    return (Tot_Ga_energy_pr_fis_l,Gj_Ga_energy_l,Gj_Ga_pr_fis_l,Ga_E_T,Ga_multy_T,Total_spin_mother,Total_spin_l,Total_spin_t,Tspinm,Tspinl,Tspint)


#Ex=[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.25,5.5,5.75,6.25,6.5,6.75,7.0,7.25] #input energy to FREYA-> neutron energy if neutron induced, excitation energy if spontaneous fission
#Ex=[-4,-7, -7, -7, -7, -7, -7, -7, -7, -11]
#mean=[1,4, 6 , 8, 10, 12, 14, 15, 16, 10 ]
#sigma=[0,2, 3 , 5, 5, 4, 3, 2, 2, 5]
Ex = [-1]
mean = [5]
sigma = [1]

Tot_Ga_energy_pr_fis_l, Gj_Ga_energy_l, Gj_Ga_pr_fis_l, Ga_E_T, Ga_multy_T,Total_spin_mother,Total_spin_l,Total_spin_t,Tspinm,Tspinl,Tspint=Fraya_kjore(Ex,mean,sigma)
#print(Gj_Ga_energy_l,Tot_Ga_energy_pr_fis_l)
print(Tspinm)

'''
plt.plot(Ex,Tot_Ga_energy_pr_fis_l,'*',label="Total Gamma energy per fission")
plt.title('Total Gamma energy per fission')
plt.show()

plt.plot(Ex,Gj_Ga_energy_l,'*',label="Gjennomsnitt Gamma energy")
plt.title('Gjennomsnitt Gamma energy')
plt.show()

plt.plot(np.abs(Ex),Gj_Ga_pr_fis_l,'*',label="Gjennomsnitt antall gammaer pre fission")
plt.title('Gjennomsnitt antall gammaer pre fission')
plt.show()

plt.hist(Ga_E_T, bins = 1000,histtype='step',log=True)
plt.title('Gamma energi')
plt.show()

plt.hist(Ga_multy_T, bins = 16,histtype='step',log=True)
plt.title('Gamma multiplisties')
plt.show()
'''
'''
plt.plot(np.abs(Ex),Tspinm,'+',label="Gjennomsnitt antall gammaer pre fission")
plt.title('Total spin vs Ex')
plt.show()

plt.plot(Ex,Tspinl,'*',label="Gjennomsnitt antall gammaer pre fission")
plt.plot(Ex,Tspint,'*',label="Gjennomsnitt antall gammaer pre fission")
plt.title('Total spin of fragments')
plt.show()
'''
