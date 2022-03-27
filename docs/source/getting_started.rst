Installation
============

To use PORTALS, first request access to Pablo Rodriguez-Fernandez (pablorf@mit.edu), indicating the intended use.
Then clone the github repository:

.. code-block:: console

   git clone git@github.com:pabloprf/PORTALS.git


Note that PORTALS requires `python3`. It will not work otherwise.
The following packages are requied, and can be installed with `pip3`:

.. code-block:: console

   pip3 install ipython pyDOE deap seaborn uncertainties h5py netCDF4 fortranformat xarray urllib3 geomdl openpyxl scoop xlsxwriter xlrd statistics statsmodels dill notebook ipywidgets multiprocessing_on_dill torch gpytorch botorch --user


The following packages do not affect standard usage but are recommended:

.. code-block:: console

   pip3 install PyQt5 torchvision ax-platform gptools --user


The following packages do not affect standard usage but are useful to interact with OMFIT (in development, e.g. to read g-files):

.. code-block:: console

   pip3 install omfit_classes --user
   pip3 install omas --user

(Note, sometimes `omas` installation may fail because of dependencies. In such case, please do `pip3 install omas --user --no-dependencies`)

Add to .bashrc and source:

.. code-block:: console

   export PORTALS_PATH=/path/to/portals/
   source $PORTALS_PATH/config/portals.bashrc

User configuration
------------------

In `PORTALS/config/`, there is a `config_user_example.json` with specifications of where to run certain codes and what is the login requirements. Please create an equivalent file `config_user.json` in the same folder, indicating your specific needs.

.. note::
   The file `config_user.json` is included in .gitignore, so it will not be pushed to the common repo.

For example, if `"tglf":"engaging"` in `preferences`, this means that, every time in the PORTALS workflow when TGLF needs to run, it will access the engaging machine to do so, and therefore you must specify how to access the engaging machine:

.. code-block:: console

    "preferences": {
        "tglf":             "engaging",
        "verbose_level":    "1"
    },
    "engaging": {
        "machine":          "eofe7.mit.edu", 
        "username":         "pablorf",
        "partition":        "sched_mit_psfc",
        "identity":         "~/.ssh/id_rsa",
        "scratch":          "/nobackup1/pablorf/scratch/"
        }

.. warning::
   If you select to run a code in a given machine, please make sure you have ssh rights to that machine with the login instructions specified. PORTALS will attempt to secure-copy and access that machine through a standard SSH connection and it must therefore be set-up prior to launching PORTALS. Make sure that you can ssh with `ssh username@machine`, and it is recommended that no password is required for the SSH keys, but it is up to the user. Otherwise PORTALS will ask for the password very often.

`preferences` in `config_user.json` also includes a `"verbose_level"`, which indicates how many messages are printed to the terminal when running PORTALS. For debugging purposes, it is recommended a maximum verbose level of `5`. For production runs, a minimum verbose level of `1` is recommended so that you only get important messages.


Notes on simulation codes
-------------------------

Note that PORTALS does not maintain or develop the simulation codes that are used within it, such as those from `GACODE <http://gafusion.github.io/doc/index.html>`_ or `TRANSP <hhttps://transp.pppl.gov/index.html>`_. It assumes that proper permissions have been obtained and that working versions of those codes exist in the machine configured to run them.


* Use of codes at MIT (mfews and `ENGAGING <https://www1.psfc.mit.edu/computers/cluster/accessing.html>`_ )

- The user must install the GACODE repo in the user's home directory, by following instructions here: http://gafusion.github.io/doc/download.html. The platform for ENGAGING is `PSFCLUSTER`.

- To run the NTCC and TRANSP toolsets in the MFEWS computers, make sure you have in the .bashrc file:

.. code-block:: console

   export PORTALS_PATH=/home/pablorf/PORTALS
   source $PORTALS_PATH/config/portals.bashrc


