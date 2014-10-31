# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Test spiders using local webserver
"""
import subprocess
import unittest
import os

from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, task
from scrapy import log, signals
from podtags.spiders.podbay import PodbaySpiderForGames

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 
html_server = subprocess.Popen([
    'python',
    os.path.join(
        BASE_DIR,
        'responses',
        'podbay',
        'server.py'
    )
])
 
def setup_crawler():
    items = [] 
    spider = TestSpider()
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.configure()
    crawler.signals.connect(add_item, signals.item_passed)
    crawler.crawl(spider)
    #log.start()
    crawler.start()
 
def add_item(item):
    global items
    items.append(item)
 
class TestSpider(PodbaySpiderForGames):
    allowed_domains = ['localhost']
    start_urls = [
        'http://localhost:8080/browse/games-and-hobbies'
    ]

class SpidersTests(unittest.TestCase):
    def test_PodbaySpiderForGames(self):
        global items
        items = []
        try:
            setup_crawler()
            task.deferLater(reactor, 1, reactor.stop)
            reactor.run()
            self.assertEqual(len(items), 1)
            self.assertEqual(items[0]['id'], '123456789')
        except:
            html_server.kill()
            raise
        finally:
            html_server.kill()
