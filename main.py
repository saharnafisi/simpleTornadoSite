import tornado.web
import tornado.ioloop
import os
import sqlite3
import re


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("get request send")
        self.render("Base.html")

    def post(self):
        self.write("post request send")
        #items = ["صفحه اصلی", "ثبت نام", "ورود", "درباره ما", "خروج"]
        # items=["sahar"]


class RegisterUser(tornado.web.RequestHandler):
    def get(self):
        self.render("Register.html")

    def post(self):
        fname = self.get_argument("fname")
        lname = self.get_argument("lname")
        userName = self.get_argument("userName")
        education = self.get_argument("education")
        email = self.get_argument("email")
        password = self.get_argument("password")
        key = self.get_argument("key")
        query = """INSERT INTO 'user'('firstName','lastName','userName','education','email','password','keys')
         VALUES(?,?,?,?,?,?,?)"""
        cursor = self.application.db.cursor()
        cursor.execute(query, [fname, lname, userName,
                               education, email, password, key])
        #cursor.execute(query, ["sahar", "nafisi", "diplom", "sahar@gmail.com", "123", "sssss"])
        self.application.db.commit()
        self.redirect("/addUser")

class ShowUser(tornado.web.RequestHandler):
    def get(self,userName):
        query="SELECT * FROM 'user' WHERE userName=?"
        cursor = self.application.db.cursor()
        cursor.execute(query, [userName])
        self.application.db.commit()
        user=cursor.fetchone()
        user=str(user)
        self.write(user)

if __name__ == "__main__":
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "template_path": os.path.join(os.path.dirname(__file__), "templates")
    }

    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/addUser", RegisterUser),
        (r"/users/([a-zA-Z0-9]+)",ShowUser)
    ], **settings)

    app.db = sqlite3.connect("site.db")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
