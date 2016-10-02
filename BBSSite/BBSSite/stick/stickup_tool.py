#!/usr/bin/env python
# -*- coding: utf-8 -*-
# QingTao
import re

import requests
from bs4 import BeautifulSoup

from BBSSite.model.category import Category

news_url = 'http://bbs.xjtu.edu.cn/BMYAASHMFXVPBATHNVWLJZOKBAFYTPMNZPWV_B/con?B=XJTUnews&F=M.1473991809.A&N=113252&st=1&T=0'
reply_url = 'http://bbs.xjtu.edu.cn/BMYAASHMFXVPBATHNVWLJZOKBAFYTPMNZPWV_B/pst?B=XJTUnews&F=M.1473991809.A&num=113251'
post_form_url = 'http://bbs.xjtu.edu.cn/BMYAASHMFXVPBATHNVWLJZOKBAFYTPMNZPWV_B/bbssnd?board=XJTUnews&th=1473991809&ref=M.1473991809.A&rid=113251'


def stick_tool(my_url, new_url, reply_content):
    # print 'reply_url -----------', reply_url
    new_html = requests.get(new_url).text
    soup = BeautifulSoup(new_html, 'lxml')

    a = soup.find('a', href=re.compile('pst\?B='))

    if a is not None:
        reply_url = my_url + a['href']

    print 'reply_url -----------', reply_url

    reply_html = requests.get(reply_url).text
    soup = BeautifulSoup(reply_html, 'lxml')

    inputtitle = soup.find('input', {'class': 'inputtitle'}).get('value')
    print 'inputtitle -----------', type(inputtitle)

    default_text = soup.find('textarea').text

    form_action = soup.find('form', {'name': 'form1'}).get('action')

    post_form_url = my_url + form_action

    payload = {'title': inputtitle.encode('gbk'),
               'text': reply_content.encode('gbk') + default_text.encode('gbk', 'replace')}
    response = requests.post(post_form_url, data=payload)
    return response.status_code


if __name__ == "__main__":
    stick_tool('http://bbs.xjtu.edu.cn/BMYAAIAJJAGFOIBXHVRQEEWBAMJYCYYRBCUX_B/',
               'http://bbs.xjtu.edu.cn/BMYAAIAJJAGFOIBXHVRQEEWBAMJYCYYRBCUX_B/con?B=SecondHand&F=M.1475288745.A&N=62597&T=0',
               '')
