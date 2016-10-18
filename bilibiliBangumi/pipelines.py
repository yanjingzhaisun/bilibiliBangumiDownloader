# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import datetime

class BilibilibangumiPipeline(object):
    def process_item(self, item, spider):
        targetLink = item['link'][0]
        #print(targetLink)
        foldername = '~/Movies/temp/' + datetime.datetime.now().strftime('%Y%m%d')
        os.system('mkdir -p ' + foldername )
        bashCommand = "youtube-dl -o '" + foldername + "/%(title)s.%(ext)s' "
        #os.system(bashCommand + targetLink + " &")
        #for test   
        print(bashCommand + targetLink + " &")
        return item
