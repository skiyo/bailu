# -*- coding:utf8 -*-

import os

class Bag: pass

server = Bag()
server.port = 80
server.process_num = 1

bailu = Bag()
bailu.mysql = Bag()
bailu.mysql.user = 'root'
bailu.mysql.password = 'root'
bailu.mysql.host = '127.0.0.1'
bailu.mysql.port = 3306

tornado_settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	xsrf_cookies = True,
	cookie_secret = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
	login_url = "/oauth/weibo",
	debug = True,
)