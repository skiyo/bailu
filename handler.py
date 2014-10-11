# -*- coding:utf8 -*-
import tornado.web
from pyoauth2 import Client
import conf

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('not login')


class OAuthWeiboHandler(tornado.web.RequestHandler):
	def get(self):
		pass

class OauthWeiboCallbackHandler(tornado.web.RequestHandler):
	def get(self):
		pass


class SpotHandler(tornado.web.RequestHandler):
	def get(self, spot):
		self.write(spot)

class PageNotFoundHandler(tornado.web.RequestHandler):
	def get(self):
		print "PageNotFound"
