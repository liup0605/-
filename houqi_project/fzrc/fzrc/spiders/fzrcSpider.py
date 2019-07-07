from urllib import parse

import scrapy
from lxml import etree
import liupSpider as req
import json
from ..items import FzrcItem
class FzrcSpider(scrapy.Spider):
    name = 'fzrc'
    def start_requests(self):
        for i in range(1, 23271):
            url = 'http://www.cfw.cn/rencai/Search?page=' + str(i) + '&keytype=1'
            headers = {
                'Cookie': 'Hm_lvt_c9f5d1e875e39d89d35799c49c4618bc=1561682935; LXB_REFER=www.baidu.com; Hm_lpvt_c9f5d1e875e39d89d35799c49c4618bc=1561689475',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
            yield scrapy.Request(url=url, headers=headers, dont_filter=True)

    def parse(self, response):
        for i in response.xpath('//div[@class="father"]/table[@class="table table-hover col-lg-6"]/tbody/tr/td[@class="list-job-nane"]/a/@href').extract():
            id = i.split('=')[1]
            d_url = 'http://www.cfw.cn/resumes/show_resume/'
            data = {'ids': '825435',
                    'acceptID': ''}
            data['ids'] = id
            headers = {
                'Cookie': 'Hm_lvt_c9f5d1e875e39d89d35799c49c4618bc=1561682935; LXB_REFER=www.baidu.com; Hm_lpvt_c9f5d1e875e39d89d35799c49c4618bc=1561689552; ASPSESSIONIDSCSSQTRT=KHNBMIKCBEHNEMNHMKDHJLBN',
                'Referer': 'http: // www.cfw.cn / resumes /?ids = 825435',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
            yield scrapy.FormRequest(url=d_url, callback=self.pares1, headers=headers,formdata=data,dont_filter=True)

    def pares1(self, resp):
        item = FzrcItem()
        dat = json.loads(resp.text)['showHtml']
        html = etree.HTML(dat)
        name = html.xpath('//div[@class="resume-header"]//text()')[0]
        b = html.xpath('//div[@class="resume-header"]/div[@class="resume-content1"]//text()')
        gender = b[0]
        age = b[1]
        jingyan = b[3]
        education = b[-2]
        juzhudi = b[-1]
        c = html.xpath('//div[@class="resume-header"]/div[@class="resume-content2"]//text()')
        # print(c)
        hujidi = c[0]
        marry = c[1]
        a = html.xpath('//div[@class="work-intention"]//text()')
        qiwangdidian = a[1]
        qiwangzhiwei = a[4]
        zhiwei = a[4]
        qiwanghangye = a[6]
        qiwangxinzi = a[9]
        qiuzhizhuangtai = a[11]
        item['name'] = name
        item['zhiwei'] = zhiwei
        item['gender'] = gender
        item['age'] = age
        item['jingyan'] = jingyan
        item['education'] = education
        item['juzhudi'] = juzhudi
        item['hujidi'] = hujidi
        item['marry'] = marry
        item['qiwangdidian'] = qiwangdidian
        item['qiwangzhiwei'] = qiwangzhiwei
        item['qiwanghangye'] = qiwanghangye
        item['qiwangxinzi'] = qiwangxinzi
        item['qiuzhizhuangtai'] = qiuzhizhuangtai
        yield item