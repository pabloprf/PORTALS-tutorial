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

Optimizing any function (mathematical or a simulation) with PORTALS is very easy.

For this tutorial we will need the following modules:

.. code-block:: python

   from portals.misc_tools                import IOtools
   from portals_opt.opt_tools             import STRATEGYtools

Select the location of the PORTALS namelist (see :ref:`Understanding the PORTALS namelist` to understand how to construct the namelist file) and the folder to work on:

.. code-block:: python

   folder    = IOtools.expandPath('$PORTALS_PATH/regressions/scratch/portals_tut/')
   namelist  = IOtools.expandPath('$PORTALS_PATH/regressions/namelist_examples/opt_example.namelist')

Then create your custom optimization object as a child of the parent `STRATEGYtools.FUNmain` class. You only need to modify what operations need to occur inside the `run()` (where operations/simulations happen) and `pseudo_single_objective_function()` (to define what is the target to maximize) methods.
In this example, we are using `x^2` as our function with a 5% evaluation error, to find `x` such that `x^2 = 15`:

.. code-block:: python

   class opt_class(STRATEGYtools.FUNmain):

      def __init__(self,folder,namelist=None):

         # Store folder, namelist. Read namelist
         super().__init__(folder,namelist=namelist)
         # ----------------------------------------

         # Define dimension
         self.name_objectives = ['Zval_match']

      def run(self,paramsfile,resultsfile):

         # Read stuff
         FolderEvaluation,numEval,dictDVs,dictOFs,dictCVs = self.read(paramsfile,resultsfile)

         # Operations -------------------------------------------------

         x = dictDVs['x']['value']
         
         z = x**2

         dictOFs['z']['value'] = z
         dictOFs['z']['error'] = z * 5E-2

         # Target value

         dictOFs['zval']['value'] = 15.0
         dictOFs['zval']['error'] =  0.0

         # -------------------------------------------------------------

         # Write stuff
         self.write(dictOFs,resultsfile)

      def pseudo_single_objective_function(self,Y):

         ofs_ordered_names = np.array(self.Optim['ofs'])

         of    = Y[:,ofs_ordered_names == 'z'].unsqueeze(1)
         cal = Y[:,ofs_ordered_names == 'zval'].unsqueeze(1)
         res = -(of-cal).abs().mean(axis=1).unsqueeze(1)

         return of,cal,res

Then, create an object from the previously defined class:

.. code-block:: python

   opt_fun1D  = opt_class(folder)

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

Checkout file `PORTALS/config/main.namelist`, which has comprehensive comments.

*Under development*

Understanding the PORTALS outputs
---------------------------------

As a result of the last step of :ref:`Optimize a custom function`, optimization results are plotted...

*Under development*


