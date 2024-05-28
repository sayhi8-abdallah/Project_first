"""this is training about creating a web"""
import sqlite3
from flask import Flask, render_template

Hacking_app = Flask(__name__)


db = sqlite3.connect("baby.db")
cr = db.cursor()
x = cr.execute("select * from skills")
y = x.fetchall()
d = len(y)


my_skills = [("Python", 85), ("MySQL", 35), ("HTML", 40),
             ("CSS", 25), ("JavaScript", 50)]

my_skills.append(y[d - 1][0:2])
db.close()


@Hacking_app.route("/")
def homepage():
    """this is a fuction for training about creating a web"""
    return render_template("homepage.html",
                           title="HomePage",
                           custom_css="home")


@Hacking_app.route("/add")
def addpage():
    """this is a fuction for training about creating a web"""
    return render_template("add.html",
                           title="AddPage",
                           custom_css="add",
                           database="add")


@Hacking_app.route("/about")
def aboutpage():
    """this is a fuction for training about creating a web"""
    return render_template("about.html",
                           title="About")


@Hacking_app.route("/skills")
def skills():
    """this is a fuction for training about creating a web"""
    return render_template("skills.html",
                           title="My Skills",
                           page_head="My Skills",
                           description="This Is My Skills Page",
                           skills=my_skills,
                           custom_css="skills")


if __name__ == "__main__":

    Hacking_app.run(debug=True)
