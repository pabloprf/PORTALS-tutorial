TGLF Capabilities
=================

**PORTALS** can be used to run the TGLF model, interpret results, plot revelant quantities and perform scans and transport analyses.
This framework does not provide linceses or support to run TGLF, therefore, please see :ref:`Installation` for information on how to get TGLF working and how to configure your setup.

Once setup has been successful, the following regression test should run smoothly:

.. code-block:: console

	python3 $PORTALS_PATH/regressions/TGLF_workflow.py


Run TGLF from input.gacode
--------------------------

For this tutorial we will need the following modules:

.. code-block:: python

	from portals.gacode_tools 	import TGLFmodule
	from portals.misc_tools 	import IOtools

Select the location of the input.gacode file to start the simulation from. Note that you can use the `IOtools.expandPath()` method to work with relative paths. You should also select the folder where the simulation will be run:

.. code-block:: python

	inputgacode_file 	= IOtools.expandPath('$PORTALS_PATH/regressions/data/input.gacode')
	folder 				= IOtools.expandPath('$PORTALS_PATH/regressions/scratch/tglf_tut/')

TGLF is a local transport model, and therefore one must specify the radial location (in square root of normalized toroidal flux, `rho`) to run TGLF at. Note that the values are given as a list, and several radial locations can be run at once:

.. code-block:: python

	rhos = [0.5]

The TGLF class can be initialized:

.. code-block:: python

	tglf = TGLFmodule.TGLF(rhos=rhos)

To generate the input files (input.tglf) to TGLF at each radial location, **PORTALS** needs to run a few commands (*profiles_gen* and a zeroth-iteration of *tgyro*) to correctly map the quantities in the input.gacode file to the ones required by TGLF. This is done automatically with the `prep()` command. Note that **PORTALS** has a *only-run-if-needed* philosophy and it it finds that the input files to TGLF already exist in the working folder, the preparation method will not run any command, unless a `restart=True` argument is provided.

.. code-block:: python

	cdf = tglf.prep(folder,inputgacode=inputgacode_file,restart=False)

Now, we are ready to run TGLF. Once the `prep()` command has finished its thing, one can run TGLF with different settings, assumptions, etc. That is why, at this point, a sub-folder name for this specific run can be provided. Similarly to the `prep()` command, a `restart` flag can be provided.
The set of control inputs to TGLF (like saturation rule, electromagnetic effects, etc.) are provided in two ways.
First, the argument `TGLFsettings` (which goes from `1` to `5` as of now) indicates the base case to start with. The user is referred to `GACODEdefaults.py` to understand the meaning of each setting.
Second, the argument `extraOptions` can be passed as a dictionary of variables to change.
For example, the following two commands will run TGLF with saturation rule number 2 with and without electromagnetic effets:

.. code-block:: python

	tglf.run(subFolderTGLF='yes_em_folder/',TGLFsettings=5,extraOptions={},restart=False)
	tglf.read(label='yes_em') # Read TGLF results from previous folder and assign them the key name

	tglf.run(subFolderTGLF='no_em_folder/',TGLFsettings=5,extraOptions={'USE_BPER':False},restart=False)
	tglf.read(label='no_em')

Once the `.read()` method has been used after each individual run, the dictionary `tglf.results` is populated with the specified key that we gave as a label (e.g. `tglf.results['yes_em']`) and it contains all TGLF results parsed and interpreted.
In this example, `tglf.results['yes_em']` and `tglf.results['no_em']` are themselves dictionaries, so please do `.keys()` to get all the possible results that have been obtained.

TGLF results can be plotted together by indicating what labels to plot:
	
.. code-block:: python

	tglf.plotRun(labels=['yes_em','no_em'])



This basic regression test will perform an entire TGLF workflow, from a `.CDF` TRANSP output file to a plot with TGLF outputs. It will eventually plot results in a notebook-like plot with different tabs with information about TGLF outputs and inputs, similar to this:

.. figure:: figs/TGLFnotebook.png
	:align: center
	:alt: TGLF_Notebook
	:figclass: align-center



Run TGLF from TRANSP results
----------------------------

There are a number of routines out there that utilize TRANSP outputs to build input files to other simulation codes. PORTALS can be used to facilitate this process to run codes from the GACODE suite.

First, one should create a TGLF class that contains information for the extraction of TRANSP data. The `.CDF` file is needed at this step. It is recommended that a namelist file `TR.DAT` file exists in the same folder, to grab direction of currents and fields. If no namelist is found in the same folder, default signs will be used.

.. code-block:: python

	from portals.gacode_tools import TGLFmodule

	LocationCDF = '/path/to/file.CDF' # Absolute path of the CDF file
	timeRun     = 2.0                 # Time of of interest in seconds
	avTime      = 0.02                # Averaging window around timeRun (+-avTime)
	rho         = 0.9                 # rho location (norm. sqrt. tor. flux) to run TGLF

	tglf = TGLFmodule.TGLF( cdf = LocationCDF, time = timeRun, avTime = avTime, rhos = [rho] )


Next one needs to indicate the folder in which to perform all operations required to generate the input files to TGLF.

.. code-block:: python

	folderWork = '/path/to/final/folder' # Folder for operations and storage
	cdf = tglf.prep( folderWork )

This routine will generate in `folderWork` all the final (`input.tglf`) and intermediate (`input.gacode`, `plasmastate.cdf`, `.geq`) files.

One can stop here and run TGLF externally as one wishes, independent from PORTALS. But you can also run TGLF through PORTALS if the SSH connections to ENGAGING are set properly:

.. code-block:: python

	tglf.run( subFolderTGLF = 'run1/' )


This workflow will generate all TGLF outputs in the folder `/path/to/final/folder/run1/`. Now one can read the results generated and store them in the `tglf.results` dictionary with a self-descriptive short label:

.. code-block:: python

	tglf.read( label = 'base_case' )

One can also run a new TGLF simulation with different settings (e.g. with perpendicular magnetic fluctuations) and store the results with a different label:
	
.. code-block:: python

	tglf.run( subFolderTGLF = 'run2/', extraOptions = {'USER_BPER':True} )
	tglf.read( label = 'electromagnetic' )

Now one can plot all TGLF results together with:

.. code-block:: python

	tglf.plotRun( labels = [ 'base_case', 'electromagnetic' ] )

Run TGLF scans from TRANSP results
----------------------------------

Check out [this script](../../dev_tests/TGLF_case3.py) and modify it for your specific case.

IMPORTANT NOTES
---------------

- The `.prep()` method performs three operations in a sequence:
1. `TRXPL` (https://w3.pppl.gov/~hammett/work/GS2/docs/trxpl.txt) to generate `plasmastate.cdf` and `.geq` files for a specific time-slice from the TRANSP outputs.
2. `PROFILES_GEN` to generate an `input.gacode` file from the `plasmastate.cdf` and `.geq` files. This file is standard within the GACODE suite and contains all plasma information that is required to run core transport codes.
3. `TGYRO` for a "zero" iteration to generate `input.tglf` at specific `rho` locations from the `input.gacode`. This method to generate input files is inspired by how the OMFIT framework works (https://gafusion.github.io/OMFIT-source/index.html).

- `.prep()` will only perform the operations that it needs. For example, if `input.gacode` is found in the right location, it will avoid running steps #1 and #2. This is the default behavior unless a `restart = True` argument is passed to `.prep()`. The user must be careful not to manually change the files in the working folder, to avoid losing track of the files that were used in the process.

- In a similar fashion, `.run()`  will NOT run TGLF if PORTALS detects that ALL the TGLF output files exist in the right location, unless a `restart=True` argument is passed to `.run()`. The user must pass the restart argument if the TGLF settings are changed and the same folder contains outputs already.

- One can change every TGLF input with the `extraOptions = {}` dictionary, as shown earlier. However, `gacode_tools.GACODEdefaults.py` contains a list of presets for TGLF that can be selected by simply passing the argument `TGLFsettings = 1` to the `.run()` method.
Available preset as of 09/08/2021 are:
	- TGFLsettings = 0: Minimal working example
	- TGLFsettings = 1: "Old" ES SAT1
	- TGLFsettings = 2: ES SAT0
	- TGLFsettings = 3: ES SAT1 (a.k.a. SAT1geo)
	- TGLFsettings = 4: ES SAT2

The user is not limited to use those combinations. One can start with a given `TGLFsettings` option, and then modify as many parameters as needed with the `extraOptions` dictionary.

## Interpreting external TGLF results

When TGLF has been run in a folder `tglf/` outside of the PORTALS framework, one can also use PORTALS to look at the ouput results as follows:

.. code-block:: python

	from portals.gacode_tools.TGLFmodule import TGLF

	tglf_results = TGLF()

	folderTGLFresults = 'tglf/'
	input_gacodeLoc   = '/path/to/file.gacode'
	rho_of_interest   = 0.65

	tglf_results.read( folder = folderTGLFresults, input_profilesLoc = input_gacodeLoc, NoSuffixesRho = rho_of_interest )

Note that one needs to provide the `input.gacode` file that was used to generate the TGLF input file, as well as the `rho` location. This is because the TGLF files by themselves do not contain information about the normalization, thus one needs more information to build useful output quantities like heat fluxes in real units.

Now, one can plot all TGLF results:

.. code-block:: python

	tglf_results.plotRun()

Detailed information
--------------------

- The contents of the TGLF class `TGLF` can be found in `gacode_tools.TGLFmodule.py` if one wants to understand how the input files are handled. TGLF outputs are stored in the dictionary `tglf.results` after peforming the `.read()` method.
