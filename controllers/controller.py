from flask import render_template

from app import app
from models.bean_list import *


@app.route("/")
def index():
    return render_template("index.html", title="MBS")


@app.route("/beans")
def bean_shop():
    return render_template("beans.html", title="MBS", beans=beans_list)


@app.route("/bean/<bean_id>")
def single_bean(bean_id):
    chosen_bean = beans_list[int(bean_id)]
    return render_template("bean.html", title="MBS", bean=chosen_bean)
