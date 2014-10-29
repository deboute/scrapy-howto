*******************
Simple scrapy howto
*******************

`Scrapy`_ is a python framework allowing the easy creation if web crawlers, spiders and scrappers.

This howto will show how to scrap a podcast directory and extract reviews in order to create tag clouds for each podcast.

This will enable us to see which words are used the most to describe each podcast.

**Table of Contents**


.. contents::
    :local:
    :depth: 1
    :backlinks: none

==============
install scrapy
==============

::

  $ pip install scrapy
  $ pip install service_identity

`Scrapy`_ is built upon `Twisted`_, the asynchronous multi-protocol networking framework.

==========================
Start a new scrapy project
==========================

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


===============
Create a spider
===============

Our project needs to fetch information from a podcast directory, we will use podbay.fm as an example.

Podbay lists podcasts by category, giving us links to individual podcast pages ( "/show/$podcast_id" ).

Reviews for a podcast are accessible at "/show/$podcast_id/reviews".

By using xpath requests on a podcast's review page we can easily retrieve the following elements:

* id
* thumbnail
* title
* description
* homepage
* list of reviews

We will need to create a Podcast item in items.py

.. code-block:: python

  class PodcastItem(scrapy.Item):
    """This class defines a podcast
    """
    id = scrapy.Field()
    thumbnail = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    homepage = scrapy.Field()
    reviews = scrapy.Field()
    tags = scrapy.Field()

Which is pretty self-explanatory.

And then create a new CrawlSpider object in the spiders directory.

We just have to associate specific url regexes to callback functions that will execute xpath request on their content in order to create our Podcast objects instances.

.. code-block:: python

  class PodbaySpiderForGames(CrawlSpider):
    """This class defines a spider that parses games and hobbies podcasts
    in order to fetch basic data on them and a stack of reviews
    """
    # these variables define where our spider will start scrapping
    name = 'podbay'
    allowed_domains = ['podbay.fm']
    start_urls = [
        'http://podbay.fm/browse/games-and-hobbies'
    ]
    rules = [
        # first rule extracts individual podcast pages links from start_url
        Rule(
            LinkExtractor(allow=['/show/\d+$']),
            follow=True
        ),
        # second rule follows reviews page from individual podcast page
        Rule(
            LinkExtractor(allow=['show/\d+/reviews$']),
            callback='parse_podcast'
        ),
    ]

    @fail_parsing
    def parse_podcast(self, response):
        """This function gets basic data for a podcast

        :param response: A Response object
        :type response: Response

        :returns: a PodcastItem object
        """
        podcast = PodcastItem()
        # extract podcast id from parsed url
        podcast['id'] = response.url.split('/')[-2]
        # navigate xpaths to extract meaningful data from the page
        podcast['title'] = response.xpath(
            "//div[@class='well sidebar-nav']/h4/text()"
        ).extract()[0]
        podcast['homepage'] = response.xpath(
            "//div[@class='well sidebar-nav']/a[5]/@href"
        ).extract()[0]
        podcast['thumbnail'] = response.xpath(
            "//div[@class='thumbnail']/a/img/@src"
        ).extract()[0]
        podcast['reviews'] = response.xpath(
            "//div[@class='span8 well']/p/text()"
        ).extract()
        return podcast

That's it, really, you do not need much more to collect the data.

---------------------------------
Count not common words in content
---------------------------------

Now we have captured via xpath a list of reviews, we will create pipelines that will extract meaningful words and count them.

In settings.py, we can define a dictionnary of pipelines, giving each of them a priority of execution. They will be executed in order upon each Podcast item.

We can use them to validate our data, remove duplicates and actually execute our word counting function on the actual reviews.

The actual word sorting is quite simple, we just have to explore the reviews and discard every word that is not in a common words fil we'll provide to the application.

That's it ! Discard common words, count up uncommon words, generate a json file and we already have finished the exercise.

====================
Test the application
====================

In order to test and generate the json file, clone this repository, enter the podcast/podcast folder and execute

::
  
  scrapy crawl podbay -o wordcloud.json

=======
License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/deboute/scrappy-howto/blob/master/LICENSE>`_ file for more details.

.. _Scrapy: http://scrapy.org
.. _Twisted: https://twistedmatrix.com/trac/
