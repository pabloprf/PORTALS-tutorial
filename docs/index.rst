MITIM: a toolbox for optimization tasks in plasma physics and fusion energy
=============================================================================

**MITIM** is a light-weight, command-line, object-oriented Python library for *plasma physics* and *fusion energy* researchers that simplifies optimization tasks and model execution.
Developed and maintained by Pablo Rodriguez-Fernandez, MIT Plasma Science and Fusion Center, 2018-2023.

Github repo: https://github.com/pabloprf/MITIM-fusion  
Users Agreement: :ref:`License and Contributions`

.. note::

   This project is under active development.

.. warning::

   The authors are not responsible for any errors or omissions, or for the results obtained from the use of this repository. All scripts and coding examples in this repository are provided "as is", with no guarantee of completeness, accuracy or of the results obtained.

   The intended use of this repository and the capabilities it provides is to accelerate the learning curve of main transport codes, specially for students and young researchers. For publication-quality results, the user is advised to understand every step behind the wheels of MITIM, and to write custom workflows and routines to test and verify results.

   The users are strongly encouraged to contribute to the code by submitting issues, requesting features or finding bugs. The Users Agreement applies to any forked version of the repository.

Overview
--------

MITIM was developed as a by-product of transport and optimization research projects at the MIT Plasma Science and Fusion Center that started in 2018, and has been improved since.
Its original acronym was PORTALS (*Performance Optimization of Reactors via Training of Active Learning Surrogates*).

The basis of MITIM is to handle the standalone execution of codes and interpretation of results in object-oriented python scripts (see :ref:`Standalone Capabilities` for more details).
These python objects can directly be called in a custom surrogate-based optimization framework (see :ref:`Optimization Capabilities` for more details).

If you use MITIM for your research, please consider citing the following paper in your upcoming publications:

P. Rodriguez-Fernandez, N.T. Howard and J. Candy, `Nonlinear gyrokinetic predictions of SPARC burning plasma profiles enabled by surrogate modeling <https://iopscience.iop.org/article/10.1088/1741-4326/ac64b2>`_, Nucl. Fusion 62, 076036 (2022).

MITIM documentation contents
------------------------------

.. toctree::
   :maxdepth: 1

   installation
   capabilities/standalone
   capabilities/optimization
