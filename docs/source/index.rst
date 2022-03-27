PORTALS: a toolbox for optimization tasks in fusion and plasma physics
======================================================================

**PORTALS** is a light-weight, command-line, object-oriented Python library for *plasma physics* and *fusion energy* researchers that simplifies optimization tasks.
Developed and maintained by Pablo Rodriguez-Fernandez, MIT Plasma Science and Fusion Center, 2018-2021.

Github repo: https://github.com/pabloprf/PORTALS  

Users Agreement: :ref:`License and Contributions`

.. note::

   This project is under active development.

.. warning::

   The authors are not responsible for any errors or omissions, or for the results obtained from the use of this repository. All scripts and coding examples in this repository are provided "as is", with no guarantee of completeness, accuracy or of the results obtained.

   The intended use of this repository and the capabilities it provides is to accelerate the learning curve of main transport codes, specially for students and young researchers. For publication-quality results, the user is advised to understand every step behind the wheels of PORTALS, and to write custom workflows and routines to test and verify results.

   The users are strongly encouraged to contribute to the code by submitting issues, requesting features or finding bugs. The Users Agreement applies to any forked version of the repository.

Overview
--------

PORTALS was developed as a by-product of transport and optimization research projects at the MIT Plasma Science and Fusion Center in 2018, and has been improved since.
Its original acronym was *Performance Optimization of Reactors via Training of Active Learning Surrogates*, but now PORTALS stands on its own, as a *portal* to various plasma physics activities.

The basis of PORTALS is to handle the standalone execution of codes and interpretation of results in object-oriented python scripts (see :ref:`Standalone Capabilities` for more details).
These python objects can directly be called in a custom Bayesian Optimization framework (see :ref:`Optimization` for more details).


Documentation Contents
--------

.. toctree::

   getting_started
   lincese
   standalone
   optimization
   api

