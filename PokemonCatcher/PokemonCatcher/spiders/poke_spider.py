# -*- coding: utf-8 -*-
import scrapy
import urllib

from PokemonCatcher.items import PokemoncatcherItem

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    allowed_domains = ["wiki.52poke.com"]
    start_urls = [
        "https://wiki.52poke.com/wiki/皮卡丘",
        "https://wiki.52poke.com/wiki/西狮海壬"
    ]

    def parse(self, response):
        filename = urllib.parse.unquote(response.url.split("/")[-1])
        with open(filename,'wb') as f:
            f.write(response.body)
        id='firstHeading'
        item = PokemoncatcherItem()
        item['name'] = response.xpath('//h1/text()').extract()[0]
        item['id'] = response.xpath('//a[@title="宝可梦列表（按全国图鉴编号）"]/text()').extract()[0][1:]
        print(item['name'])
        print(item['id'])
        yield item