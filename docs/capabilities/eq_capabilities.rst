Equilibria Capabilities
=======================

**MITIM** has a quick g-eqdsk file reader and visualizer that is heavily based on OMFITclasses

To open and plot a g-eqdsk file:

.. code-block:: python

	from mitim_tools.gs_tools import GEQmodule
	g = GEQmodule.MITIMgeqdsk(file)
	g.plot()

It will plot results in a notebook-like plot with different tabs:

.. figure:: ./figs/GSnotebook.png
	:align: center
	:alt: TGLF_Notebook
	:figclass: align-center
