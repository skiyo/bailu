# -*-coding:UTF-8-*-

import sys, MySQLdb, traceback, time

class DB:
    def __init__ (self,
                  host   = '',
                  user   = '',
                  passwd = '',
                  db     = '',
                  port   = 3306,
                  charset= 'utf8'
                  ):
        self.host   = host
        self.user   = user
        self.passwd = passwd
        self.db     = db
        self.port   = port
        self.charset= charset
        self.conn   = None
        self._conn()

    def _conn (self):
        try:
            self.conn = MySQLdb.Connection(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port , charset=self.charset)
            #self.cursor.execute ("set names utf8") #utf8 字符集
            return True
        except :
            return False

    def _reConn (self, num = 28800, stime = 3):
        _number = 0
        _status = True
        while _status and _number <= num:
            try:
                self.conn.ping() 
                _status = False
            except:
                if self._conn()==True: 
                    _status = False
                    break
                _number +=1
                time.sleep(stime)

    def select (self, sql = ''):
        self._reConn()
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        self.cursor.execute (sql)
        result = self.cursor.fetchall()
        self.cursor.close ()
        return result

    def query (self, sql = ''):
        self._reConn()
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        result = self.cursor.execute (sql)
        self.conn.commit()
        self.cursor.close ()
        return (True, result)

    def escape(self, str):
        return self.conn.escape_string(str)

    def close (self):
        self.conn.close()
