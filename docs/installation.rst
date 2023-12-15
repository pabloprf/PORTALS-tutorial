Installation
============

.. important::
   MITIM requires python3.9, a requirement driven by the optimization capabilities in PyTorch.
   If you do not have python3.9 but still want to use MITIM' non-optimization features, you may try to install each python package individually (see ``setup.py`` file) and skip ``botorch``. However, this option is not supported and there is no assurance the code will work

Clone the github repository:

.. code-block:: console

   git clone git@github.com:pabloprf/MITIM.git

Source the configuration file (in *.bashrc* file):

.. code-block:: console

   export MITIM_PATH=/path/to/mitim/
   source $MITIM_PATH/config/mitim.bashrc
   
.. note::
   
   It may be useful, at this point, to create a virtual environment to install required MITIM dependencies. For examples using python's ``venv`` package:

   .. code-block:: console

      python3 -m venv mitim-env
      source mitim-env/bin/activate

   Alternatively, you can use ``--user`` as a flag when doing ``pip3`` in the next step to install in your user local directory.

Use ``pip3`` to install all the required MITIM requirements:

.. code-block:: console

   pip3 install -e $MITIM_PATH[pyqt]

.. note::
   
   The optional argument ``[pyqt]`` added in the intallation command above must only be used if the machine allows for graphic interfaces. If running in a computing cluster, remove that flag.

   If you are using ZSH you may have problems with the square braquets, in such a case you can do ``pip3 install -e $MITIM_PATH\[pyqt\]``

.. note::
   
   If you wish to install all capabilities (including compatibility with the `OMFIT <https://omfit.io/>`_  or `FREEGS <https://github.com/freegs-plasma/freegs>`_ codes), it is recommended that ``pip3`` is run as follows:

   .. code-block:: console

      pip3 install -e $MITIM_PATH[pyqt,omfit,freegs]

User configuration to run simulation codes
------------------------------------------

In ``$MITIM_PATH/config/``, there is a ``config_user_example.json`` with specifications of where to run certain codes and what the login requirements are. **If you are planning on using MITIM to run plasma simulation codes**, please create an equivalent file ``config_user.json`` in the same folder, indicating your specific needs.

.. code-block:: console

   cp $MITIM_PATH/config/config_user_example.json $MITIM_PATH/config/config_user.json
   vim $MITIM_PATH/config/config_user.json

``preferences`` in ``config_user.json`` also includes a ``verbose_level`` flag, which indicates the amount of messages that are printed to the terminal when running MITIM.
For debugging purposes, it is recommended a maximum verbose level of ``5``.
For production runs, a minimum verbose level of 1 is recommended so that you only get important messages.

``preferences`` also allows a ``dpi_notebook`` value (in percent from standard), which should be adjusted for each user's screen configuration.

.. hint::
   For example, if TGLF is set up to run in the MIT *Engaging* machine, this means that, every time in the MITIM workflow when TGLF needs to run, it will access the MIT *Engaging* machine to do so, and therefore you must specify how to access the engaging machine:

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
   If you select to run a code in a given machine, please make sure you have ssh rights to that machine with the login instructions specified, unless you are running it locally. MITIM will attempt to secure-copy and access that machine through a standard SSH connection and it must therefore be set-up prior to launching MITIM. Make sure that you can ssh with ``ssh username@machine``, and it is recommended that no password is required for the SSH keys, but it is up to the user. Otherwise MITIM will ask for the password very often.

.. warning::

   Note that MITIM does not maintain or develop the simulation codes that are used within it, such as those from `GACODE <http://gafusion.github.io/doc/index.html>`_ or `TRANSP <hhttps://transp.pppl.gov/index.html>`_. It assumes that proper permissions have been obtained and that working versions of those codes exist in the machine configured to run them.

   MITIM does not distribute nor mantain such simulation codes.

License and contributions
-------------------------

By examining, downloading or using this repository, the user explicitly agrees to the MITIM terms and conditions as stated here. All code sources are copyrighted by the main author Pablo Rodriguez-Fernandez. The author will continue to release development versions of MITIM, and respond to requests for assistance, bug-fixes and documentation as time permits.

In turn for access to MITIM, the user agrees:

- not to distribute the original or any modified versions of the source code to any third parties at any time,
- not to provide wide, public access in clusters or computing systems (MITIM must be installed in private directories or personal computers),
- to inform the first author of planned research using MITIM,
- prior to publication, to communicate any significant results and, if requested, provide the opportunity for a courtesy review.

