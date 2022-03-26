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

	from portals.gacode_tools import TGLFmodule
	from portals.misc_tools   import IOtools

Select the location of the input.gacode file to start the simulation from. Note that you can use the `IOtools.expandPath()` method to work with relative paths. You should also select the folder where the simulation will be run:

.. code-block:: python

	inputgacode_file = IOtools.expandPath( '$PORTALS_PATH/regressions/data/input.gacode' )
	folder           = IOtools.expandPath( '$PORTALS_PATH/regressions/scratch/tglf_tut/' )

The TGLF class can be initialized by providing the radial location (in square root of normalized toroidal flux, `rho`) to run. Note that the values are given as a list, and several radial locations can be run at once:

.. code-block:: python

	tglf = TGLFmodule.TGLF( rhos = [ 0.5, 0.7 ] )

To generate the input files (input.tglf) to TGLF at each radial location, **PORTALS** needs to run a few commands (*profiles_gen* and a zeroth-iteration of *tgyro*) to correctly map the quantities in the input.gacode file to the ones required by TGLF. This is done automatically with the `prep()` command. Note that **PORTALS** has a *only-run-if-needed* philosophy and it it finds that the input files to TGLF already exist in the working folder, the preparation method will not run any command, unless a `restart=True` argument is provided.

.. code-block:: python

	cdf = tglf.prep( folder, inputgacode = inputgacode_file, restart = False )

Now, we are ready to run TGLF. Once the `prep()` command has finished its thing, one can run TGLF with different settings, assumptions, etc. That is why, at this point, a sub-folder name for this specific run can be provided. Similarly to the `prep()` command, a `restart` flag can be provided.
The set of control inputs to TGLF (like saturation rule, electromagnetic effects, etc.) are provided in two ways.
First, the argument `TGLFsettings` (which goes from `1` to `5` as of now) indicates the base case to start with. The user is referred to `GACODEdefaults.py` to understand the meaning of each setting.
Second, the argument `extraOptions` can be passed as a dictionary of variables to change.
For example, the following two commands will run TGLF with saturation rule number 2 with and without electromagnetic effets. After each `run()` command, a `read()` is needed, to populate the `tglf.results` dictionary with the TGLF outputs (`label` refers to the dictionary key for each run):

.. code-block:: python

	tglf.run(   subFolderTGLF = 'yes_em_folder/', 
				TGLFsettings = 5, extraOptions = {},
				restart = False )

	tglf.read( label = 'yes_em' )

	tglf.run(   subFolderTGLF = 'no_em_folder/', 
				TGLFsettings = 5, extraOptions = {'USE_BPER':False},
				restart = False )

	tglf.read( label = 'no_em' )

In this example, `tglf.results['yes_em']` and `tglf.results['no_em']` are themselves dictionaries, so please do `.keys()` to get all the possible results that have been obtained.
TGLF results can be plotted together by indicating what labels to plot:
	
.. code-block:: python

	tglf.plotRun( labels = ['yes_em', 'no_em'] )

As a result, a TGLF notebook (with different tabs) will be opened with all relevant output quantities:

.. figure:: figs/TGLFnotebook.png
	:align: center
	:alt: TGLF_Notebook
	:figclass: align-center


Run TGLF from a TRANSP results file
-----------------------------------

If instead of an input.gacode, you have a TRANSP .CDF file (`cdf_file`) and want to run TGLF at a specific time (`time`) with an averaging time window (`avTime`), you must initialize the TGLF class as follows:

.. code-block:: python

	cdf_file = IOtools.expandPath( '$PORTALS_PATH/regressions/data/12345.CDF' )		
	tglf     = TGLFmodule.TGLF( cdf = cdf_file, time = 2.5, avTime = 0.02, rhos = [ 0.5, 0.7 ] )

Similarly as in the previous section, you need to run the `prep()` command, but this time you do not need to provide the input.gacode file:

.. code-block:: python

	cdf = tglf.prep(f older, restart = False )

The rest of the workflow is identical.


Run TGLF from a input.tglf file directly
----------------------------------------

If you have a input.tglf file already, you can still use this script to run it. However, you still need the input.gacode file because you need a way to grab normalizations. As an extra step, you should create the TGLF input classes at each rho location:

.. code-block:: python

	inputtglf_file = IOtools.expandPath( '$PORTALS_PATH/regressions/data/input.tglf' )
	inputsTGLF 	   = { 0.5: TGLFmodule.TGLFinput( file = inputtglf_file ) }

Then, when running the `.prep()` method you should tell the code to use specific inputs:

.. code-block:: python

    cdf = tglf.prep( folder, 
                     inputgacode    = inputgacode_file,
                     specificInputs = inputsTGLF,
                     restart        = False)

The rest of the workflow is identical.

Please be aware that this way of running TGLF is not recommended, as the user must ensure that the input.gacode file and the input.tglf belong to the same plasma.



Notes
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
