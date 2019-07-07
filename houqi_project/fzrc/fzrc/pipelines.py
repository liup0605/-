# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class FzrcPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='houqi_project', port=3306,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into zhaopingou (name,zhiwei,gender,marry,age,education,jingyan,juzhudi,hujidi,qiuzhizhuangtai,qiwangdidian,qiwangzhiwei,qiwanghangye,qiwangxinzi) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,
                            [item['name'], item['zhiwei'], item['gender'], item['marry'], item['age'],
                             item['education'], item['jingyan'], item['juzhudi'],
                             item['hujidi'], item['qiuzhizhuangtai'], item['qiwangdidian'], item['qiwangzhiwei'],
                             item['qiwanghangye'], item['qiwangxinzi']])
        self.conn.commit()
        return item
