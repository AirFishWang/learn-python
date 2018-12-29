# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     server
   Description :
   Author :        wangchun
   date：          18-12-29
-------------------------------------------------
   Change Activity:
                   18-12-29:
-------------------------------------------------
"""
import logging
import json
import traceback
import tornado.web
import tornado.ioloop
from tornado.escape import json_encode


def fun(x, y):
    return x + y


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello World, web service")

    @tornado.web.asynchronous
    def post(self):
        try:
            arg = self.request.arguments
            x = self.request.arguments.get('x')[0]
            y = self.get_argument('y')
            sum = fun(x, y)
            result = json_encode({'sum': sum})
            self.write(result)
        except Exception, e:
            traceback.print_exc()
            logging.exception(e)
            self.write("error")

        self.finish()


application = tornado.web.Application([
    (r'/index', IndexHandler),               # open http://127.0.0.1:8080/index
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()