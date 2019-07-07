import requests
from lxml import etree
from urllib import parse
url = 'http://www.cfw.cn/rencai/Search?page=3&keytype=1'
headers = {'Cookie': 'Hm_lvt_c9f5d1e875e39d89d35799c49c4618bc=1561682935; LXB_REFER=www.baidu.com; Hm_lpvt_c9f5d1e875e39d89d35799c49c4618bc=1561689475',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
text = requests.get(url=url,headers=headers).text
html = etree.HTML(text)
hrefs = html.xpath('//div[@class="father"]/table[@class="table table-hover col-lg-6"]/tbody/tr/td[@class="list-job-nane"]/a/@href')
for i in hrefs:
    d_url = 'http://www.cfw.cn'+parse.quote(i)
    print(d_url)