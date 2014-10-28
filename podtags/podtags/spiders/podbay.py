from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from podtags.items import PodcastItem

class PodbaySpiderForGames(CrawlSpider):
    """This class defines a spider that parses games and hobbies podcasts
    """
    name = 'podbay'
    allowed_domains = ['podbay.fm']
    start_urls = ['http://podbay.fm/browse/games-and-hobbies']
    rules = [Rule(LinkExtractor(allow=['/show/\d+']), 'parse_podcast')]

    def parse_podcast(self, response):
        """This function gets basic data for a podcast
        """
        podcast = PodcastItem()
        podcast['id'] = response.url.split('/')[-1]
        podcast['title'] = response.xpath("//div[@class='well sidebar-nav']/h4/text()").extract()[0]
        podcast['homepage'] = response.xpath("//div[@class='well sidebar-nav']/a[5]/@href").extract()[0]
        podcast['thumbnail'] = response.xpath("//div[@class='thumbnail']/a/img/@src").extract()[0]
        return podcast
