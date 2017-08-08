import tornado.web
import tornado.ioloop
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("get request send")

    def post(self):
        #self.write("post request send")
        items = ["صفحه اصلی", "ثبت نام", "ورود", "درباره ما", "خروج"]
        # items=["sahar"]
        name = "sahar"
        self.render("header.html", items=items, name=name)


if __name__ == "__main__":
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

    app = tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)


    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()