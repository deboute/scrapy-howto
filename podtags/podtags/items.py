# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PodcastItem(scrapy.Item):
    """This class defines a podcast
    """
    id = scrapy.Field()
    thumbnail = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    homepage = scrapy.Field()
    reviews = scrapy.Field()
