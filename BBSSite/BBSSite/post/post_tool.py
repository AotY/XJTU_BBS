#!/usr/bin/env python
# -*- coding: utf-8 -*-
# QingTao

# http://bbs.xjtu.edu.cn/BMYAHMRBMKZRSHHLPANBIEWFLSHELXYWPFEO_B/tdoc?board=XJTUnews
import requests

from BBSSite.model.category import Category

post_url_dict = {
    'XJTUnews': 'bbssnd?board=XJTUnews&th=-1',
    'dance': 'bbssnd?board=dance&th=-1',
    'Photography': 'bbssnd?board=Photography&th=-1',
    'PieBridge': 'bbssnd?board=PieBridge&th=-1',
    'SecondHand': 'bbssnd?board=SecondHand&th=-1',
    'Art': 'bbssnd?board=Art&th=-1',
    'Joke': 'bbssnd?board=Joke&th=-1',
    'Cycling': 'bbssnd?board=Cycling&th=-1',
    'Running': 'bbssnd?board=Running&th=-1',
    'Fitness': 'bbssnd?board=Fitness&th=-1',
    'Emprise': 'bbssnd?board=Emprise&th=-1',

}


def get_post_categories(my_url):
    categories = []
    for post in post_url_dict.items():
        category = Category(post[0], my_url + post[1])
        categories.append(category)
    return categories

def post_tool(my_url, category, title, content):
    print my_url, category, title.encode('gbk'), content.encode('gbk')
    post_url = my_url + post_url_dict.get(category)
    edittitle = title.encode('gbk')
    text = content.encode('gbk')
    payload = {'title': edittitle, 'text': text}
    print 'payload------', payload
    response = requests.post(post_url, data=payload)
    return response.status_code

