# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Here goes item processing

See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""
#
# IMPORTS
#
# BASE 
import re
import os
# SCRAPY
from scrapy.exceptions import DropItem

#
# PIPELINE CLASSES
#
class RemovesDuplicatesPipeline(object):
    """
    From scrapy documentation.
    Removes duplicate entries.
    """
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: {}".format(item))
        else:
            self.ids_seen.add(item['id'])
            return item

class ValidatesPipeline(object):
    """
    Manages simple items validation
    """
    def process_item(self, item, spider):
        # add validation to taste
        if not item['reviews']:
            raise DropItem("No reviews for item: {}".format(item))
        return item

class ParsesReviewsPipeline(object):
    def process_item(self, item, spider):
        pass
