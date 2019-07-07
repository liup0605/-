# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class WanhangPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='houqi_project', port=3306,
                           charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql = "insert into wanhang (id,name,gender,age,jiguan,jingyan,education,city,yixiangzhiwei,salary,gongzuoxingzhi,daogangshijian,school) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,[item['id'], item['name'], item['gender'], item['age'], item['jiguan'],item['jingyan'],item['education'],item['city'],item['yixiangzhiwei'],item['salary'],item['gongzuoxingzhi'],item['daogangshijian'],item['school']])
        self.conn.commit()
        return item
