#!/usr/bin/env python
# -*- coding: utf-8 -*-
# QingTao

'''
模拟登陆
'''

import requests
from bs4 import BeautifulSoup
import urlparse



def login_tool(username='LeoTao', pwd='19940623tao;'):
    home_url = 'http://bbs.xjtu.edu.cn'
    login_url = 'http://bbs.xjtu.edu.cn/BMY/bbslogin'
    payload = {'id': username, 'pw': pwd}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        'Connection': 'keep-alive'
    }
    s = requests.Session()
    response = s.post(login_url, data=payload, headers=headers)
    # response = requests.post(login_url, data=payload)
    '''
    这里返回了url地址， 拼接地址就可以访问自己的主页了
    '''
    soup = BeautifulSoup(response.text, 'html.parser')

    # print 'result: ', soup.prettify()
    url_content = soup.findAll('meta')[-1]
    if url_content is not None:
        login_url = url_content.get('content')[7:]
    my_url = urlparse.urljoin(home_url, login_url) #获取到自己的主页
    print my_url
    return my_url #返回我的主页链接


if __name__ == '__main__':
    login()