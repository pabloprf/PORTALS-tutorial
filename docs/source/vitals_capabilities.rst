VITALS
======

The VITALS (Validation via Iterative Training of Active Learning Surrogates) method, described in `P. Rodriguez-Fernandez et al., Fusion Technol. 74:1-2, 65-76 (2018) <https://www.tandfonline.com/doi/full/10.1080/15361055.2017.1396166>`_ consists of using Bayesian Optimization techniques to help in the multi-channel validation of transport models.

VITALS has been implemented to work with the TGLF model, and can be run using the PORTALS repo, following a few steps described below.


1. Preparation of TGLF class
----------------------------

For this tutorial we will need the following modules and the folder to run VITALS:

.. code-block:: python

	from portals.gacode_tools     import TGLFmodule
	from portals.misc_tools       import IOtools
	from portals_opt.vitals_tools import VITALSmain

	folder = IOtools.expandPath( '$PORTALS_PATH/regressions/scratch/vitals_tut/' )

As a starting point of VITALS, you need to prepare and run TGLF for the base case (please follow the :ref:`TGLF` tutorial for more details):

.. code-block:: python

	inputgacode_file = IOtools.expandPath( '$PORTALS_PATH/regressions/data/input.gacode' )
	
	tglf = TGLFmodule.TGLF( rhos = [ 0.5 ] )
	cdf = tglf.prep( folder, inputgacode = inputgacode_file)
	tglf.run( subFolderTGLF = 'run_base/', TGLFsettings = 5)

If you want to match fluctuation levels or nT cross-phase angles in VITALS, information about the synthetic diagnostic must be provided in the `read()` stage for each radial location:

.. code-block:: python

    tglf.read( label = 'run_base', d_perp_cm = { 0.5: 1.9 } )

Now, once TGLF has run and outputs have been read and stored in the `tglf.results` dictionary, information about the values of experimental fluctuations and heat flux error bars needs to be provided:

.. code-block:: python

	tglf.NormalizationSets['EXP']['exp_TeFluct_rho']    = [0.5]
	tglf.NormalizationSets['EXP']['exp_TeFluct']        = [1.12] # Percent fluctuation
	tglf.NormalizationSets['EXP']['exp_TeFluct_error']  = [0.1]  # Abolute error

	tglf.NormalizationSets['EXP']['exp_neTe_rho']       = [0.5]
	tglf.NormalizationSets['EXP']['exp_neTe']           = [-130] # Degrees
	tglf.NormalizationSets['EXP']['exp_neTe_error']     = [17]

	tglf.NormalizationSets['EXP']['exp_Qe_rho']         = [0.5]
	Qe_base = tglf.NormalizationSets['EXP']['exp_Qe'][np.argmin(np.abs(tglf.NormalizationSets['EXP']['rho']-0.5))]
	tglf.NormalizationSets['EXP']['exp_Qe_error']       = [ Qe_base * 0.2 ] # e.g. 20% error

	tglf.NormalizationSets['EXP']['exp_Qi_rho']        = [0.5]
	Qi_base = tglf.NormalizationSets['EXP']['exp_Qi'][np.argmin(np.abs(tglf.NormalizationSets['EXP']['rho']-0.5))]
	tglf.NormalizationSets['EXP']['exp_Qi_error']       = [ Qi_base * 0.2 ]

At this point, the TGLF class is ready to go into VITALS. One can give the `tglf` object directly to VITALS, or you can save it in a pickle file to read later:

.. code-block:: python

	tglf_file = folder + 'tglf_base.pkl'
	tglf.save_pkl(tglf_file)


2. VITALS Run 
-------------

First you must select the objective functions you want VITALS to match:

.. code-block:: python

	ofs = ['Qe','Qi','TeFluct','neTe']

Then, the free parameters that VITALS can vary, along with their minimum and maximum variation relative to the base case:

.. code-block:: python

	dvs     = ['RLTS_1', 'RLTS_2', 'RLNS_1', 'ZEFF']
	dvs_min = [     0.7,      0.7,      0.7,    0.7]
	dvs_max	= [     1.3,      1.3,      1.3,    1.3]

Then, as it the case for all optimization problems in PORTALS, you must create a function class by selecting the namelist file to use:

.. code-block:: python

	namelist   = IOtools.expandPath( '$PORTALS_PATH/regressions/data/namelist_examples/vitals_example.namelist' )
	vitals_fun = VITALSmain.evaluateVITALS( folder, namelist = namelist )

Once the VITALS object has been created, parameters such as the TGLF control inputs can be chosen:

.. code-block:: python

	vitals_fun.TGLFparameters['TGLFsettings']  = 5

We are now ready to prepare the VITALS class. Here we have two options:

.. code-block:: python

	# Option 1. Pass the tglf object directly
	vitals_fun.prepare( tglf,      classLoaded = True,  0.5, ofs, dvs, dvs_min, dvs_max  )

	# Option 2. Pass the tglf pickled file
	vitals_fun.prepare( tglf_file, classLoaded = False, 0.5, ofs, dvs, dvs_min, dvs_max )

Now we can create and launch the PORTALS optimization process:

.. code-block:: python

	portals_bo = STRATEGYtools.PRF_BO(vitals_fun)
	portals_bo.run()

3. VITALS Interpretation 
------------------------

We can plot the VITALS results easily with:

.. code-block:: python

	vitals_fun.plot_optimization_results()



