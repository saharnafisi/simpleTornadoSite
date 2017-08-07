import tornado.web
import tornado.ioloop

class mainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")




if __name__=="__main__":
    app=tornado.web.Application([(r"/main",mainHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()