# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GxrcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    age = scrapy.Field()
    jiguan = scrapy.Field()
    jingyan = scrapy.Field()
    education = scrapy.Field()
    city = scrapy.Field()
    yixiangzhiwei = scrapy.Field()
    salary = scrapy.Field()
    gongzuoxingzhi = scrapy.Field()
    daogangshijian = scrapy.Field()
    school = scrapy.Field()
