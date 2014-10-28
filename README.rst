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


This will tell `Scrapy`_ to create the basic files it needs

::

  $ tree podtags
  podtags
  ├── podtags
  │   ├── __init__.py
  │   ├── items.py
  │   ├── pipelines.py
  │   ├── settings.py
  │   └── spiders
  │       └── __init__.py
  └── scrapy.cfg


Create a spider
---------------

Our project needs to fetch information from a podcast directory, we will use podbay.fm as an example.

Podbay lists podcasts by category, giving us links to individual podcast pages "/show/$podcast_id".

Reviews for a podcast are accessible at "/show/$podcast_id/reviews".

By using xpath requests on a podcast's page we can easiy retrieve the following elements:
- id
- thumbnail
- title
- description
- homepage

We will be able afterwards to trigger the retrieval of the reviews page in order to start parsing reviews in order to build a tag cloud

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/deboute/scrappy-howto/blob/master/LICENSE>`_ file for more details.

.. _Scrapy: http://scrapy.org
.. _Twisted: https://twistedmatrix.com/trac/
