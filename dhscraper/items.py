# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

# sample function to remove currency
def remove_currency(value):
    return value.replace('$','').strip()

def remove_patterns(value):
    value = value.strip()
    value = re.search(r"^.+(?=\n)", value)
    #added but not run. may cause a problem 9/18/2021 4:00PM
    value = re.search(r"(?=\")*(?=\“)*(?=\")*\w[\w \:;-\’\.\'\",\"\"\(\)]+(?=\")*(?=\”)*(?=\")*", value)
    return value.group()

def only_whitespace(value):
    return value.strip()

class DhscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote = scrapy.Field(input_processor = MapCompose(remove_tags,remove_patterns), output_processor = TakeFirst())
    author = scrapy.Field(input_processor = MapCompose(remove_tags,only_whitespace), output_processor = TakeFirst())
    #if there is price
    #price = scrapy.Field(input_processor = MapCompose(remove_tags, remove_currency), output_processor = TakeFirst())
    #
