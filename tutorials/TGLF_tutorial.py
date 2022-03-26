'''
Tutorial to run TGLF 
'''

import numpy as np
from portals.gacode_tools 	import TGLFmodule
from portals.misc_tools 	import IOtools

# ---------------------------------------------------------------------------------
# Data Selection
# ---------------------------------------------------------------------------------

# Select the input.gacode file to start the simulation from
inputgacode_file = IOtools.expandPath('$PORTALS_PATH/regressions/data/input.gacode')

# Select the folder for the simulation
folder = IOtools.expandPath('$PORTALS_PATH/regressions/scratch/tglf_tut/')

# Indicate the radial locations to run TGLF at (rho_tor)
rhos = [0.5]

# Indicate if you want to start the simulation from scratch or check first if results exist
restart = False 	# True = From scratch

# ---------------------------------------------------------------------------------
# Workflow Preparation
# ---------------------------------------------------------------------------------

# Initialize TGLF class at the locations
tglf = TGLFmodule.TGLF(rhos=rhos)

# Prepare input files to TGLF (will run dummy iteration of TGYRO to populate files for TGLF)
cdf = tglf.prep(folder,restart=restart,inputgacode=inputgacode_file)

# ---------------------------------------------------------------------------------
# Run TGLF standalone simulation and read results
# ---------------------------------------------------------------------------------

# Type of simulation and name (will create subfolder with that name)
TGLFsettings = 2
name_sim 	 = 'run1'

# Run TGLF
tglf.run(subFolderTGLF=name_sim,TGLFsettings=TGLFsettings,restart=restart)

# Read TGLF results from previous folder and assign them the key name
tglf.read(label=name_sim)

# ---------------------------------------------------------------------------------
# Interpreting results
# ---------------------------------------------------------------------------------

'''
Once the .read() method has been used, the dictionary tglf.results is populated with the 
specified key (tglf.results['run1']) and it contains all TGLF results parsed and interpreted.

tglf.results['run1'] is itself a dictionary, so please do tglf.results['run1'].keys() to get
all the possible results that have been obtained.
'''

# ---------------------------------------------------------------------------------
# Plot TGLF results
# ---------------------------------------------------------------------------------

tglf.plotRun(labels=[name_sim])

'''
Run TGLF scans
--------------
Scans could be run manually following the previous tutorial and storing the results that the user
is interested in. However, PORTALS also provides a scanning capability.

Class initialization and preparation (.prep() method) are identical to the previous workflow, but
instead of running .run() we will use runScan(), as follows:

	variable  = 'RLTS_2' 				# Variable to scan (must match the TGLF input file nomenclature)
	varUpDown = np.linspace(0.2,2.0,10)	# Relative values to scan (e.g. from 0.2xOriginal to 2.0xOriginal)
	name_scan = 'scan1'					# Name of the scan (will create subfolder)
	
	tglf.runScan(subFolderTGLF = name_scan,variable=variable,varUpDown=varUpDown,TGLFsettings = TGLFsettings, restart = restart)

Then, similar to the .read() command, we will use readScan():
	
	tglf.readScan(label=name_scan,variable=variable)

And, similar to the .plotRun() command, we will use .plotScan():

	tglf.plotScan(labels=[name_scan],variableLabel=variable)


Notes on other possible ways to run TGLF from
---------------------------------------------

- 	If instead of an input.gacode, you have a TRANSP .CDF file (cdf_file) and want to run TGLF
	at a specific time (time) with an averaging time window (avTime), you must initialize the TGLF
	class as follows:

		time 	 = 2.5
		avTime 	 = 0.02
		cdf_file = IOtools.expandPath('$PORTALS_PATH/regressions/data/12345.CDF')
		
		tglf 	 = TGLFmodule.TGLF(cdf=cdf_file,time=time,avTime=avTime,rhos=rhos)

	In this case, the .prep() method does not require an input.gacode file, and intead it will run
	TRXPL and PROFILES_GEN to generate it:

		cdf = tglf.prep(folder,restart=restart)

	The rest of the workflow is identical.

-	If you have a input.tglf file already, you can still use this script to run it. However, you
	still need the input.gacode file because you need a way to grab normalizations.
	As an extra step, you should create the TGLF input classes at each rho location:

		inputtglf_file 	= IOtools.expandPath('$PORTALS_PATH/regressions/data/input.tglf')
		inputsTGLF 		= { rhos[0]: TGLFmodule.TGLFinput(file=inputtglf_file)}

	Then, when running the .prep() method you should tell the code to use specific inputs:

		cdf = tglf.prep(folder,restart=restart,inputgacode=inputgacode_file,specificInputs=inputsTGLF)

	The rest of the workflow is identical.
	Please be aware that this way of running TGLF is not recommended, as the user must ensure that the
	input.gacode file and the input.tglf belong to the same plasma.

'''
