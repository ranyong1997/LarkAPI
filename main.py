#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 11:08
# @Author  : 冉勇
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @desc    :
import asyncio
from app.larkcustombot import post
from app.larkcustombot.larkcustombot import LarkCustomBot

# 机器人webhook
webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/fce32975-4d2f-49ab-b7a0-72921b173bb9"
# 如果你给机器人设置了签名：
secret = ''
feishu = LarkCustomBot(webhook=webhook, secret=secret)
# 发送文本消息并艾特全体（默认加在文本最后）：
# asyncio.run(feishu.send_text(text="text content", is_at_all=True))
first_line = [post.content_text('测试'), post.content_a(
    href='baidu.com', text='百度')]
# 第二行，以此类推
second_line = [post.content_imag(
    'img_v2_57d3b923-97af-42ed-8909-6d81ac0fc76g')]

asyncio.run(feishu.send_post(first_line, second_line, title='测试'))
