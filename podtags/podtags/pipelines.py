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
import glob
from collections import defaultdict
# SCRAPY
from scrapy.exceptions import DropItem
# CUSTOM
from podtags.words import common_words

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
    """
    This class manages the parsing of reviews and the isolation
    of non-common words
    """
    def __init__(self):
        # manage regexes
        self.regexes = {
            # lazy url discarder regex
            'url': re.compile(
                '|'.join([
                    '^(http(s)?://|www\.)',
                    '\.(com|it|net|org)($|/)'
                ])),
            # extra stuff discarder regex
            'extras': re.compile(
                r'\'(d|ll|m|re|s|t|ve)$',
                flags=re.UNICODE
            ),
            # token = word
            'token': re.compile(
                r'[\w]+',
                flags=re.UNICODE
            )
        }

    def process_item(self, item, spider):
        """
        Find non-common words and count their occurences
        """
        reviews_words = defaultdict(int)
        # for each review
        for review in item['reviews']:
            # tokenize text
            for token in self._tokenize(review):
                # increment counter for each non-common token
                if token not in common_words:
                    reviews_words[token] += 1
        # build popular words dictionary
        popular_words = defaultdict(int)
        for (word, count) in reviews_words.items():
            if count > 1:
                popular_words[word] = count

        item['tags'] = popular_words
        # drop reviews now we extracted meaningful tags
        del(item['reviews'])
        return item

    def _tokenize(self, text):
        """
        Return individual tokens from a block of text.

        :param text: text to tokenize
        :type text: str

        :returns: list of (normalized) string tokens
        """
        tokens = []
        for token in text.split():
            # throw urls away
            if self.regexes['url'].search(token):
                continue
            # normalize token
            token = token.lower()
            token = self.regexes['extras'].sub('', token)
            for sub_token in self.regexes['token'].findall(token):
                if sub_token:
                    sub_token = sub_token.lower()
                # add normalized subtoken to list
                if sub_token not in tokens:
                    tokens.append(sub_token)
        return tokens
