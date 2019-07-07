import scrapy
from lxml import etree
import liupSpider as req
import json
from ..items import GouItem

data = '''pageSize: 2
            pageNo: 25
            keyStr: 
            companyName: 
            schoolName: 
            keyStrPostion: 
            postionStr: 
            startDegrees: -1
            endDegress: -1
            startAge: 0
            endAge: 0
            gender: -1
            region: 
            timeType: -1
            startWorkYear: -1
            endWorkYear: -1
            beginTime: 
            endTime: 
            isMember: -1
            hopeAdressStr: 
            cityId: 5
            updateTime: 
            tradeId: 
            startDegreesName: 
            endDegreesName: 
            tradeNameStr: 
            regionName: 
            isC: 1
            is211_985_school: 0
            clientNo: 
            userToken: 22B0EAD65F6D04C1EF3BF78B99AC831C
            clientType: 2'''
data = req.get_dict_from_params(data)
# print(data)
headers = '''Accept: multipart/form-data
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Length: 420
    Content-type: application/x-www-form-urlencoded
    Cookie: JSESSIONID=EA77C49E4CD67F91A36C717A1E9B4C80; Hm_lvt_b025367b7ecea68f5a43655f7540e177=1561345665; zhaopingou_login_callback=https%3A//qiye.zhaopingou.com/resume; certCode=32550c78c8df4b4080512965b11b2f36; zhaopingou_htm_cookie_register_userName=2019-06-25; hrkeepToken=5CB3BE5F3C3E7220AE4E91D45B91C25B; zhaopingou_account=13315408265; JSESSIONID=74E83B2EAF69527218C949365C3D0524; zhaopingou_select_city=-1; Hm_lpvt_b025367b7ecea68f5a43655f7540e177=1561463860
    Host: qiye.zhaopingou.com
    Origin: https://qiye.zhaopingou.com
    Pragma: no-cache
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'''
headers = req.get_dict_from_params(headers)
# print(headers)
class ZhaopingouSpider(scrapy.Spider):
    name = 'zpg'
    def start_requests(self):
        url = 'https://qiye.zhaopingou.com/zhaopingou_interface/find_warehouse_by_position_new'
        yield scrapy.FormRequest(url=url,formdata=data,headers=headers,method='POST',dont_filter=True)

    def parse(self, response):
        datas = json.loads(response.text)['warehouseList']
        d_url = 'https://qiye.zhaopingou.com/zhaopingou_interface/zpg_find_resume_html_details'
        for i in datas:
            resumeHtmlId = i['resumeHtmlId']
            data = {'resumeHtmlId': str(resumeHtmlId),
                'keyStr': '',
                'keyPositionName': '',
                'tradeId': '',
                'postionStr': '',
                'jobId': '0',
                'companyName': '',
                'schoolName': '',
                'clientNo': '',
                'userToken': '22B0EAD65F6D04C1EF3BF78B99AC831C',
                'clientType': '2'}
            yield scrapy.FormRequest(url=d_url, formdata=data, callback=self.parse1, method='POST',dont_filter=True)

    def parse1(self, resp):
        item = GouItem()
        json_html = json.loads(resp.text)['jsonHtml']
        html = etree.HTML(json_html)
        try:
            name = html.xpath('//div[@class="resume_details_outer mianfei_service_orange"]//text()').extract()[2]
            zhiwei = html.xpath('//div[@class="resume_details_outer mianfei_service_orange"]//text()').extract()[3]
            gender = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[0]
            zhengzhi = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[-1]
            guoji = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[-3]
            education = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[-5]
            chusheng = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[-7]
            if '岁' in chusheng:
                chusheng = ''
            c = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()
            # print(c)
            if '婚'  in c[2]:
                marry = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[2]
                age = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[4]

            else:
                marry = ''
                age = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()').extract()[2]

            d = html.xpath('//div[@class="resumeb-head-contact"]//text()').extract()
            jingyan = d[1]
            juzhudi = d[4]
            hujidi = d[7]
            if hujidi=='暂不合适':
                hujidi = ''

            e = html.xpath('//dl[@class="resume-box"]/dd/p/span//text()').extract()
            length = len(e)
            if length==6:
                qiuzhizhuangtai = e[0]
                qiwangdidian = e[1]
                qiwangzhiwei = e[2]
                gongzuoxingzhi = e[3]
                qiwanghangye = e[-2]
                qiwangxinzi = e[-1]
                # print(qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,gongzuoxingzhi,qiwanghangye,qiwangxinzi,'66666')
            else:
                qiuzhizhuangtai = e[0]
                qiwangdidian = e[1]
                qiwangzhiwei = e[2]
                gongzuoxingzhi = ''
                qiwanghangye = e[-2]
                qiwangxinzi = e[-1]
            f = html.xpath('//div[@class="resume_detail_html"]/dl[@class="resume-box"]/dd/div[@class="experience"]/span/text()').extract()
            jiaoyujingli = ' '.join(f)
        except:
            pass
        item['name'] = name
        item['zhiwei'] = zhiwei
        item['gender'] = gender
        item['zhengzhi'] = zhengzhi
        item['guoji'] = guoji
        item['education'] = education
        item['chusheng'] = chusheng
        item['marry'] = marry
        item['age'] = age
        item['jingyan'] = jingyan
        item['juzhudi'] = juzhudi
        item['hujidi'] = hujidi
        item['qiuzhizhuangtai'] = qiuzhizhuangtai
        item['qiwangdidian'] = qiwangdidian
        item['qiwangzhiwei'] = qiwangzhiwei
        item['gongzuoxingzhi'] = gongzuoxingzhi
        item['qiwanghangye'] = qiwanghangye
        item['qiwangxinzi'] = qiwangxinzi
        item['jiaoyujingli'] = jiaoyujingli
        yield item
