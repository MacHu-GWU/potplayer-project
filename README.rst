Welcome to the potplayer Documentation
===================================================================================================

A tools to manipulate `potplayer <https://potplayer.daum.net/>`_ playlist.

Potplayer is a popular/powerful universal format video player in windows. ``potplayer`` provide a programmatic way to play with PotPlayer.


**Quick links**:

- `GitHub Homepage <https://github.com/MacHu-GWU/potplayer-project>`_
- `Online Documentation <https://pypi.python.org/pypi/potplayer>`_
- `PyPI download <https://pypi.python.org/pypi/potplayer>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/MacHu-GWU/potplayer-project/issues>`_
- `API reference and source code <http://www.wbh-doc.com.s3.amazonaws.com/potplayer/py-modindex.html>`_


**Usage**

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

You can find the test at ``site-packages/potplayer/tests``.


.. _install:

Install
---------------------------------------------------------------------------------------------------
``potplayer`` is released on PyPI, so all you need is:

.. code-block:: console

	$ pip install potplayer

To upgrade to latest version:

.. code-block:: console
	
	$ pip install --upgrade potplayer

``potplayer`` doesn't force user to install all pre-requisite third party packages. You can install it when you see the error message and when you need it.