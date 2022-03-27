Optimization
============

*Nothing here yet*

Once setup has been successful, the following regression test should run smoothly:

.. code-block:: console

   python3 $PORTALS_PATH/regressions/PORTALS_workflow.py

Optimize a custom function
--------------------------

Optimizing any function (mathematical or a simulation) with PORTALS is extremely easy.

For this tutorial we will need the following modules:

.. code-block:: python

   from portals.misc_tools                import IOtools
   from portals_opt.opt_tools             import STRATEGYtools
   from portals_opt.opt_tools.decoration  import BOgraphics


Select the location of the PORTALS namelist (see :ref:`Understanding the PORTALS namelist` to understand how to construct the namelist file) and the folder to work on:

.. code-block:: python

   folder    = IOtools.expandPath('$PORTALS_PATH/regressions/scratch/portals_tut/')
   namelist  = IOtools.expandPath('$PORTALS_PATH/regressions/data/namelist_examples/opt_example.namelist')

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
         dictOFs['z']['value'] = dictDVs['x']['value']**2
         dictOFs['z']['error'] = dictOFs['z']['value']*5E-2
         # -------------------------------------------------------------

         # Write stuff
         self.write(dictOFs,resultsfile)

Then, create an object from the previously defined class:

.. code-block:: python

   opt_fun1D  = opt_class(folderWork,namelist=namelist)

.. note::

   Note that at this point, you can pass any parameter that you want, just changing the `__init__()` method as appropriate.

Now we can create and launch the PORTALS optimization process from the beginning (i.e. `restart = True`):

.. code-block:: python

   PRF_BO = STRATEGYtools.PRF_BO( opt_fun1D, restartYN = True )
   PRF_BO.run()

Once finished, we can plot the results easily with:

.. code-block:: python

   fn,res,prfs_model = BOgraphics.retrieveResults(folderWork,pkl_YN=True,doNotShow=True)
   fn.show()


Understanding the PORTALS namelist
----------------------------------

*Nothing here yet*

Current fusion applications
---------------------------

.. toctree::

   vitals_capabilities



   