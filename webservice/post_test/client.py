# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     client
   Description :
   Author :        wangchun
   date：          18-12-29
-------------------------------------------------
   Change Activity:
                   18-12-29:
-------------------------------------------------
"""
import json
import urllib
import urllib2

if __name__ == "__main__":
    url = "http://127.0.0.1:8080/index"
    params = {"x": 4,  "y": 5}
    data = urllib.urlencode(params)
    request = urllib2.Request(url, data)
    result_str = urllib2.urlopen(request, timeout=60).read()
    result = json.loads(result_str)
    print result