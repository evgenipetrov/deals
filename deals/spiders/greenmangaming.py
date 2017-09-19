# -*- coding: utf-8 -*-
import scrapy


class GreenmangamingSpider(scrapy.Spider):
    name = 'greenmangaming'
    allowed_domains = ['greenmangaming.com']
    start_urls = ['https://www.greenmangaming.com/hot-deals/']

    def parse(self, response):
        for element in response.xpath('.//*[@class="img-full"]/parent::a'):
            yield {
                'title': element.xpath('./div/div/*[contains (@class, "prod-name")]/text()').extract_first(),
                'originalPrice': element.xpath('./div/div/*[contains (@class, "prices")]/span[@class="prev-price"]/text()').extract_first(),
                'discountedPrice': element.xpath('./div/div/*[contains (@class, "prices")]/span[@class="current-price"]/text()').extract_first()
            }
        pass



   #  def parse(self, response):
   #     for href in response.xpath('.//*[@class="img-full"]/parent::a'):
  #          yield response.follow(href, self.parse_title)
  #      pass

  #  def parse_title(self, response):
  #      def extract_with_xpath(query):
  #          return response.xpath(query).extract_first()
#
  #      yield {
   #         'title': extract_with_xpath('.//*[@id="store"]//h1/text()'),
   #         'platform': extract_with_xpath('.//*[@id="platform-list"]//a/text()')
  #      }