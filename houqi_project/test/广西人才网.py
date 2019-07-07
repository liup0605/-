import requests
from lxml import etree
import liupSpider as req
import MySQLdb
conn=MySQLdb.Connect(host='127.0.0.1',user='root',password='123456',db='houqi_project',port=3306,charset='utf8')
cursor=conn.cursor()
# for i in range(1,50000):
headers = '''Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Content-Type: application/json
Cookie: UM_distinctid=16b930e3e648b-000d0923c74c87-2711938-100200-16b930e3e66221; searchLog=; Hm_lvt_8b5e38a6a547f78d5f305bf6658222cd=1561540313; Hm_lpvt_8b5e38a6a547f78d5f305bf6658222cd=1561540313; ASP.NET_SessionId=1z4lhxi1iq3rsr1bpj34u5vy; eu=%2fZQO0XVpQdIrQiNI94q7zhwYbTEPMv2zuPhK0nwf%2b8lqDcahJr%2bq8BhdtCeGh6f64ak0AjIBWtcMBk39wCV6kiYxcSCE4i%2buwl7ou5f4V5WY4ntRCnEKp8W7daG%2bLCBIvlbKGAdHJ9MroqPrwhAJPrzaQppPpop%2f5WO%2fXmEYpf13v1UMpI4ZnQ%3d%3d
Host: resume.gxrc.com
Pragma: no-cache
Referer: http://resume.gxrc.com/Resume/ResumeSearch/Search?Keyword=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36
X-Requested-With: XMLHttpRequest'''
headers = req.get_dict_from_params(headers)
url = 'http://resume.gxrc.com/Resume/ResumeSearchPart/SearchJson?Page=1&PageSize=20'
# print(url)
datas = requests.get(url=url, headers=headers).json()['ResultList']
print(datas)
for i in datas:
    id = i['ResumeID']
    name = i['Name']
    gender = i['Sex']
    age = i['Age']
    jiguan = '广西'
    jingyan = i['TalentDegree']
    education = i['Education']
    city = ''
    yixiangzhiwei = i['Specialty']
    salary = '面议'
    gongzuoxingzhi = '全职'
    daogangshijian = i['WorkingState']
    school = i['College']
    sql = "insert into wanhang (id,name,gender,age,jiguan,jingyan,education,city,yixiangzhiwei,salary,gongzuoxingzhi,daogangshijian,school) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (id, name, gender, age, jiguan, jingyan, education, city, yixiangzhiwei, salary, gongzuoxingzhi, daogangshijian,school)
    cursor.execute(sql)
    conn.commit()

#     ResumeGuid = i['ResumeGuid']
#     # print(ResumeGuid)
#     headers = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: no-cache
# Connection: keep-alive
# Cookie: UM_distinctid=16b930e3e648b-000d0923c74c87-2711938-100200-16b930e3e66221; searchLog=; Hm_lvt_8b5e38a6a547f78d5f305bf6658222cd=1561540313; Hm_lpvt_8b5e38a6a547f78d5f305bf6658222cd=1561540313; Hm_lvt_747e739fe4af8f7f57a24a399882681a=1561540401; ASP.NET_SessionId=b3v5tlmszicx0ciqz1wjynic; CNZZDATA1261311732=1327777776-1561535911-http%253A%252F%252Fvip.gxrc.com%252F%7C1561537116; Hm_lpvt_747e739fe4af8f7f57a24a399882681a=1561541874; eu=%2fZQO0XVpQdIrQiNI94q7zhwYbTEPMv2zuPhK0nwf%2b8lqDcahJr%2bq8BhdtCeGh6f64ak0AjIBWtcMBk39wCV6kiYxcSCE4i%2buwl7ou5f4V5WY4ntRCnEKp8W7daG%2bLCBIvlbKGAdHJ9MroqPrwhAJPrzaQppPpop%2fNB9QDP1RMRR3xoVMu5RnFw%3d%3d
# Host: vip.gxrc.com
# Pragma: no-cache
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'''
#     headers = req.get_dict_from_params(headers)
#     d_url = 'http://vip.gxrc.com/ResumeManage/ResumeView?resumeGuid='+ResumeGuid
#     text = requests.get(url=d_url,headers=headers).text
#     # print(text)
#     html = etree.HTML(text)
#     try:
#         gender = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[1]/text()')[0]
#         marry = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[3]/text()')[0].strip()
#         age = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[5]/text()')[0].strip()
#         guoji = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[9]/font/text()')[0].strip()
#         zhengzhi = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div/span[15]/text()')[0]
#         education = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[1]/span[5]/font/text()')[0].strip()
#         qiuzhizhuangtai = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[3]/span[3]/text()')[0].strip()
#         zhiwei = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[2]/span[3]/text()')[0].strip()
#         jingyan = html.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/p[3]/span[1]/text()')[0].strip()
#         jingyan = jingyan+'年工作经验'
#         qiwangzhiwei = html.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[1]/span[1]/text()')[0].strip()
#         qiwanghangye = html.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[1]/span[3]/font/text()')[0].strip()
#         qiwangdidian = html.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[2]/span[2]/text()')[0].strip()
#
#         qiwangxinzi = html.xpath('//*[@id="content"]/div[2]/div[4]/div[2]/p[2]/span[3]/text()')[0].strip()
#         jiaoyujingli = html.xpath('//*[@id="content"]/div[2]/div[6]/table/tbody/tr/td[2]/p/span[1]/text()')[0].strip()
#         # print(jiaoyujingli)
#     except:
#         pass
#
# # print(datas)
#     # html = etree.HTML(datas)
#     # name = html.xpath('//div[@class="w3 fl"]/text()')
#     # print(name)