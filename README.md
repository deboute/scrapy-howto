= Simple scrapy howto =

[http://scrapy.org/ Scrapy] is a python framework allowing the easy creation if web crawlers, spiders and scrappers.

This howto will show how to scrap a podcast directory and extract reviews in order to create tag clouds for each podcast.

This will enable us to see which words are used the most to describe each podcast.

== install scrapy ==

  pip install scrapy
  pip install service_identity

Scrapy is built upon Twisted, the asynchronous multi-protocol networking framework.

== Start a new scrapy project ==

Scrapy provides a CLI, very much like django-admin, that allows you to setup a new project

  scrapy startproject podtags
