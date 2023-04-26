import scrapy
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field




class LinkSpider(scrapy.Spider):
    name = "links"

    ret_links = []

    LOG_ENABLED = False

    start_urls = ["https://www.fanatics.com/?pageSize=24&sortOption=TopSellers&query=university%20of%20floridahttps://www.fanatics.com/?pageSize=24&sortOption=TopSellers&query=university%20of%20florida"]

    def parse(self, response):

        image_urls = response.css('img')
        for url in image_urls:
            img_url = url.xpath('@src').get()
            if ".jpg" in img_url:
                self.ret_links.append("https:"+img_url)
