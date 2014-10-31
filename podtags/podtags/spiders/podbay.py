# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Spider definition for podbay.fm
"""
#
# IMPORTS
#
#SCRAPY
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
# CUSTOM
from podtags.items import PodcastItem

# DECORATOR
def failParsing(func):
    """Do not use while debugging xpath
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            # add logging to taste.
            pass
    return wrapper

# SPIDER
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
            callback='parsePodcast'
        ),
    ]

    @failParsing
    def parsePodcast(self, response):
        """
        This function gets basic data for a podcast

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
