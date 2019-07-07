import scrapy
import json
import liupSpider as req
from ..items import GxrcItem
class GxrcSpider(scrapy.Spider):
    name = 'gxrc'
    def start_requests(self):
        cookie = {
        'UM_distinctid':'16b930e3e648b-000d0923c74c87-2711938-100200-16b930e3e66221','searchLog':'','Hm_lvt_8b5e38a6a547f78d5f305bf6658222cd':'1561540313','Hm_lpvt_8b5e38a6a547f78d5f305bf6658222cd':'1561540313','ASP.NET_SessionId':'1z4lhxi1iq3rsr1bpj34u5vy','eu':'%2fZQO0XVpQdIrQiNI94q7zhwYbTEPMv2zuPhK0nwf%2b8lqDcahJr%2bq8BhdtCeGh6f64ak0AjIBWtcMBk39wCV6kiYxcSCE4i%2buwl7ou5f4V5WY4ntRCnEKp8W7daG%2bLCBIvlbKGAdHJ9MroqPrwhAJPrzaQppPpop%2f5WO%2fXmEYpf13v1UMpI4ZnQ%3d%3d'
        # 'Host': 'resume.gxrc.com',
        # 'Referer': 'http://resume.gxrc.com/Resume/ResumeSearch/Search?Keyword=',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }

        for i in range(1,50100):
            url = 'http://resume.gxrc.com/Resume/ResumeSearchPart/SearchJson?Page='+ str(i) +'&PageSize=50'
            yield scrapy.Request(url=url,cookies=cookie)

    def parse(self, response):
        item = GxrcItem()
        # print(response.text)
        datas = json.loads(response.text)['ResultList']
        for i in datas:
            item['id'] = i['ResumeID']
            item['name'] = i['Name']
            item['gender'] = i['Sex']
            item['age'] = i['Age']
            item['jiguan'] = '广西'
            item['jingyan'] = i['TalentDegree']
            item['education'] = i['Education']
            item['city'] = ''
            item['yixiangzhiwei'] = i['CareerObjective']
            item['salary'] = '面议'
            item['gongzuoxingzhi'] = '全职'
            item['daogangshijian'] = i['WorkingState']
            item['school'] = i['College']

            yield item

    # def pares1(self, resp):
    #     item = GxrcItem()
    #     gender = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[1]/text()').extract()[0]
    #     marry = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[3]/text()').extract()[0].strip()
    #     age = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[5]/text()').extract()[0].strip()
    #     guoji = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[9]/font/text()').extract()[0].strip()
    #     zhengzhi = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[15]/text()').extract()[0]
    #     education = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[1]/span[5]/font/text()').extract()[0].strip()
    #     qiuzhizhuangtai = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[3]/span[3]/text()').extract()[0].strip()
    #     zhiwei = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[2]/span[3]/text()').extract()[0].strip()
    #     jingyan = resp.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[3]/span[1]/text()').extract()[0].strip()
    #     jingyan = jingyan + '年工作经验'
    #     qiwangzhiwei = resp.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[1]/span[1]/text()').extract()[0].strip()
    #     qiwanghangye = resp.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[1]/span[3]/font/text()').extract()[0].strip()
    #     qiwangdidian = resp.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[2]/span[2]/text()').extract()[0].strip()
    #
    #     qiwangxinzi = resp.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[2]/span[3]/text()').extract()[0].strip()
    #     jiaoyujingli = resp.xpath('//*[@id="content"]/div[2]/div[6]/table/tbody/tr/td[2]/p/span[1]/text()').extract()[0]

