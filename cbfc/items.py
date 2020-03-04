# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CbfcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Movie(scrapy.Item):
    m_id = scrapy.Field()
    movie_name = scrapy.Field()
    movie_language = scrapy.Field()
    movie_category = scrapy.Field()
    certificate_reg_office = scrapy.Field()
    certificate_no = scrapy.Field()
    certificate_date = scrapy.Field()
    movie_length = scrapy.Field()
    movie_producer = scrapy.Field()
    certificate_applicant = scrapy.Field()
    cuts = scrapy.Field()