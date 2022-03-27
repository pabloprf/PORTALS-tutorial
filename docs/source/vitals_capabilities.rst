VITALS
======

1. Preparation of TGLF class
----------------------------

For this tutorial we will need the following modules:

.. code-block:: python

	from portals.gacode_tools import TGLFmodule
	from portals.misc_tools   import IOtools
	from portals_opt.vitals_tools import VITALSmain


.. code-block:: python

	inputgacode_file = IOtools.expandPath( '$PORTALS_PATH/regressions/data/input.gacode' )
	folder           = IOtools.expandPath( '$PORTALS_PATH/regressions/scratch/tglf_tut/' )
	rho 	         = 0.5

As a starting point of VITALS, you need to prepare and run TGLF for the base case (please follow the :ref:`TGLF` tutorial for more details):

.. code-block:: python

	from portals.gacode_tools import TGLFmodule
	from portals.misc_tools   import IOtools

	

	tglf = TGLFmodule.TGLF( rhos = [ rho ] )
	cdf = tglf.prep( folder, inputgacode = inputgacode_file, restart = False )
	tglf.run( subFolderTGLF = 'run_base/', TGLFsettings = 5, restart = False )

If VITALS needs to match fluctuation levels or nT-phase angles, information about the synthetic diagnostic must be provided in the `read()` stage:

.. code-block:: python

    tglf.read( label = 'run_base', d_perp_cm = { rho: 1.9 } )

Now, once TGLF has run, information about the values of experimental fluctuations and heat flux error bars needs to be provided:

.. code-block:: python

	tglf.NormalizationSets['EXP']['exp_TeFluct_rho']    = [rho]
	tglf.NormalizationSets['EXP']['exp_TeFluct'] 		= [1.12] 		# Percent fluctuation
	tglf.NormalizationSets['EXP']['exp_TeFluct_error'] 	= [0.1] 		# Abolute error on it

	tglf.NormalizationSets['EXP']['exp_neTe_rho'] 		= [rho]
	tglf.NormalizationSets['EXP']['exp_neTe']			= [-130]		# Degrees
	tglf.NormalizationSets['EXP']['exp_neTe_error']		= [17] 			# Absolute error

	tglf.NormalizationSets['EXP']['exp_Qe_rho'] 		= [rho]
	Qe_base = tglf.NormalizationSets['EXP']['exp_Qe'][np.argmin(np.abs(tglf.NormalizationSets['EXP']['rho']-rho))]
	tglf.NormalizationSets['EXP']['exp_Qe_error'] 		= [ Qe_base * 0.2 ] 

	tglf.NormalizationSets['EXP']['exp_Qi_rho'] 		= [rho]
	Qi_base = tglf.NormalizationSets['EXP']['exp_Qi'][np.argmin(np.abs(tglf.NormalizationSets['EXP']['rho']-rho))]
	tglf.NormalizationSets['EXP']['exp_Qi_error'] 		= [ Qi_base * 0.2 ]

At this point, the TGLF class is ready to go into VITALS. One can give the class `tglf` directly to VITALS, or you can save it in a pickle file:

.. code-block:: python

	file = folderWork+'tglf.pkl'
	tglf.save_pkl(file)


2. VITALS Run 
-------------

First

.. code-block:: python

	dvs 		= ['RLTS_1','RLTS_2','RLNS_1','ZEFF']
	ofs 		= ['Qe','Qi','TeFluct','neTe']
	dvs_min 	= [0.7,0.7,0.7,0.7]
	dvs_max		= [1.3,1.3,1.3,1.3]


file = folderWork+'tglf.pkl'
tglf.save_pkl(file)

vitals_fun = VITALSmain.evaluateVITALS(folderWork,namelist=namelist)
vitals_fun.TGLFparameters['TGLFsettings']  = TGLFsettings

vitals_fun.prepare(file,rho,ofs,dvs,dvs_min,dvs_max)

PRF_BO = STRATEGYtools.PRF_BO(vitals_fun,restartYN=False)
PRF_BO.run()



3. VITALS Interpretation 
------------------------

vitals_fun.plot_optimization_results()





