#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 17:52
# @Author  : 冉勇
# @Site    : 
# @File    : config.py
# @Software: PyCharm
# @desc    : 配置管理
import json

# 位置内容字符串
UNKNOWN_DEFAULT = 'UNKNOWN'


class Config:
    """
    配置管理器
    """
    def __init__(self, filename: str):
        """
        初始化配置管理器
        :param filename: 配置json文件
        """
        fp = open(filename, 'r', encoding="utf-8")
        if fp == None:
            raise FileNotFoundError("[Config] 未能找到配置文件config.json")
        self.params: dict = json.load(fp)

    def getr(self, key: str) -> any:
        """
        获取key对应配置
        :param key:
        :return:
        """
        if key in self.params.keys():
            return self.params[key]
        raise Exception(f'[Config] 未能在配置中找到key:"{key}"对应项')


