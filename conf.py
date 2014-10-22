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

bailu = Bag()

tornado_settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies = True,
    cookie_secret = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url = "/oauth/weibo",
    debug = True,
)