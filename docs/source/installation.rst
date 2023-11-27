Installation
============

Clone the github repository:

.. code-block:: console

   git clone git@github.com:pabloprf/PORTALS.git

Source the configuration file (in *.bashrc* file):

.. code-block:: console

   export PORTALS_PATH=/path/to/portals/
   source $PORTALS_PATH/config/portals.bashrc
   
.. important::
   
   It may be useful, at this point, to create a virtual environment to install required PORTALS dependencies:

   .. code-block:: console

      python3 -m venv portals-env
      source portals-env/bin/activate
      pip3 install -e $PORTALS_PATH

   Alternatively, you can use ``--user`` as a flag when doing ``pip3`` in the next step to install in your user local directory.

Use ``pip3`` to install all the required PORTALS dependencies:

.. code-block:: console

   pip3 install -e $PORTALS_PATH[pyqt]

.. note::
   
   The optional argument ``[pyqt]`` added in the intallation command above must only be used if the machine allows for graphic interfaces. If running in a computing cluster, remove that flag.

.. note::
   
   If you wish to install all capabilities (including `OMFIT <https://omfit.io/>`_ & `FREEGS <https://github.com/freegs-plasma/freegs>`_ compatibility), it is recommended that ``pip3`` is run as follows:

   .. code-block:: console

      pip3 install -e $PORTALS_PATH[omfit,freegs]

User configuration to run simulation codes
------------------------------------------

In ``$PORTALS_PATH/config/``, there is a *config_user_example.json* with specifications of where to run certain codes and what the login requirements are. **If you are planning on using PORTALS to run plasma simulation codes**, please create an equivalent file *config_user.json* in the same folder, indicating your specific needs.

.. code-block:: console

   cp $PORTALS_PATH/config/config_user_example.json $PORTALS_PATH/config/config_user.json
   vim $PORTALS_PATH/config/config_user.json


``preferences`` in *config_user.json* also includes a ``verbose_level`` flag, which indicates the amount of messages that are printed to the terminal when running PORTALS.
For debugging purposes, it is recommended a maximum verbose level of 5.
For production runs, a minimum verbose level of 1 is recommended so that you only get important messages.

``preferences`` also allows a ``dpi_notebook`` value (in percent from standard), which should be adjusted for each user's screen configuration.

.. hint::
   For example, if TGLF is set up to run in the MIT 'Engaging' machine, this means that, every time in the PORTALS workflow when TGLF needs to run, it will access the MIT 'Engaging'g machine to do so, and therefore you must specify how to access the engaging machine:

   .. code-block:: console

       "preferences": {
           "tglf":             "engaging",
           "verbose_level":    "1",
           "dpi_notebook":     "100"
       },
       "engaging": {
           "machine":          "eofe7.mit.edu", 
           "username":         "pablorf",
           "partition":        "sched_mit_psfc",
           "identity":         "~/.ssh/id_rsa",
           "scratch":          "/nobackup1/pablorf/scratch/"
           }
   If you select to run a code in a given machine, please make sure you have ssh rights to that machine with the login instructions specified, unless you are running it locally. PORTALS will attempt to secure-copy and access that machine through a standard SSH connection and it must therefore be set-up prior to launching PORTALS. Make sure that you can ssh with ``ssh username@machine``, and it is recommended that no password is required for the SSH keys, but it is up to the user. Otherwise PORTALS will ask for the password very often.

.. warning::

   Note that PORTALS does not maintain or develop the simulation codes that are used within it, such as those from `GACODE <http://gafusion.github.io/doc/index.html>`_ or `TRANSP <hhttps://transp.pppl.gov/index.html>`_. It assumes that proper permissions have been obtained and that working versions of those codes exist in the machine configured to run them.

License and contributions
-------------------------

By examining, downloading or using this repository, the user explicitly agrees to the PORTALS terms and conditions as stated here. All code sources are copyrighted by the main author Pablo Rodriguez-Fernandez. The author will continue to release development versions of PORTALS, and respond to requests for assistance, bug-fixes and documentation as time permits.

In turn for access to PORTALS, the user agrees:

- not to distribute the original or any modified versions of the source code to any third parties at any time,
- not to provide wide, public access in clusters or computing systems (PORTALS must be installed in private directories or personal computers),
- to inform the first author of planned research using PORTALS,
- prior to publication, to communicate any significant results and, if requested, provide the opportunity for a courtesy review.

