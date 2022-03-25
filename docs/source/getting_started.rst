Getting Started
===============

.. _getting_started:

Installation
------------

To use PORTALS, first request access to Pablo Rodriguez-Fernandez (pablorf@mit.edu), indicating the intended use.
Then clone the github repository:

.. code-block:: console

   git clone git@github.com:pabloprf/PORTALS.git

User configuration
------------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

