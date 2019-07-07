import os,MySQLdb

# path = 'E:\python\lixianshuju\word1'
# list1 = os.listdir(path)
# # print(list1)
# for p in list1:
#     # print(p)
#     name = os.path.splitext(p)[0].split('_')[0]
#     # print(name)
#     path = r'E:\python\lixianshuju\word1\%s' % p
#
#     with open(path, 'r') as r:
#         txt = r.readlines()
#         # print(txt)
#         zhiwei = txt[3].split(' ')
#         print(zhiwei)


conn = MySQLdb.connect(
    host='localhost',
    db='houqi_project',
    user='root',
    password='123456',
    port=3306,
    charset='utf8')
cursor = conn.cursor()

path1 = 'E:\python\lixianshuju\word1'
paths1 = os.listdir(path1)

def wipe(a):
    return a.replace('\n','').replace('\t','').replace('\r','').replace(' ','')


def get_to_txt(path):
    with open(path,'r') as r:
        txt = r.readlines()
        print(txt)
        try:
            zhiye = txt[3].split(' ') [-1]     #职业
        except:
            zhiye = ''
        # print(zhiye)
        try:
            gender = txt[6].split('|')[0].replace(' ','')   #性别
        except:
            gender = ''
        marry = txt[6].split('|')[1].replace(' ', '')
        if '婚' in marry:
            marry = txt[6].split('|')[1].replace(' ','')      #年龄
        else:
            marry = ''
        if '岁' in marry:
            age = txt[6].split('|')[1].replace(' ','')      #年龄
        else:
            age = ''
        try:
            birthday = txt[6].split('|')[2].replace(' ','')          #生日
        except:
            birthday = ''
        try:
            xueli = txt[6].split('|')[3].replace(' ','')   #学历
        except:
            xueli = ''
        try:
            guoji = wipe(txt[6].split('|')[4])        #国籍
        except:
            guoji = '中国'
        try:
            zhengzhi = wipe(txt[6].split('|')[5])       #政治
        except:
            zhengzhi = ''
        try:
            jingyan = wipe(txt[8].split('：')[1])           #经验
        except:
            jingyan = ''
        try:
            juzhudi = wipe(txt[9].split('：')[1])        #地址
        except:
            juzhudi = ''
        try:
            phone = wipe(txt[10].split('：')[1])        #电话
        except:
            phone = ''
        try:
            email = wipe(txt[11].split('：')[1])         #电子邮箱
        except:
            email = ''
        try:
            qiuzhizhuangtai = wipe(txt[18])                      #求职状态
        except:
            qiuzhizhuangtai = ''
        try:
            qiwangdidian = wipe(txt[20])                     #期望地点
        except:
            qiwangdidian = ''
        try:
            qiwangzhiwei = wipe(txt[22])                  #期望职位
        except:
            qiwangzhiwei = ''
        try:
            gongzuoxingzhi = wipe(txt[24])                #工作性质
        except:
            gongzuoxingzhi = ''
        try:
            qiwanghangye = wipe(txt[26])                   #期望行业
        except:
            qiwanghangye = ''
        try:
            qiwangxinzi = wipe(txt[28])                     #期望薪资
        except:
            qiwangxinzi = ''
        try:
            daogangshijian = wipe(txt[30])                #到岗时间
        except:
            daogangshijian = ''
        try:
            zaixiaoshijian = wipe(txt[33].split(r'\u3000\u3000\u3000')[0])  #在校时间
        except:
            zaixiaoshijian = ''
        try:
            school = wipe(txt[33].split(r'\u3000\u3000\u3000')[1])              #学校
        except:
            school = ''
        try:
            zhuanye = wipe(txt[33].split(r'\u3000\u3000\u3000')[3])        #专业
        except:
            zhuanye = ''
        print(name,zhiye,gender,marry,age,birthday,xueli,guoji,zhengzhi,jingyan,juzhudi,phone,email,qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,gongzuoxingzhi,qiwanghangye,qiwangxinzi,daogangshijian,zaixiaoshijian,school,zhuanye)
        sql = 'insert into t_word(name,zhiye,gender,marry,age,birthday,xueli,guoji,zhengzhi,jingyan,juzhudi,phone,email,qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,gongzuoxingzhi,qiwanghangye,qiwangxinzi,daogangshijian,zaixiaoshijian,school,zhuanye) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, [name,zhiye,gender,marry,age,birthday,xueli,guoji,zhengzhi,jingyan,juzhudi,phone,email,qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,gongzuoxingzhi,qiwanghangye,qiwangxinzi,daogangshijian,zaixiaoshijian,school,zhuanye])
        conn.commit()
for p in paths1:
    name = os.path.splitext(p)[0].split('_')[0]
    # global name
    path = r'E:\python\lixianshuju\word1\%s' % p
        # print(path)
    get_to_txt(path)