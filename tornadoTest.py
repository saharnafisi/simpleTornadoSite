import tornado.web
import tornado.ioloop

class mainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("get request send")
    
    def post(self):
        #self.write("post request send")
        items=["صفحه اصلی","ثبت نام","ورود","درباره ما","خروج"]
        #items=["sahar"]
        name="sahar"
        self.render("header.html" ,items=items, name=name)


if __name__=="__main__":
    app=tornado.web.Application([(r"/",mainHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()