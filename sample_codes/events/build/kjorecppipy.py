import os
from subprocess import Popen, PIPE, call
import numpy as np
'''

p = Popen('./events', stdin=PIPE)
#out, err = p.communicate('92', '239', '6', '100000','u04.dat')
out, err = p.communicate(os.linesep.join([b'92','235','1','6','100000']))
'''
'''
from subprocess import Popen
#P=Popen(["/Documents/FREYA/fission_v2.0.5/sample_codes/events/src/events.cpp",'94','239'])
P=Popen(["./src/events.cpp"])
'''
'''
list_file = Popen(["./events.cpp"],stdin=subprocess.PIPE)
list_file.communicate(input=['94', '240', '%f' % (Ex[i]), '1000000','u04.dat'])

'''



"""
Program that runs freya, creates Pu240.dat FREYA-file, then runs EventToRoot_compilable and creates Pu240.dat.root,
which is finally analyzed with root.
All interesting quantities are printed in the file data_as_func_of_excitation_enery.dat
OBS:: must run: g++ EventToRoot_compilable.C -o EventToRoot_compilable `root-config --cflags --libs` -std=c++14 when
changing the filename in EventToRoot_compilable.C, as this program is unable to do that by itself
OBS:: Must remember to change number of fissions in freya_root_uncertainty.C, if else that 100k! Else uncertainties are wrong
"""

from subprocess import Popen, PIPE, call
import numpy as np

run_or_err = 0 #parameter deciding if running FREYA for values(0) or error calculation(1)

Ex = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.25,5.5,5.75,6.25,6.5,6.75,7,7.25] #input energy to FREYA-> neutron energy if neutron induced, excitation energy if spontaneous fission
#Ex = [1,2,3,4,5,5.25,5.5,5.75,6.25,6.5,6.75,7,7.25]
Z=92
if run_or_err==0:
	#call(["rm", "data_as_func_of_excitation_energy.dat"])
	#call(["subl", "data_as_func_of_excitation_energy.dat"])

	for i in range(len(Ex)):



		p = Popen('./events', stdin=PIPE)
		#p.communicate(['92', '239', '6', '100000','u04.dat'])
		#p.communicate(os.linesep.join(["%d" %Z]))


		#o = Popen("./EventToRoot_compilable", stdin=PIPE)
		#o.communicate(os.linesep.join([" "])) #makes sure the program stops?

		#m = Popen('root', stdin=PIPE)
		#m.communicate(os.linesep.join(['.x freya_root_analyzer.C']))

		#from subprocess import call
		#call(["root","-q", "-l","freya_root_analyzer.C"])
		#call(["root","-q", "-l","fission_script_root6.C"])

	#from subprocess import call
	#call(["mv", "data_as_func_of_excitation_energy.dat", "data_as_func_of_excitation_energy.dat.unchanged"])

elif run_or_err ==1:
	#call(["rm", "uncertainties.dat"])
	#call(["subl", "uncertainties.dat"])

	#call(["rm", "avg_values_for_unc_calc.dat"])
	#call(["subl", "avg_values_for_unc_calc.dat"])

	for i in range(len(Ex)):

		print ("Now on iteration", i)

		p = Popen('./events', stdin=PIPE)
		p.communicate(os.linesep.join(["94", "240", "1", "%f" % Ex[i], "1000000", "Pu240.dat"]))

		#o = Popen("./EventToRoot_compilable", stdin=PIPE)
		#o.communicate(os.linesep.join([" "])) #makes sure the program stops?

		from subprocess import call
		#call(["root","-q", "-l","freya_root_uncertainty.C"])

		call(["python", "unc_calc.py"])

		call(["rm", "avg_values_for_unc_calc.dat"])
		call(["subl", "avg_values_for_unc_calc.dat"])
