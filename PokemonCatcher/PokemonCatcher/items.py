# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemoncatcherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()#id
    name = scrapy.Field()#名字
    name_eng = scrapy.Field()#英文名
    name_jpn = scrapy.Field()#日语名
    attribute1 = scrapy.Field()#属性1
    attribute2 = scrapy.Field()#属性2
    height = scrapy.Field()#身高
    weight = scrapy.Field()#体重