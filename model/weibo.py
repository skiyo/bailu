# -*- coding:utf8 -*-

from libs.weibo import Client
import conf
import base64

class Weibo:

    def __init__(self, access_token = ''):
        if len(access_token) > 0:
            self.c = Client(conf.weibo.api_key, conf.weibo.api_secret, conf.weibo.redirect_url, access_token)
        else:
            self.c = Client(conf.weibo.api_key, conf.weibo.api_secret, conf.weibo.redirect_url)

    def authorize(self):
        return self.c.authorize_url

    def set_code(self, code):
        self.c.set_code(code)

    def get_token(self):
        return self.c.token

    def get_user_info(self, uid):
        return self.c.get('users/show', uid = uid)

    def get_current_uid(self):
        return self.c.get('account/get_uid')