# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook


class LanxixiaowuPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['帖子名称', '浏览量'])

    def process_item(self, item, spider):
        line = [item['name'], item['views']]
        self.ws.append(line)
        self.wb.save(item['title']+'.xlsx')
        return item
