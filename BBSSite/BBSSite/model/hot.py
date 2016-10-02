#!/usr/bin/env python
# -*- coding: utf-8 -*-
# QingTao

class Hot:
    def __init__(self, ranking, talk_area, talk_area_url, title, title_url, people_num):
        self.ranking = ranking
        self.talk_area = talk_area
        self.talk_area_url = talk_area_url
        self.title = title
        self.title_url = title_url
        self.people_num = people_num

    # def __str__(self):
    #     return self.ranking + " " + self.talk_area + " " + self.title +  " " +self.people_num
