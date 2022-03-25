Getting Started
===============

.. _getting_started:

Installation
------------

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

In `PORTALS/config/`, there is a `config_user_example.json` with specifications of where to run certain codes and what is the login requirements. Please create an equivalent file `config_user.json` in the same folder, indicating your specific needs. This file is included in .gitignore, so it will not be pushed to the common repo. If you select to run a code in a given machine, please make sure you have ssh rights to that machine with the login instructions specified.

Notes on simulation codes
-------------------------

Note that **PORTALS** does not maintain or develop the simulation codes that are used within it, such as those from `GACODE <http://gafusion.github.io/doc/index.html>`_ or `TRANSP <hhttps://transp.pppl.gov/index.html>`_. It assumes that working versions of those codes exist in the machine configured to run them.

Notes on running **GACODE** in the `ENGAGING <https://www1.psfc.mit.edu/computers/cluster/accessing.html>`_ machine:
- The user must install the GACODE repo in the user's home directory, by following instructions here: http://gafusion.github.io/doc/download.html.

The GACODE platform for ENGAGING is `PSFCLUSTER`. The `.bashrc` file should contain:

.. code-block:: console

   export GACODE_PLATFORM=PSFCLUSTER
   export GACODE_ROOT=/path/to/gacode/
   . ${GACODE_ROOT}/shared/bin/gacode_setup
   . ${GACODE_ROOT}/platform/env/env.${GACODE_PLATFORM}

Then, to install:

.. code-block:: console

   cd /path/to/gacode/
   make clean
   make

- If calling the GACODE routines fail (e.g. when using `profiles_gen`), then it could be because of python modules not installed. Please do in ENGAGING:

.. code-block:: console

   pip3 install numpy matplotlib scipy fortranformat scikit-image --user


- If building the GACODE suite fails and throws errors related to `.mod` files, make sure you remove all `.mod` files from subfolders.

- To run the GACODE suite, the user must have SSH connections set-up to the MIT ENGAGING cluster. PORTALS will attempt to secure-copy and access that machine through a standard SSH connection and it must therefore be set-up prior to launching PORTALS. Make sure that you can ssh with `ssh username@eofe7.mit.edu`, and it is recommended that no password is required for the SSH keys, but it is up to the user. Otherwise PORTALS will ask for the password very often.

- To run the NTCC and TRANSP toolsets, working on a MFEWS computer is required as of now.


