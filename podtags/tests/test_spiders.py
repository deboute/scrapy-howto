# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Test spiders using local webserver
"""
#
# IMPORT
#
# BASE
import subprocess
import unittest
import os
# SCRAPY
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from scrapy import log, signals
# TWISTED
from twisted.internet import reactor, task
# CUSTOM
from podtags.spiders.podbay import PodbaySpiderForGames

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# launch local  web server
html_server = subprocess.Popen([
    'python',
    os.path.join(
        BASE_DIR,
        'responses',
        'podbay',
        'server.py'
    )
])
 
def setup_crawler(
        spider_class,
        **kwargs
    ):
    """
    Use scrapy in a script
    see http://doc.scrapy.org/en/latest/topics/practices.html

    :param spider_class: Spider class to test
    :type spider_class: text
    """
    items = []
    def add_item(item):
        items.append(item)
    # create Crawler
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.configure()
    # connect collecting function on item_passed
    crawler.signals.connect(add_item, signals.item_passed)
    # create & connect spider
    spider = spider_class(**kwargs)
    crawler.crawl(spider)
    # start crawler
    log.start()
    crawler.start()
    # run crawler
    task.deferLater(reactor, 1, reactor.stop)
    reactor.run()
    return items

class SpidersTests(unittest.TestCase):
    """
    Test case for Spiders
    """
    def test_PodbaySpiderForGames(self):
        """
        Test PodbaySpiderForGames
        """
        try:
            # create custom Crawler
            # and fetch generated items
            items = setup_crawler(
                spider_class=PodbaySpiderForGames,
                allowed_domains = ['localhost'],
                start_urls = [
                    'http://localhost:8080/browse/games-and-hobbies'
                ]
            )
            # execute test cases
            self.assertEqual(len(items), 1)
            self.assertEqual(items[0]['id'], '123456789')
        except:
            # end custom html server
            # and raise Exception
            html_server.kill()
            raise
        finally:
            # end custom html server
            html_server.kill()
