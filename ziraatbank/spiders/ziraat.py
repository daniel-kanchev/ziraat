import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from ziraatbank.items import Article


class ZiraatSpider(scrapy.Spider):
    name = 'ziraat'
    allowed_domains = ['ziraatbank.com.tr']
    start_urls = ['https://www.ziraatbank.com.tr/tr/bankamiz/ziraatten-duyurular/duyurular']

    def parse(self, response):
        links = response.xpath('//div[@class="list-box-item"]/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1/text()').get().strip()

        content = response.xpath('//div[@class="sub-page-container"]//div[@style="display:inline"]//text()').getall()
        content = '\n'.join(content[1:]).strip()

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
