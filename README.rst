Simple scrapy howto
===================

`Scrapy`_ is a python framework allowing the easy creation if web crawlers, spiders and scrappers.

This howto will show how to scrap a podcast directory and extract reviews in order to create tag clouds for each podcast.

This will enable us to see which words are used the most to describe each podcast.

install scrapy
--------------

::

  $ pip install scrapy
  $ pip install service_identity

`Scrapy`_ is built upon `Twisted`_, the asynchronous multi-protocol networking framework.

Start a new scrapy project
--------------------------

`Scrapy`_ provides a CLI, very much like django-admin, that allows you to setup a new project

::

  $ scrapy startproject podtags

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/deboute/scrappy-howto/blob/master/LICENSE>`_ file for more details.

.. _Scrappy: http://scrapy.org
.. _Twisted: https://twistedmatrix.com/trac/
