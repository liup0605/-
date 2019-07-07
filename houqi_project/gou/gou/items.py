# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    zhiwei = scrapy.Field()
    gender = scrapy.Field()
    zhengzhi = scrapy.Field()
    guoji = scrapy.Field()
    education = scrapy.Field()
    chusheng = scrapy.Field()
    marry = scrapy.Field()
    age = scrapy.Field()
    jingyan = scrapy.Field()
    juzhudi = scrapy.Field()
    hujidi = scrapy.Field()
    qiuzhizhuangtai = scrapy.Field()
    qiwangdidian = scrapy.Field()
    qiwangzhiwei = scrapy.Field()
    gongzuoxingzhi = scrapy.Field()
    qiwanghangye = scrapy.Field()
    qiwangxinzi = scrapy.Field()
    jiaoyujingli = scrapy.Field()
