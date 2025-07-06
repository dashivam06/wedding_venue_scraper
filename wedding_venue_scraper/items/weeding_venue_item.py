# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WeddingVenueItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    contact = scrapy.Field()
    highlights = scrapy.Field()
    guest_capacity = scrapy.Field()
    location = scrapy.Field() 
