# from __future__ import unicode_literals
import scrapy

import json

import os

import scrapy

from scrapy.spiders import Spider

from scrapy.http import FormRequest

from scrapy.http import Request

from chainxy.items import ChainItem

from scrapy import signals

from scrapy.xlib.pydispatch import dispatcher

from selenium import webdriver

from lxml import etree

from lxml import html

import time

import pdb


class Springwine(scrapy.Spider):

	name = 'springwine'

	domain = 'https://www.spendrups.se'

	history = []

	output = []

	def __init__(self):

		pass
	
	def start_requests(self):

		url = "http://www.springwine.se/Templates/Pages/Vin/SearchCatalog.ashx?grid=small&sortfield=title&sortdirection="

		yield scrapy.Request(url, callback=self.parse) 

	def parse(self, response):

		product_list = json.loads(response.body)

		for product in product_list:

			item = ChainItem()

			item['Alcohol'] = self.validate(product['alcohol'])

			item['Article_Number'] = self.validate(product['article'])			

			item['Origin'] = self.validate(product['country'])

			item['Name'] = self.validate(product['title'])

			item['Price'] = self.validate(product['price'])

			item['Volume'] = self.validate(product['volume'])

			item['Manufacturer'] = self.validate(product['producer'])

			item['Type'] = self.validate(product['type'])

			item['Region'] = self.validate(product['region'])

			item['Vintage'] = self.validate(product['vintage'])

			item['Is_New'] = 'Yes' if product['is_new'] else 'No'

			yield item


	def validate(self, item):

		try:

			return item.replace('\n', '').replace('\t','').replace('\r', '').strip()

		except:

			pass


	def eliminate_space(self, items):

	    tmp = []

	    for item in items:

	        if self.validate(item) != '':

	            tmp.append(self.validate(item))

	    return tmp