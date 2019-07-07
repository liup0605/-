import requests
from lxml import etree
import liupSpider as req
import MySQLdb
conn=MySQLdb.Connect(host='127.0.0.1',user='root',password='123456',db='houqi_project',port=3306,charset='utf8')
cursor=conn.cursor()
while True:
    url = 'https://qiye.zhaopingou.com/zhaopingou_interface/find_warehouse_by_position_new'
    headers = '''Accept: multipart/form-data
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Length: 420
    Content-type: application/x-www-form-urlencoded
    Cookie: JSESSIONID=7C2ED8CE135EC9629A2D349E31BC4AF5; Hm_lvt_b025367b7ecea68f5a43655f7540e177=1561345665; certCode=2db2a96fc75c4d8d89d864251ae302ee; zhaopingou_htm_cookie_register_userName=2019-06-24; hrkeepToken=22B0EAD65F6D04C1EF3BF78B99AC831C; zhaopingou_account=17319208265; JSESSIONID=0A3954A1C2DDCA1097C3D31A5A7A36A4; Hm_lpvt_b025367b7ecea68f5a43655f7540e177=1561369320; zhaopingou_select_city=5
    Host: qiye.zhaopingou.com
    Origin: https://qiye.zhaopingou.com
    Pragma: no-cache
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'''

    headers = req.get_dict_from_params(headers)
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
    datas = requests.post(url=url,data=data,headers=headers).json()['warehouseList']
    # print(datas)
    for i in datas:
        b = i['resumeHtmlId']
        d_url = 'https://qiye.zhaopingou.com/zhaopingou_interface/zpg_find_resume_html_details'
        # print(d_url)
        data = '''resumeHtmlId: 5907154
    keyStr: 
    keyPositionName: 
    tradeId: 
    postionStr: 
    jobId: 0
    companyName: 
    schoolName: 
    clientNo: 
    userToken: 22B0EAD65F6D04C1EF3BF78B99AC831C
    clientType: 2'''
        try:
            data = req.get_dict_from_params(data)
            data['resumeHtmlId'] = b
            dat = requests.post(url=d_url,data=data).json()['jsonHtml']

            html = etree.HTML(dat)
            name = html.xpath('//div[@class="resume_details_outer mianfei_service_orange"]//text()')[2]
            zhiwei = html.xpath('//div[@class="resume_details_outer mianfei_service_orange"]//text()')[3]
            gender = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[0]
            zhengzhi = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[-1]
            guoji = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[-3]
            education = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[-5]
            chusheng = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[-7]
            if '岁' in chusheng:
                chusheng = ''
            c = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')
            # print(c)
            if '婚'  in c[2]:
                marry = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[2]
                age = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[4]
                # print(marry,age,'111111')
            else:
                marry = ''
                age = html.xpath('//div[@class="resumeb-head-con"]/ul/li//text()')[2]
                # print(marry,age,'222222')
            d = html.xpath('//div[@class="resumeb-head-contact"]//text()')
            jingyan = d[1]
            juzhudi = d[4]
            hujidi = d[7]
            if hujidi=='暂不合适':
                hujidi = ''
            # print(jingyan,juzhudi,hujidi)
            e = html.xpath('//dl[@class="resume-box"]/dd/p/span//text()')
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
                # print(qiuzhizhuangtai, qiwangdidian, qiwangzhiwei, gongzuoxingzhi, qiwanghangye, qiwangxinzi,'888888')

            # print(qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,qiwanghangye,qiwangxinzi)
            f = html.xpath('//div[@class="resume_detail_html"]/dl[@class="resume-box"]/dd/div[@class="experience"]/span/text()')
            jiaoyujingli = ' '.join(f)
            # print(g)

            sql = "insert into zhaopingou (name,zhiwei,gender,marry,age,education,guoji,zhengzhi,jingyan,juzhudi,hujidi,qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,qiwanghangye,qiwangxinzi,jiaoyujingli,chusheng,gongzuoxingzhi) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (name,zhiwei,gender,marry,age,education,guoji,zhengzhi,jingyan,juzhudi,hujidi,qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,qiwanghangye,qiwangxinzi,jiaoyujingli,chusheng,gongzuoxingzhi)
            cursor.execute(sql)
            conn.commit()
        except:
            pass

