# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ChainItem(Item):

	Alcohol = Field()

	Article_Number = Field()

	Origin = Field()

	Name = Field()

	Price = Field()

	Volume = Field()

	Manufacturer = Field()

	Type = Field()

	Region = Field()

	Vintage = Field()

	Is_New = Field()