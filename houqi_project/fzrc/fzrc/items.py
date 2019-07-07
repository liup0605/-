# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FzrcItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    zhiwei = scrapy.Field()
    gender = scrapy.Field()
    education = scrapy.Field()
    marry = scrapy.Field()
    age = scrapy.Field()
    jingyan = scrapy.Field()
    juzhudi = scrapy.Field()
    hujidi = scrapy.Field()
    qiuzhizhuangtai = scrapy.Field()
    qiwangdidian = scrapy.Field()
    qiwangzhiwei = scrapy.Field()
    qiwanghangye = scrapy.Field()
    qiwangxinzi = scrapy.Field()

