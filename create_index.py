# -*-coding:UTF-8-*-

import sys
import conf
from libs.db import DB
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer


if __name__ == "__main__" :

    reload(sys)
    sys.setdefaultencoding('utf-8')

    sql = DB(conf.mysql.host, conf.mysql.username, conf.mysql.password, conf.mysql.db, conf.mysql.port, conf.mysql.charset)

    all_data = sql.select("SELECT * FROM spot")

    analyzer = ChineseAnalyzer()


    schema = Schema(title=TEXT(stored=True, analyzer=analyzer), path=ID(stored=True), hot=NUMERIC(sortable=True))
    ix = create_in("index", schema)
    writer = ix.writer()

    for data in all_data:
        writer.add_document(title=data["title"].strip() + u"\t" + data["address"].strip(), path=unicode(data["id"]), hot=(int(data["hot"])+int(data["comment_num"])*10))

    writer.commit()

    searcher = ix.searcher()
    parser = QueryParser("content", schema=ix.schema)

    q = parser.parse(u"东方")
    results = searcher.search(q, terms=True)

    print results
