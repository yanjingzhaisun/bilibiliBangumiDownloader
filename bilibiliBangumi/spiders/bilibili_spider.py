import scrapy
from bilibiliBangumi.items import BilibilibangumiItem
import time

class BilibiliSpider(scrapy.Spider):
    name = "bilibiliBangumi"
    allowed_domains = ["bilibili.com"]

    def __init__(self, *args, **kwargs):
        super(BilibiliSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_urls'),]
        scrapy.Spider.__init__(self)
    def parse(self,response):
        time.sleep(2.5)
        seasons = response.xpath('//div[@class="v1-bangumi-list-season-content slider-list-content"]/div/ul')
        print(seasons.extract())
        if len(seasons):
            for season in seasons:
                seasonID = seasons.xpath('li/@data-season-id').extract()[0]
                newurl = "http://bangumi.bilibili.com/anime/" + str(seasonID)
                print("===================================" + seasonID)
                yield scrapy.Request(newurl, callback=self.parse_content)
        #else:
            #yield scrapy.Request(self.start_urls[0], callback=self.parse_content)



    def parse_content(self, response):
        #sel = self.browser
        #sel.get(response.url)
        print("--------------------------------new parse_content")
        item = BilibilibangumiItem();
        time.sleep(2.5)
        sites = response.xpath('//div[@class="complete-list"]/div[@class="video-slider-list-wrapper"]/div[@class="slider-part-wrapper"]/ul/li')
        #sites = sel.select('//div[@class="complete-list"]/div/div[@class="slider-list-content"]/div/ul/li')
        #print(sites.extract())
        for site in sites:
            item['link'] = site.xpath('a/@href').extract()
            #print(item['link'])
            yield item
