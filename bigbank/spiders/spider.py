import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import BigbankItem
from itemloaders.processors import TakeFirst


class LuminorSpider(scrapy.Spider):
	name = 'bigbank'
	start_urls = ['https://www.bigbank.lv/jaunumi/']

	def parse(self, response):
		post_links = response.xpath('//div[contains(@class, "bg-lightest-gray")]')
		for post in post_links:
			url = post.xpath('./a/@href').get()
			date = post.xpath('./p[@style="margin-bottom:-21px"]/text()').get()
			title = post.xpath('./a/h4[string-length(text()) > 0]/text()').get()
			if url[-1] == '/':
				yield response.follow(url, self.parse_post, cb_kwargs=dict(date=date, title=title))

	def parse_post(self, response, date, title):
		description = response.xpath('//div[@class="wrapper content-typography"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description)

		item = ItemLoader(item=BigbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', re.findall(r"(\d+.\d+.\d{4})", date)[0])

		return item.load_item()
