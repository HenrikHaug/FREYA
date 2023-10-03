from __future__ import division
from subprocess import Popen, PIPE, call
import os
import numpy as np
import matplotlib.pyplot as plt
import math as mat
from scipy.stats import linregress
from scipy.stats import norm
import matplotlib.mlab as mlab
from scipy.stats import binom
from scipy.stats import beta
#normalisering forsok
#from sklearn import preprocessing


#from scipy.interpolate import make_interp_spline


def Fraya_kjore(Ex,mean,sigma,fission_number):
    Ex=Ex
    mean=mean
    sigma=sigma
    fission_number=fission_number
    print(mean)

    # definere lister
    Tot_Ga_energy_pr_fis_l=[]       #total gamma energy pr fission
    Gj_Ga_energy_l=[]               #gjennomsnitt gamma energi pr fisson
    Gj_Ga_pr_fis_l=[]               #gjennomsnitt gamma pr fission
    Ga_E_T=[]                       #gamma energi
    Ga_multy_T=[]                   #total antall gamma
    Total_spin_mother=[]            #total spin mother nucleus
    Total_spin_l=[]                 #total spin lille fragment
    Total_spin_t=[]                 #total spin tungt fragment
    Tspinm=[]                       #total spin mother nucleus
    Tspinl=[]                       #total spin lille fragment
    Tspint=[]                       #total spin tungt fragment

    ga_energy_pr_ga_pr_spin_output=[]      # gamma enrgi pr fisson
    ga_energy_pr_ga_pr_spin_output_list=[] # for alle enerier og spins
    ga_energy_pr_ga_pr_spin_readinn=[]

    ga_energy_pr_fis_output=[]      # gamma enrgi pr fisson
    ga_energy_pr_fis_output_list=[] # for alle enerier og spins
    ga_energy_pr_fis_readinn=[]

    Ga_E_T_list=[]
    Ga_E_T_list_readinn=[]

    Ga_multy_total_list=[]
    multy_pr_spin_list=[]

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
        p.communicate(os.linesep.join(["90", "231", "%f" % Ex[i], "%d" % fission_number, "Th232.dat", "%d" % mean[i], "%d" % sigma[i]]))

        #lese fra fil
        infile=open('Th232.dat','r')
        lines=infile.readlines()

        #total number of fissions
        fissions=lines[0].split()           #total number of fissions
        nr_of_fissions=float(fissions[3])   #total number of fissions
        #print(nr_of_fissions)
        Ga_E=[]                 # gamma energy
        T_Ga_multy=0.0          # total gamma multiplisties
        Ga_multy=[]             # gamma multipliseties
        pfgm=[]                 # pre fission gammas
        gml=[]                  # gamma multiplisity lett fragment
        gmt=[]                  # gamma multiplisity tungt fragment
        gel=[]                  # gamma energy lett fragment
        get=[]                  # gamma energy tungt fragment
        spin_initial=[]         # initial spin mother
        spin_lett=[]            # initial spin dougther lett
        spin_tung=[]            # initial spin dougther tung
        #gj energi forsok

        #if i>0:
        #    ga_energy_pr_fis_output_list.append(ga_energy_pr_fis_readinn)
        ga_energy_pr_ga_pr_spin_readinn=[]
        ga_energy_pr_fis=[]     # gamma enrgi pr fisson

        ga_energy_pr_fis_readinn=[]
        #ga_energy_pr_fis_2=[]     # gamma enrgi pr fisson

        Ga_multy_total_list_readinn=[]



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
                        #forsok paa aa faa ut gamma energi pr fisson
                        ga_energy_pr_fis.append(float(v[j]))
                        if k==0:
                            gel.append(float(v[j]))
                        if k==1:
                            get.append(float(v[j]))
                    i+=1
            ga_energy_pr_ga_pr_spin_output.append(np.sum(ga_energy_pr_fis)/ingen)     # gamma enrgi pr fisson
            ga_energy_pr_ga_pr_spin_readinn.append(np.sum(ga_energy_pr_fis)/ingen)
            ga_energy_pr_fis_output.append(np.sum(ga_energy_pr_fis))     # gamma enrgi pr fisson
            ga_energy_pr_fis_readinn.append(np.sum(ga_energy_pr_fis))
            ga_energy_pr_fis=[]
            #print(Ga_E_T, 'D')

        #Ga_E_T_list_readinn.append(ga_energy_pr_fis)
        ga_energy_pr_ga_pr_spin_output_list.append(ga_energy_pr_ga_pr_spin_readinn)
        ga_energy_pr_fis_output_list.append(ga_energy_pr_fis_readinn)
        Ga_E_T_list.append(Ga_E)

        Ga_multy_total_list.append(Ga_multy)

        #print(Ga_E_T, 'H')

        #print(ga_energy_pr_fis_output_list)




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
        multy_pr_spin_list.append(Gj_Ga_pr_fis)


        #testing



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
    return (Tot_Ga_energy_pr_fis_l,Gj_Ga_energy_l,Gj_Ga_pr_fis_l,Ga_E_T,Ga_multy_T,Total_spin_mother,Total_spin_l,Total_spin_t,Tspinm,Tspinl,Tspint,ga_energy_pr_ga_pr_spin_output,ga_energy_pr_ga_pr_spin_output_list,ga_energy_pr_fis_output_list,nr_of_fissions,Ga_E_T_list,Ga_multy_total_list,multy_pr_spin_list)


#Ex=[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.25,5.5,5.75,6.25,6.5,6.75,7.0,7.25] #input energy to FREYA-> neutron energy if neutron induced, excitation energy if spontaneous fission
Ex=[-7, -7, -7, -7, -7, -7]
mean=[2, 5 , 8, 11, 14, 18]
sigma=[2, 2 , 2, 2, 2, 2]
fission_number=20000
#Ex = [-1]
#mean = [5]
#sigma = [1]

Tot_Ga_energy_pr_fis_l, Gj_Ga_energy_l, Gj_Ga_pr_fis_l, Ga_E_T, Ga_multy_T,Total_spin_mother,Total_spin_l,Total_spin_t,Tspinm,Tspinl,Tspint,ga_energy_pr_ga_pr_spin_output,ga_energy_pr_ga_pr_spin_output_list,ga_energy_pr_fis_output_list,nr_of_fissions,Ga_E_T_list,Ga_multy_total_list,multy_pr_spin_list=Fraya_kjore(Ex,mean,sigma,fission_number)
#print(Gj_Ga_energy_l,Tot_Ga_energy_pr_fis_l)
'''
np.savetxt("Ga_E_T_list.txt",Ga_E_T_list)
np.savetxt("Ex.txt",Ex)
np.savetxt("mean.txt",mean)
np.savetxt("sigma.txt",sigma)
np.savetxt("fission_number.txt",fission_number)
'''

print(Tspinm)
'''
for i in range(len(Ex)):
 plt.plot(Ex[i],Tot_Ga_energy_pr_fis_l[i],'o',label=('Energy: %.d, Spin mean: %.d, Sigma %.d'  %(abs(Ex[i]), mean[i], sigma[i])))
plt.title('Total Gamma energy per fission')
plt.legend()
plt.show()
'''

#print(Tot_Ga_energy_pr_fis_l)
'''

plt.plot(Ex,Gj_Ga_energy_l,'*',label="Gjennomsnitt Gamma energy")
plt.title('Gjennomsnitt Gamma energy')
plt.show()

plt.plot(np.abs(Ex),Gj_Ga_pr_fis_l,'*',label="Gjennomsnitt antall gammaer pre fission")
plt.title('Gjennomsnitt antall gammaer pre fission')
plt.show()
'''
'''
plt.hist(Ga_E_T, bins = 1000,normed=1,histtype='step',log=True)
plt.title('Gamma energi')
plt.show()


hist2=[]
hist=0
hist, bins_eges=np.histogram(Ga_E_T,bins=1000, density=True)
#print(len(hist))
grus=np.linspace(0,np.max(Ga_E_T),len(hist))
hist2.append((1/(np.max(Ga_E_T)/1000))*hist)
#print(len(grus),(hist2[0]))
plt.plot(grus,hist2[0])
plt.yscale('log')
plt.title('Gamma energi')
plt.show()
print((1/(np.max(Ga_E_T_list[i])/1000)))
for i in range(len(Ex)):
    hist2=[]
    hist=0
    hist, bins_eges=np.histogram(Ga_E_T_list[i],bins=1000, density=True)
    grus=np.linspace(0,np.max(Ga_E_T_list[i]),len(hist))
    hist2.append((1/(np.max(Ga_E_T_list[i])/1000))*hist)
    plt.plot(grus,hist)
    plt.plot(grus,hist2[0])
    plt.yscale('log')
plt.title('Gamma energi')
plt.hist(Ga_E_T, bins = 1000,normed=1,histtype='step',log=True)
plt.show()
'''

MeV=1000
Bins=1000
G_maks=8500
X=np.linspace(0,G_maks,Bins)
bin_sice=G_maks/Bins
hist=np.zeros(len(X))
norm=(MeV/(G_maks/1000))
print(norm)
'''
print(norm)
print(np.max(Ga_E_T))
for i in range(len(Ga_E_T)):
    G=(Ga_E_T[i]*1000)//bin_sice
    #print(G)
    hist[G]+=1
hist[10]=1
print(hist[0:20]*norm/(4*fission_number), norm)
plt.plot(X,hist*norm/(4*fission_number), color="r")
plt.yscale('log')
plt.show()
'''

print(Ga_E_T_list[0][53],Ga_E_T_list[1][53],Ga_E_T_list[2][53],Ga_E_T_list[3][53])
print(len(Ga_E_T_list[0]),len(Ga_E_T_list[1]),len(Ga_E_T_list[2]),len(Ga_E_T_list[3]))
#the rigth one
for i in range(len(Ex)):
    hist=np.zeros(len(X))
    for J in range(len(Ga_E_T_list[i])):
        G=(Ga_E_T_list[i][J]*1000)//bin_sice
        hist[G]+=1
    hist[10]=1
    plt.plot(X,hist*norm/fission_number,label=('Spin mean: %.d'  %(mean[i])))
    #plt.plot(X[120:],hist[120:]*norm/fission_number)
plt.yscale('log')
plt.legend()
plt.title(r'$\gamma$ Energy Spektra')
plt.xlabel(r'$E\gamma$  (keV)')
plt.ylabel('Photons/(Fissions MeV)')
plt.show()

'''
hist, bins, patches = plt.hist(Ga_E_T, bins = 1000, histtype='step',log=True)
X=np.linspace(0,np.max(Ga_E_T),len(hist))
#print(hist)
plt.plot(X,hist, color="k")
#plt.hist(Ga_E_T/25000.0*138, bins = 1000, histtype='step',log=True)
plt.title('Gamma energi')
plt.show()
'''


plt.hist(Ga_multy_T, bins = 16,normed=1,histtype='step',log=True)
plt.title('Gamma multiplisties')
plt.show()

print((Ga_multy_total_list[0][22]),len(Ga_multy_total_list[1]),(Ga_multy_total_list[2][22]),len(Ga_multy_total_list[3]))


plt.plot(np.abs(Ex),Tspinm,'+',label="Gjennomsnitt antall gammaer pre fission")
plt.title('Total spin vs Ex')
plt.show()

plt.plot(Ex,Tspinl,'*',label="Gjennomsnitt antall gammaer pre fission")
plt.plot(Ex,Tspint,'*',label="Gjennomsnitt antall gammaer pre fission")
plt.title('Total spin of fragments')
plt.show()

#hist=np.zeros(len(Ex))


for i in range(len(Ex)):
    hist2=[]
    hist=0
    hist, bins_eges=np.histogram(ga_energy_pr_fis_output_list[i],bins=500, density=True)
    print(len(hist))
    grus=np.linspace(0,np.max(ga_energy_pr_fis_output_list[i]),len(hist))
    hist2.append((1/(np.max(ga_energy_pr_fis_output_list[i])/500))*hist)
    print(len(grus),len(hist2[0]))
    plt.plot(grus,hist2[0])
    plt.yscale('log')
    #plt.show()

n, bins, patches=plt.hist(ga_energy_pr_fis_output_list, normed=1, bins = 160,histtype='step',log=True)
plt.title('Gamma energy pr fission')
#plt.show()




sigg=[]
for i in range(len(Ex)):
    sigg.append(np.std(ga_energy_pr_fis_output_list[i]))
    plt.axvline(x = Tot_Ga_energy_pr_fis_l[i]-sigg[i], color = 'r')
    plt.axvline(x = Tot_Ga_energy_pr_fis_l[i]+sigg[i], color = 'r')
    n, bins, patches = plt.hist((ga_energy_pr_fis_output_list[i]), normed=1, bins = 500,histtype='step', label=('Energy: %.d, Spin mean: %.d, Sigma %.d'  %(abs(Ex[i]), mean[i], sigma[i])))

    #fit to histogram
    #(muuu, sigggma) = norm.fit(ga_energy_pr_fis_output_list[i])
    #y = mlab.normpdf( bins, (muuu-0.5), sigggma)
    #l = plt.plot(bins, y, 'r--', linewidth=2)

    #plt.hist((ga_energy_pr_fis_output_list[i]),normed=1, bins = 500,histtype='step', label=('Energy: %.d, Spin mean: %.d, Sigma %.d'  %(abs(Ex[i]), mean[i], sigma[i])))
print(sigg)
plt.title('Gamma energy pr fission')
plt.legend()
plt.show()

for i in range(len(Ex)):
    plt.hist(ga_energy_pr_ga_pr_spin_output_list[i],normed=1, bins = 500,histtype='step', label=('Energy: %.d, Spin mean: %.d, Sigma %.d'  %(abs(Ex[i]), mean[i], sigma[i])))
plt.title('Gamma energy pr ga_pr_spin')
plt.legend()
plt.show()

for i in range(len(Ex)):
 plt.errorbar(mean[i],Tot_Ga_energy_pr_fis_l[i],yerr=sigg[i],marker='o',label=('Energy: %.d, Spin mean: %.d, Sigma %.d'  %(abs(Ex[i]), mean[i], sigma[i])))
plt.title('Total Gamma energy per initial Angular Momentum')
plt.legend()
plt.show()

'''
eksempel for bruk av errorbar
a=[7,7,7,7,7,7,7,7]
b=[7.033393200000015, 7.1607452000000693, 7.1026242000000757, 7.0235464000000665, 7.0392688000000474, 7.1444440000000045, 7.0942504000000568, 7.0613136000000258]
c=[2.909909190437697, 2.9201206857041013, 2.9620358941401048, 2.9476940498374358, 2.8980284119633075, 2.9425402081983516, 2.9166164261520291, 2.9091023053263458]
plt.errorbar(a,b,yerr=c)
plt.title('Total Gamma energy per fission')
plt.legend()
plt.show()
'''
print(multy_pr_spin_list,'hei')

plt.plot(mean,multy_pr_spin_list)
plt.title('Total Gamma multiplisity per initial Angular Momentum')
plt.show()

plt.subplot(2,1,1)
plt.errorbar(mean,multy_pr_spin_list,yerr=np.std(multy_pr_spin_list),marker='o')
plt.xlim(0,19)
plt.ylim(9,11)
plt.legend()

plt.ylabel(r'$\bar{M}_\gamma$')

plt.subplot(2,1,2)

plt.errorbar(mean,Tot_Ga_energy_pr_fis_l,yerr=np.std(Tot_Ga_energy_pr_fis_l),marker='o')
#plt.title('Total Gamma energy per initial Angular Momentum')
plt.xlabel(r'J $(\hbar)$')
plt.ylabel(r'$\bar{E}_\gamma$ (MeV)')
plt.xlim(0,19)
plt.ylim(6,8)
plt.legend()

plt.show()
