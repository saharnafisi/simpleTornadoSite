import tornado.web
import tornado.ioloop
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("get request send")
        items = ["صفحه اصلی", "ثبت نام", "ورود", "درباره ما", "خروج"]
        self.render("header.html",items=items)

    def post(self):
        #self.write("post request send")
        items = ["صفحه اصلی", "ثبت نام", "ورود", "درباره ما", "خروج"]
        # items=["sahar"]
        


if __name__ == "__main__":
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

    app = tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)


    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()