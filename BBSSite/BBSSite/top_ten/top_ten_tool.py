#!/usr/bin/env python
# -*- coding: utf-8 -*-
# QingTao
import requests
from bs4 import BeautifulSoup

from BBSSite.model.hot import Hot


def get_top_ten(my_url):
    r = requests.get(my_url + 'bbstop10')
    soup = BeautifulSoup(r.text, 'html.parser')

    tables = soup.findAll('table', {'border': 1})
    # print len(tables)
    # 获取今日十大热门话题 名次	讨论区	标题	人数
    table1 = tables[0]
    trs = table1.findAll('tr')[1:]
    hot_talks = []
    for tr in trs:
        tds = tr.findAll('td')
        # 名次
        ranking = tds[0].text
        # 讨论区
        talk_area_name = tds[1].text
        talk_area_url = tds[1].find('a').get('href')
        # 标题
        title = tds[2].text
        title_url = tds[2].find('a').get('href')
        # 人数
        people_num = tds[-1].text
        hot = Hot(ranking, talk_area_name, my_url + talk_area_url, title, my_url + title_url, people_num)
        hot_talks.append(hot)

    # for h in hot_talks:
    #     print h.title
    #     print h.title_url
    #     print h.talk_area
    #     print h.talk_area_url
    #     # print hot_talks
    return hot_talks
if __name__ == '__main__':
    my_url = 'http://bbs.xjtu.edu.cn/BMYAHMRBMKZRSHHLPANBIEWFLSHELXYWPFEO_B/'
    get_top_ten(my_url)