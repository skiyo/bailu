# -*- coding:utf8 -*-
import tornado.web
from model.weibo import Weibo
import conf
import se
import json

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        if self.get_secure_cookie('t'):
            return json.loads(self.get_secure_cookie('t'))

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        wb = Weibo(self.current_user)
        self.write(wb.get_user_info(self.current_user['uid']))

class SpotHandler(BaseHandler):
    def get(self, spot):
        self.write(spot)

class SugHandler(BaseHandler):
    def get(self):
        self.write(se.search(self.get_argument("q")))

class OAuthWeiboHandler(tornado.web.RequestHandler):
    def get(self):
        wb = Weibo()
        self.redirect(wb.authorize())

class OauthWeiboCallbackHandler(tornado.web.RequestHandler):
    def get(self):
        wb = Weibo()
        wb.set_code(self.get_argument('code'))
        token = wb.get_token()
        self.set_secure_cookie('t', json.dumps(token), 1)
        self.redirect('/')

class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Not Found.')
