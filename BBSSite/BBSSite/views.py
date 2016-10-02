#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render, render_to_response

from BBSSite.login.login_tool import login_tool
from BBSSite.post.post_tool import get_post_categories, post_tool
from BBSSite.stick.get_my_post import get_my_post
from BBSSite.stick.reply_dict import get_replies
from BBSSite.stick.stickup_tool import stick_tool
from BBSSite.top_ten.top_ten_tool import get_top_ten

my_url = None


def login(request):
    global my_url
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    my_url = login_tool(username, pwd)
    return my_url


def top_ten(request):
    global my_url
    if request.method == 'GET':
        if my_url is None:
            # login(request)
            return render(request, 'BBSSite/login.html')
        else:
            # 获取十大
            try:
                hots = get_top_ten(my_url)
            except:
                my_url = None
                return render(request, 'BBSSite/login.html')
            return render(request, 'BBSSite/top_ten.html', {'hots': hots})
    else:
        my_url = login(request)
        # 获取十大
        hots = get_top_ten(my_url)
        return render(request, 'BBSSite/top_ten.html', {'hots': hots})


# 我要发帖
def to_post(request):
    global my_url
    if request.method == 'GET':
        if my_url is None:
            # login(request)
            return render(request, 'BBSSite/login.html')
        else:
            categories = get_post_categories(my_url)
            return render(request, 'BBSSite/to_post.html', {'categories': categories})

    else:
        my_url = login(request)
        categories = get_post_categories(my_url)
        return render(request, 'BBSSite/to_post.html', {'categories': categories})


category = None


def post(request):
    if request.method == "GET":
        return render(request, 'BBSSite/post.html')
    else:
        if request.POST.get('category') is None or request.POST.get('category') == '':
            if category is not None:
                title = request.POST.get('title')
                content = request.POST.get('content')

                print 'category========', category
                status_code = post_tool(my_url, category, title, content)
                if status_code == 200:
                    notification = u'发帖成功, 继续发帖或者返回'
                else:
                    notification = u'发帖失败'
                # return request
                # return render(request, 'BBSSite/post.html', {'title': title, 'content': content, 'notification': notification})
                return render(request, 'BBSSite/notification.html', {'notification': notification})
            else:
                # return render(request, 'BBSSite/post.html', {'notification': ''})
                return render(request, 'BBSSite/notification.html', {'notification': ''})
        else:
            global category
            category = request.POST.get('category')
            print 'category-------------', category
        return render(request, 'BBSSite/post.html')


# 我要顶贴
def stick_post(request):
    global my_url
    if request.method == 'GET':
        if my_url is None:
            my_url = login(request)
            posts = get_my_post(my_url)
            return render(request, 'BBSSite/stick_post.html', {'posts': posts})
        else:
            # 我的发帖
            posts = get_my_post(my_url)
            return render(request, 'BBSSite/stick_post.html', {'posts': posts})
    else:
        my_url = login(request)
        # 我的发帖
        posts = get_my_post(my_url)
        return render(request, 'BBSSite/stick_post.html', {'posts': posts})


reply_url = None


def reply(request):
    if request.method == "GET":
        replies = get_replies()
        return render(request, 'BBSSite/reply.html', {'replies': replies})
    else:

        if request.POST.get('reply_url') is None or request.POST.get('reply_url') == '':
            if reply_url is not None:
                reply_content = request.POST.get('reply-content')
                status_code = stick_tool(my_url, reply_url, reply_content)
                if status_code == 200:
                    notification = u'顶贴成功, 继续发帖或者返回'
                else:
                    notification = u'顶贴失败'
                return render(request, 'BBSSite/notification.html', {'notification': notification})
            else:
                return render(request, 'BBSSite/notification.html', {'notification': ''})
        else:
            global reply_url
            reply_url = request.POST.get('reply_url')
            replies = get_replies()
            print 'reply_url-------------', reply_url
            return render(request, 'BBSSite/reply.html', {'replies': replies})


def notification(request):
    return render(request, 'BBSSite/notification.html', {'notification': ''})
