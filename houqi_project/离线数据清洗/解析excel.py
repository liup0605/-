import pandas as pd
import numpy as np
import os
import MySQLdb
conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='houqi_project',
            charset="utf8"
        )
cur = conn.cursor()
path='E:\python\lixianshuju\excel'
dirs=os.listdir(path)
# print(dirs)
for i in dirs:
    # print(i)
    f=pd.read_excel('E:\python\lixianshuju\excel\%s'%i)
    datas=np.array(f).tolist()
    # print(datas)
    for ds in datas:
        data=[ str(i) for i in ds]
        print(data)
        if '数据1' in i:
            name=data[0]
            xueli=data[1]
            gongzuoxingzhi=data[2]
            jingyan=data[3]
            age=data[4]
            hujidi=data[5]
            qiwangdidian=data[6]
            qiwangxinzi=data[7]
            qiwanghangye=data[8]
            qiuzhizhuangtai=data[9]
            juzhudi=data[10]
            birthday=data[11]
            email=data[12]
            phone=data[13]
            sql = 'insert into t_excel(name,xueli,gongzuoxingzhi,jingyan,age,hujidi,qiwangdidian,qiwangxinzi,qiwanghangye,qiuzhizhuangtai,juzhudi,birthday,email,phone)  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, [name,xueli,gongzuoxingzhi,jingyan,age,hujidi,qiwangdidian,qiwangxinzi,qiwanghangye,qiuzhizhuangtai,juzhudi,birthday,email,phone])
            conn.commit()
        elif '数据2' in i:
            sql='select id from t_excel where phone=%s '
            toal=cur.execute(sql,[data[14]])
#
            name=data[0]
            marry=data[1]
            xueli=data[2]
            gongzuoxingzhi=data[3]
            jingyan=data[4]
            age=data[5]
            hujidi=data[6]
            qiwangdidian=data[7]
            qiwangxinzi=data[8]
            qiwanghangye=data[9]
            qiuzhizhuangtai=data[10]
            juzhudi=data[11]
            birthday=data[12]
            email=data[13]
            phone=data[14]
            if toal == 0:
                sql = 'insert into t_excel(name,marry,xueli,gongzuoxingzhi,jingyan,age,hujidi,qiwangdidian,qiwangxinzi,qiwanghangye,qiuzhizhuangtai,juzhudi,birthday,email,phone)  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(sql, [name,marry,xueli,gongzuoxingzhi, jingyan, age, hujidi, qiwangdidian, qiwangxinzi, qiwanghangye,qiuzhizhuangtai, juzhudi, birthday, email, phone])
                conn.commit()
            else:
                id=cur.fetchone()[0]
#                 print(id)
                sql='update t_excel set marry=%s where id=%s;'
                cur.execute(sql,[marry,id])
                conn.commit()
        elif '数据3' in i:
            print(data)
            sql = 'select id from t_excel where phone=%s '
            toal = cur.execute(sql, [data[15]])
            name = data[0]
            marry = data[1]
            xueli = data[2]
            gongzuoxingzhi = data[3]
            jingyan = data[4]
            age = data[5]
            hujidi = data[6]
            qiwangdidian = data[7]
            qiwangxinzi = data[9]
            qiwangzhiwei = data[8]
            qiwanghangye=data[10]
            qiuzhizhuangtai = data[11]
            juzhudi = data[12]
            birthday = data[13]
            email = data[14]
            phone = data[15]
            if toal == 0:
                sql = 'insert into t_excel(name,marry,xueli,gongzuoxingzhi,jingyan,age,hujidi,qiwangdidian,qiwangxinzi,qiwanghangye,qiwangzhiwei,qiuzhizhuangtai,juzhudi,birthday,email,phone)  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(sql,[name,marry,xueli,gongzuoxingzhi, jingyan, age, hujidi, qiwangdidian, qiwangxinzi, qiwanghangye,qiwangzhiwei,qiuzhizhuangtai, juzhudi, birthday, email, phone])
                conn.commit()
            else:
                id = cur.fetchone()[0]
                print(id)
                sql = 'update t_excel set qiwangzhiwei=%s where id=%s;'
                cur.execute(sql, [qiwangzhiwei,id])
                conn.commit()



