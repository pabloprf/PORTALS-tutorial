Optimization
============

**PORTALS** can be used to optimize any custom function (:ref:`Optimize a custom function`) or simulations that have already been developed in the code (:ref:`Current fusion applications`), such as :ref:`VITALS` and :ref:`PRISA`.
Make sure you follow the :ref:`Installation` tutorial for information on how to get PORTALS working and how to configure your setup.

Once setup has been successful, the following regression test should run smoothly:

.. code-block:: console

   python3 $PORTALS_PATH/regressions/PORTALS_workflow.py

Current fusion applications
---------------------------

.. toctree::

   vitals_capabilities
   prisa_capabilities

Optimize a custom function
--------------------------

Optimizing any function (mathematical or a simulation) with PORTALS is extremely easy.

For this tutorial we will need the following modules:

.. code-block:: python

   from portals.misc_tools                import IOtools
   from portals_opt.opt_tools             import STRATEGYtools

Select the location of the PORTALS namelist (see :ref:`Understanding the PORTALS namelist` to understand how to construct the namelist file) and the folder to work on:

.. code-block:: python

   folder    = IOtools.expandPath('$PORTALS_PATH/regressions/scratch/portals_tut/')
   namelist  = IOtools.expandPath('$PORTALS_PATH/regressions/namelist_examples/opt_example.namelist')

Then create your custom optimization object as a child of the parent `STRATEGYtools.FUNmain` class. You only need to modify what operations need to occur inside the `run()` method. In this example, we are using `$x^2$` as our function with a 5% error:

.. code-block:: python

   class opt_class(STRATEGYtools.FUNmain):

      def __init__(self,folder,namelist=None):

        # Store folder, namelist. Read namelist
         super().__init__(folder,namelist=namelist)
         # ----------------------------------------

      def run(self,paramsfile,resultsfile):

         # Read stuff
         FolderEvaluation,numEval,dictDVs,dictOFs,dictCVs = self.read(paramsfile,resultsfile)

         # Operations -------------------------------------------------
         
         x = dictDVs['x']['value']
         
         z = x**2

         dictOFs['z']['value'] = z
         dictOFs['z']['error'] = z * 5E-2
         # -------------------------------------------------------------

         # Write stuff
         self.write(dictOFs,resultsfile)

Then, create an object from the previously defined class:

.. code-block:: python

   opt_fun1D  = opt_class( folder, namelist = namelist )

.. note::

   Note that at this point, you can pass any parameter that you want, just changing the `__init__()` method as appropriate.

Now we can create and launch the PORTALS optimization process from the beginning (i.e. `restart = True`):

.. code-block:: python

   PRF_BO = STRATEGYtools.PRF_BO( opt_fun1D, restartYN = True )
   PRF_BO.run()

Once finished, we can plot the results easily with:

.. code-block:: python

   opt_fun1D.plot_optimization_results()


Understanding the PORTALS namelist
----------------------------------

The PORTALS namelist contains many parameters (as it is currently under development and improvement). An example can be found in '$PORTALS_PATH/regressions/data/namelist_examples/opt_example.namelist'.

A generic user would only need to care about the following parameters.

- Problem selection: The objective functions names (OPT_ofs) and values (OPT_calofs). The design variables names (OPT_dvs) , minimum (OPT_dvs_min), maximum (OPT_dvs_max) and baseline (OPT_BaselineDV) values.

.. code-block:: console

   OPT_ofs        = [z]    
   OPT_calofs     = [8.0]  

   OPT_dvs        = [x]
   OPT_dvs_min    = [-1]   
   OPT_BaselineDV = [2.0] 
   OPT_dvs_max    = [4.0]

- Main optimization parameters: Number of initial training points (OPT_initialPoints), number of optimization iterations (OPT_BOiterations), number of function evaluations in parallel (OPT_parallelCalls)

.. code-block:: console

   OPT_initialPoints   = 4
   OPT_BOiterations    = 3                   
   OPT_parallelCalls   = 1 

.. note::
   
   The namelist contains many other variables that control the surrogate model, correction techniques and many other aspects of the framework, but that requires being an advanced user.

Understanding the PORTALS outputs
---------------------------------

As a result of the last step of :ref:`Optimize a custom function`, optimization results are plotted...

*Nothing here yet*


