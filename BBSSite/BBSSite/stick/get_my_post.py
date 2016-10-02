#!/usr/bin/env python
# -*- coding: utf-8 -*-
# QingTao
import requests
from bs4 import BeautifulSoup

from BBSSite.model.post import Post
import re

def get_my_post(my_url):
    post_form_url = my_url + 'bbsfind'
    payload = {'user': 'LeoTao', 'day': 60}
    # r = requests.get(post_form_url, params=payload)
    response = requests.post(post_form_url, data=payload)
    # print 'get_my_post------------', response.text
    my_posts = parse_list(response.text, my_url)
    return my_posts



def parse_list(content, my_url):
    soup = BeautifulSoup(content, 'html.parser')
    # print soup.prettify()
    posts = []
    # aa = soup.findAll('a', {'href', r'con(.*)'})
    # soup.find_all('div', class_=re.compile('comment-'))
    aa = soup.find_all('a', href=re.compile('con\?B='))
    for a in aa:
        # print 'a----------:', a
        title = a.text
        url = a.get('href')
        post = Post('', '', title, my_url + url)
        posts.append(post)


    # trs = soup.findAll('tr')
    # for tr in trs:
    # tds = trs[0].findAll('td')
    # print 'tr---------------: ', trs[0]

    # author = tds[1].find('a').text

    # date = tds[-2].text


    # print title
    # print len(trs)
    return posts
if __name__ == '__main__':
    my_url = 'http://bbs.xjtu.edu.cn/BMYAHMRBMKZRSHHLPANBIEWFLSHELXYWPFEO_B/'
    get_my_post(my_url)