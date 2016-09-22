.. image:: https://travis-ci.org/MacHu-GWU/potplayer-project.svg?branch=master

.. image:: https://img.shields.io/pypi/v/potplayer.svg

.. image:: https://img.shields.io/pypi/l/potplayer.svg

.. image:: https://img.shields.io/pypi/pyversions/potplayer.svg


Welcome to potplayer Documentation
===============================================================================
**Call a media player to play some video/music from Python is Pain!**

`Pot Player <https://potplayer.daum.net/>`_ is a universal media player software for windows. And the pot player playlist (*.dpl) file is a pure text file to manipulate playlist.

Now with ``potplayer``

**Quick Links**
-------------------------------------------------------------------------------
- `GitHub Homepage <https://github.com/MacHu-GWU/potplayer-project>`_
- `Usage <usage_>`_
- `PyPI download <https://pypi.python.org/pypi/potplayer>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/MacHu-GWU/potplayer-project/issues>`_
- `API reference and source code <http://pythonhosted.org/potplayer/py-modindex.html>`_

.. _usage:

**Usage**
-------------------------------------------------------------------------------
The main usage is to manipulate **video/audio/image** play list:

.. code-block:: python

	>>> import potplayer
	>>> playlist = potplayer.PlayList() # create a PlayList
	>>> playlist.add(r"august_holiday.jpg") # add some `to play` files, can be video/audio/image
	>>> playlist.add(r"life_goes_on.jpg")
	>>> playlist.add(r"trees_cloud_fog_landscape.jpg")
	>>> playlist.dump("play") # dump play list to play.dpl, so you can open it with PotPlayer

You can also use ``run()`` and ``kill()`` method to open anything with PotPlayer, or, kill it.

.. code-block:: python

	>>> potplayer.run("play.dpl") # open a play list, of course you can use this with a video
	>>> potplayer.kill() # kill all running PotPlayer process


.. _install:

Install
-------------------------------------------------------------------------------

``potplayer`` is released on PyPI, so all you need is:

.. code-block:: console

	$ pip install potplayer

To upgrade to latest version:

.. code-block:: console

	$ pip install --upgrade potplayer