'''
Tutorial to run VITALS 
'''

from portals_opt.vitals_tools import VITALSmain

# ---------------------------------------------------------------------------------
# Data Preparation
# ---------------------------------------------------------------------------------

'''
Follow TGLF_tutorial.py until the results are read in the TGLF class "tglf".
That's the starting point of VITALS
'''

#... tglf.read()

rho = 0.5 			# Only rho=0.5 in this example

'''
Since the TGLF and TGYRO classes know nothing about experimental error bars on fluxes,these should be specied now.

They are given in the form of lists or arrays (which allows to specify more than one radial location,
depending how the original tglf class was run) and the values are in absolute units (MW/m^2).
'''

tglf.NormalizationSets['EXP']['exp_Qe_rho']   = [rho]	
tglf.NormalizationSets['EXP']['exp_Qe_error'] = [0.21]

tglf.NormalizationSets['EXP']['exp_Qi_rho']   = [rho]
tglf.NormalizationSets['EXP']['exp_Qi_error'] = [0.14]


'''
Since the TGLF and TGYRO classes know nothing about fluctuations,these should be specied now.

They are given in the form of lists or arrays (which allows to specify more than one radial location,
depending how the original tglf class was run) and the values are in percent fluctuations and in degrees
'''

tglf.NormalizationSets['EXP']['exp_TeFluct_rho'] 	= [rho]
tglf.NormalizationSets['EXP']['exp_TeFluct'] 		= [1.2]
tglf.NormalizationSets['EXP']['exp_TeFluct_error'] 	= [0.1]

tglf.NormalizationSets['EXP']['exp_neTe_rho'] 		= [rho]
tglf.NormalizationSets['EXP']['exp_neTe']			= [-120]
tglf.NormalizationSets['EXP']['exp_neTe_error']		= [20]


# ---------------------------------------------------------------------------------
# VITALS Preparation
# ---------------------------------------------------------------------------------

# Select the folder for the simulation
folder = IOtools.expandPath('$PORTALS_PATH/regressions/scratch/vitals_tut/')

# Select the PORTALS namelist file
namelist_file = '/Users/pablorf/PORTALS/dev_tests/settings/portals.namelist'

# Produce an Optimization settings dictionary out of the namelist file
Optim = IOtools.readOptim_Complete(namelist_file,copyTo=folder)

# Select objectives to match
ofs = ['Qe','Qi','TeFluct','neTe']

# Extract objectives from the tglf class
[Qe_exp,Qi_exp,fluct_exp,neTe_exp],\
[Qe_std,Qi_std,fluct_std,neTe_std], tglf,
Optim['calofs'],Optim['wofs'] = VITALSmain.prepareVITALS(tglf,rho,folder,ofs=ofs,classLoaded=True,
															grabFluct=True,grabPhase=True,grabErrors=True)

# Select free parameters and possible relative variations
Optim['dvs'] 		= ['RLTS_1','RLTS_2','RLNS_1']
Optim['dvs_min'] 	= [		0.8,	 0.8,	  0.8]
Optim['BaselineDV']	= [		1.0,	 1.0,	  1.0]
Optim['dvs_max'] 	= [		1.2,	 1.2,	  1.2]

# Pass simulation details to dictionary
SpecificParams 	= {	'tglf'				:	tglf,	
					'rel_error' 		:   0.05,
					'TGLFsettings'		:	TGLFsettings,
					'extraOptions'		: 	extraOptions,
					'UsingMultipliers'	:	True,
					'launchSlurm'		:   launchSlurm,
					'numSim'			: 	folderWork.split('/')[-1], #????????
					'experimentalVals'	: 	{ 'Qe':Qe_exp, 'Qi':Qi_exp, 'TeFluct':fluct_exp,'neTe':neTe_exp},
					'std_deviation'		: 	{ 'Qe':Qe_std, 'Qi':Qi_std, 'TeFluct':fluct_std,'neTe':neTe_std} }

# ---------------------------------------------------------------------------------
# Run VITALS
# ---------------------------------------------------------------------------------

# Initialize optimization class
PRF_BO = STRATEGYtools.PRF_BO(folder,Optim,VITALSmain.mainFunction,SpecificParams,restartYN=True)

# Run
PRF_BO.run()




