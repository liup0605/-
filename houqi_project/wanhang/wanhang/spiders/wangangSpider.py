import scrapy
import json
import liupSpider as req
from ..items import WanhangItem
from urllib import parse
class WanhangSpider(scrapy.Spider):
    name = 'wh'

    def start_requests(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
        for p in range(1,3548):
            url = 'http://www.job910.com/talents.html?pageIndex='+ str(p)
            yield scrapy.Request(url=url,headers=headers)

    def parse(self, response):
        for url in response.xpath('//div[@class="joblistblist"]/ul/li/ul/li[@class="wb15l"]/a/@href').extract():
            d_url = 'http://www.job910.com' + parse.quote(url)
            yield scrapy.Request(d_url,callback=self.pares1,dont_filter=True)

    def pares1(self, resp):
        item = WanhangItem()
        id = resp.xpath('//span[@class="fts-14 gray flex1"]/text()').extract()[0]
        name = resp.xpath('//div[@class="flexbox align-center"]/span[@class="fts-34 gray-dark"]/text()').extract()[0].strip()
        gender = resp.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()').extract()[0]
        a = resp.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()').extract()[1].strip()
        age = a.split('（')[0]
        jiguan = resp.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()').extract()[2].strip()
        jingyan = resp.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()').extract()[3].strip()
        education = resp.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()').extract()[4].strip()
        city = resp.xpath('//div[@class="m-t-18"]/span//text()').extract()[1]
        yixiangzhiwei = resp.xpath('//div[@class="m-t-10"]/span//text()').extract()[1]
        s = resp.xpath('//div[@class="m-t-10 text-center white-light-bg"]//text()').extract()[1].strip()
        salary = s.split('：')[1].strip()
        gongzuoxingzhi = resp.xpath('//div[@class="m-t-10 text-center white-light-bg"]//text()').extract()[3]
        daogangshijian = resp.xpath('//div[@class="m-t-10 text-center white-light-bg"]//text()').extract()[5]
        school = resp.xpath('//div[@class="unit-item-title m-tb-10"]/span[@class="gray-dark bold"]//text()').extract()[0]
        item['id'] = id
        item['name'] = name
        item['gender'] = gender
        item['age'] = age
        item['jiguan'] = jiguan
        item['jingyan'] = jingyan
        item['education'] = education
        item['city'] = city
        item['yixiangzhiwei'] = yixiangzhiwei
        item['salary'] = salary
        item['gongzuoxingzhi'] = gongzuoxingzhi
        item['daogangshijian'] = daogangshijian
        item['school'] = school
        yield item