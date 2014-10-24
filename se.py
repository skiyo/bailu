# -*-coding:UTF-8-*-

import sys
import pprint
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer

reload(sys)
sys.setdefaultencoding('utf-8')

analyzer = ChineseAnalyzer()

ix = open_dir("index")

searcher = ix.searcher()
parser = QueryParser("title", schema=ix.schema)


def search(query):
    q = parser.parse(unicode(query))
    results = searcher.search(q, terms=True, sortedby="hot", reverse=True, limit=5)
    ret = {}
    ret["term"] = []
    ret["spot"] = []
    for h in results:
        for t in h.matched_terms():
            ret["term"].append(t[1].decode('utf-8'))

        ret["spot"].append({
            "id" : int(h["path"]),
            "rank" : int(h["hot"]),
            "title" : h["title"].split("\t")[0],
            "address" : h["title"].split("\t")[1]
        })

    ret["term"] = list(set(ret["term"]))
    return ret


if __name__ == "__main__" :
    print search("九寨沟")