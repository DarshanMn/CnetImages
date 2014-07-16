from scrapy.spider import Spider
from scrapy.selector import Selector
from CnetImages.items import CnetimagesItem
class CnetSpider(Spider):
    name = "cnet_images"
    allowed_domains = ["www.cnet.com"]
    start_urls = [
		"http://www.cnet.com/products/google-nexus-5/"
    ]

    def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//figure[@class="image pull-none image-large"]')
		items = []
		for site in sites:
			item = CnetimagesItem()
			item['images'] = site.xpath('a/img/@src').extract()
			items.append(item)
		return items
