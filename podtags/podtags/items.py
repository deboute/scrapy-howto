# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Definition of a Podcast object

See documentation in:
http://doc.scrapy.org/en/latest/topics/items.html
"""
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
