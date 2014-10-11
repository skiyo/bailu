# -*- coding:utf8 -*-

import tornado.web
import conf
import handler

controller = [
	(r"/", handler.IndexHandler),
	(r"/oauth/weibo", handler.OAuthWeiboHandler),
	(r"/oauth/weibo_callback", handler.OauthWeiboCallbackHandler),
	(r".*", handler.PageNotFoundHandler),
]