#to run:
#in terminal enter the virtual env: venv
#$ source ./venv/bin/activate
#$ cd dhscraper
#$ scrapy crawl dh -o outFile.csv
import scrapy
from scrapy.loader import ItemLoader
'''items.py'''
from dhscraper.items import DhscraperItem

class DhSpider(scrapy.Spider):
    name = 'dh'
    start_urls = ['https://www.goodreads.com/quotes/tag/love?page=2']

    def parse(self,response):

        for quotes in response.css('div.quoteText'):
            l = ItemLoader(item = DhscraperItem(), selector = quotes)

            l.add_css('quote', 'div.quoteText')
            l.add_css('author', 'span.authorOrTitle')
            #for link
            #l.add_css('link', 'a.quoteLink::attr(href)')
            #

            yield l.load_item()

        next_page = response.css('a.next_page').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
