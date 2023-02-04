#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 10:56
# @Author  : 冉勇
# @Site    : 
# @File    : sdk.py
# @Software: PyCharm
# @desc    :
from doctest import FAIL_FAST
import requests
from requests_toolbelt import MultipartEncoder


def uploadImage(path, tenant_access_token):
    """
    上传图片
    :param path: 图片路径地址
    :param tenant_access_token: 自建应用机器人的token
    :return:
    """
    url = "https://open.feishu.cn/open-apis/im/v1/images"
    form = {'image_type': 'message',
            'image': (open(path, 'rb'))}  # 需要替换具体的path
    multi_form = MultipartEncoder(form)
    headers = {'Authorization': f'Bearer {tenant_access_token}', 'Content-Type': multi_form.content_type}
    response = requests.request("POST", url, headers=headers, data=multi_form)
    print(response.headers['X-Tt-Logid'])  # 用于调试或oncall
    print(response.content)  # 打印响应


if __name__ == '__main__':
    uploadImage(path='../../images/1.png', tenant_access_token="t-g10422aADBAULX7ZYD2ZWWEDDDGXDTBA73XP24GS")
