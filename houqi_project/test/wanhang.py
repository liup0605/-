import requests
from lxml import etree
import liupSpider as req
from urllib import parse
import MySQLdb
conn=MySQLdb.Connect(host='127.0.0.1',user='root',password='123456',db='houqi_project',port=3306,charset='utf8')
cursor=conn.cursor()
p = 500
while True:
    url = 'http://www.job910.com/talents.html'
    headers = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: JSESSIONID=EA77C49E4CD67F91A36C717A1E9B4C80; Hm_lvt_b025367b7ecea68f5a43655f7540e177=1561345665; zhaopingou_login_callback=https%3A//qiye.zhaopingou.com/resume; certCode=32550c78c8df4b4080512965b11b2f36; zhaopingou_htm_cookie_register_userName=2019-06-25; hrkeepToken=5CB3BE5F3C3E7220AE4E91D45B91C25B; zhaopingou_account=13315408265; JSESSIONID=74E83B2EAF69527218C949365C3D0524; zhaopingou_select_city=-1; Hm_lpvt_b025367b7ecea68f5a43655f7540e177=1561463860
    Host: www.job910.com
    Pragma: no-cache
    Referer: http://www.job910.com/talents.html?pageIndex=3&pageSize=20&sortField=&sort=0&keyword=&nowPosition=&jobclass=&hopeWorkArea=&NowAreaCode=&education=-1&experiencn=-1&updatetime=30&workMethod=&technial=
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'''
    headers = req.get_dict_from_params(headers)

    params = '''pageIndex: 1
    pageSize: 20
    sortField: 
    sort: 0
    keyword: 
    nowPosition: 
    jobclass: 
    hopeWorkArea: 
    NowAreaCode: 
    education: -1
    experiencn: -1
    updatetime: 30
    workMethod: 
    technial: '''
    params = req.get_dict_from_params(params)
    params['pageIndex'] = p
    text = requests.get(url=url,headers=headers,params=params).text
    html = etree.HTML(text)
    try:
        hrefs = html.xpath('//div[@class="joblistblist"]/ul/li/ul/li[@class="wb15l"]/a/@href')
        for href in hrefs:
            d_url = 'http://www.job910.com'+parse.quote(href)
            # print(d_url)
            text = requests.get(url=d_url).text
            # print(text)
            html = etree.HTML(text)
            id = html.xpath('//span[@class="fts-14 gray flex1"]//text()')[0]
            name = html.xpath('//div[@class="flexbox align-center"]/span[@class="fts-34 gray-dark"]/text()')[0].strip()
            gender = html.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()')[0]
            a = html.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()')[1].strip()
            age = a.split('（')[0]
            jiguan = html.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()')[2].strip()
            jingyan = html.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()')[3].strip()
            education = html.xpath('//div[@class="base-info"]/div[@class="line-h-2 fts-16 gray m-t-10"]/div/span//text()')[4].strip()
            city = html.xpath('//div[@class="m-t-18"]/span//text()')[1]
            yixiangzhiwei = html.xpath('//div[@class="m-t-10"]/span//text()')[1]
            s = html.xpath('//div[@class="m-t-10 text-center white-light-bg"]//text()')[1].strip()
            salary = s.split('：')[1].strip()
            gongzuoxingzhi = html.xpath('//div[@class="m-t-10 text-center white-light-bg"]//text()')[3]
            daogangshijian = html.xpath('//div[@class="m-t-10 text-center white-light-bg"]//text()')[5]
            school = html.xpath('//div[@class="unit-item-title m-tb-10"]/span[@class="gray-dark bold"]//text()')[0]
            # print(school)
            sql = "insert into wanhang (id,name,gender,age,jiguan,jingyan,education,city,yixiangzhiwei,salary,gongzuoxingzhi,daogangshijian,school) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (id,name,gender,age,jiguan,jingyan,education,city,yixiangzhiwei,salary,gongzuoxingzhi,daogangshijian,school)
            cursor.execute(sql)
            conn.commit()
    except:
        pass
    p+=1