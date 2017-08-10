import tornado.web
import tornado.ioloop
import os
import sqlite3
import re


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("get request send")
        items = ["صفحه اصلی", "ثبت نام", "ورود", "درباره ما", "خروج"]
        self.render("header.html", items=items)

    def post(self):
        #self.write("post request send")
        items = ["صفحه اصلی", "ثبت نام", "ورود", "درباره ما", "خروج"]
        # items=["sahar"]


class RegisterUser(tornado.web.RequestHandler):
    def get(self):
        self.render("Register.html")

    def post(self):
        fname = self.get_argument("fname")
        lname = self.get_argument("lname")
        education = self.get_argument("education")
        email = self.get_argument("email")
        password = self.get_argument("password")
        key=self.get_argument("key")
        key_rex=r'[a-z]{2}[0-9]{3}'
        query = """INSERT INTO 'user'('firstName','lastName','education','email','password','keys')
         VALUES(?,?,?,?,?,?)"""
        cursor = self.application.db.cursor()
        #cursor.execute(query, [fname, lastname, education, email, password, "sssss"])
        cursor.execute(query, ["sahar", "nafisi", "diplom", "sahar@gmail.com", "123", "sssss"])
        self.application.db.commit()
        self.redirect("/addUser")

if __name__ == "__main__":
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/addUser", RegisterUser),
    ], **settings)

    app.db = sqlite3.connect("site.db")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()