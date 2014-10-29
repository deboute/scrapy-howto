# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Spider settings
"""
# Scrapy settings for podtags project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'podtags'

SPIDER_MODULES = ['podtags.spiders']
NEWSPIDER_MODULE = 'podtags.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.1.0'

ITEM_PIPELINES = {
    'podtags.pipelines.RemovesDuplicatesPipeline': 100,
    'podtags.pipelines.ValidatesPipeline': 200,
    'podtags.pipelines.ParsesReviewsPipeline': 300,
}
