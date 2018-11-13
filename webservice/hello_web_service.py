# -*- coding: utf-8 -*-
"""
    reference: http://www.cnblogs.com/aylin/p/5702994.html
"""
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello World, web service")


application = tornado.web.Application([
    (r'/index', IndexHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()