# -*-coding:UTF-8-*-

import sys
import conf
from libs.db import DB

if __name__ == "__main__" :

    reload(sys)
    sys.setdefaultencoding('utf-8')

    sql = DB(conf.mysql.host, conf.mysql.username, conf.mysql.password, conf.mysql.db, conf.mysql.port, conf.mysql.charset)

    f = open('dict/spot', 'r')
    for line in open('dict/spot'):
        (title, address) = f.readline().split("\t")
        sql.query("INSERT INTO spot (title, address) VALUES('"+sql.escape(title)+"', '"+sql.escape(address)+"')")