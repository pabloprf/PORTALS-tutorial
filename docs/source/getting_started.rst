Installation
============

To use PORTALS, first request access to Pablo Rodriguez-Fernandez (pablorf@mit.edu), indicating the intended use.
Then clone the github repository:

.. code-block:: console

   git clone git@github.com:pabloprf/PORTALS.git

Add to your path (in *.bashrc* file) and source the configuration file:

.. code-block:: console

   export PORTALS_PATH=/path/to/portals/
   source $PORTALS_PATH/config/portals.bashrc
   
You can use ``pip3`` to install (note that PORTALS requires **python3**) all the required PORTALS dependencies.

.. code-block:: console

   pip3 install -e $PORTALS_PATH

.. note::
   
   It may be useful to create a virtual environment to install required PORTALS dependencies:

   .. code-block:: console

      python3 -m venv portals-env
      source portals-env/bin/activate
      pip3 install -e $PORTALS_PATH

   Alternatively, you can use ``--user`` as a flag when doing ``pip3`` to install in your user local directory.

.. note::
   
   If you wish to install all capabilities (including omfit compatibility), it is recommended that ``pip3`` is run as follows, even though you may need to update your fortran compiler.

   .. code-block:: console

      pip3 install -e $PORTALS_PATH[omfit]

User configuration
------------------

In ``$PORTALS_PATH/config/``, there is a *config_user_example.json* with specifications of where to run certain codes and what is the login requirements. Please create an equivalent file *config_user.json* in the same folder, indicating your specific needs.

.. code-block:: console

   cp $PORTALS_PATH/config/config_user_example.json $PORTALS_PATH/config/config_user.json

.. note::
   The file *config_user.json* is included in .gitignore, so it will not be pushed to the common repo.

For example, if TGLF is set up to run in the engaging machine, this means that, every time in the PORTALS workflow when TGLF needs to run, it will access the engaging machine to do so, and therefore you must specify how to access the engaging machine:

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

.. warning::
   If you select to run a code in a given machine, please make sure you have ssh rights to that machine with the login instructions specified, unless you are running it locally. PORTALS will attempt to secure-copy and access that machine through a standard SSH connection and it must therefore be set-up prior to launching PORTALS. Make sure that you can ssh with ``ssh username@machine``, and it is recommended that no password is required for the SSH keys, but it is up to the user. Otherwise PORTALS will ask for the password very often.

``preferences`` in *config_user.json* also includes a ``verbose_level`` flag, which indicates the amount of messages that are printed to the terminal when running PORTALS.
For debugging purposes, it is recommended a maximum verbose level of 5.
For production runs, a minimum verbose level of 1 is recommended so that you only get important messages.
``preferences`` also allows a ``dpi_notebook`` value (in percent from standard), which should be adjusted for each user's screen configuration.


Notes on simulation codes
-------------------------

Note that PORTALS does not maintain or develop the simulation codes that are used within it, such as those from `GACODE <http://gafusion.github.io/doc/index.html>`_ or `TRANSP <hhttps://transp.pppl.gov/index.html>`_. It assumes that proper permissions have been obtained and that working versions of those codes exist in the machine configured to run them.

* Use of codes at MIT (MFEWS and `ENGAGING <https://www1.psfc.mit.edu/computers/cluster/accessing.html>`_ )

   - The user must install the GACODE repo in the user's home directory, by following instructions here: http://gafusion.github.io/doc/download.html. The platform for ENGAGING is ``PSFCLUSTER``. Sometimes ``profiles_gen`` could fail because scikit-learn is not installed as a python3 module.

   - To run the NTCC and TRANSP toolsets in the MFEWS computers, make sure you have followed the setup process outlined above and have in the *.bashrc* file ``source $PORTALS_PATH/config/portals.bashrc``.

* *Other machines coming soon*

