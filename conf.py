# -*- coding:utf8 -*-

import os

class Bag: pass

server = Bag()
server.port = 80
server.process_num = 1

mysql = Bag()
mysql.username = 'root'
mysql.password = 'root'
mysql.host = '127.0.0.1'
mysql.port = 3306
mysql.db = 'bailu'
mysql.charset = 'utf8'

weibo = Bag()
weibo.api_key = '3649416783'
weibo.api_secret = '24843e6843b5a8319201991e5d0a4d75'
weibo.redirect_url = 'http://127.0.0.1/oauth/weibo_callback'

bailu = Bag()

tornado_settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies = True,
    cookie_secret = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url = "/oauth/weibo",
    debug = True,
)