from flask import render_template

from app import app
from models.bean_list import *

@app.route("/beans")
def beans():
    return render_template("beans.html", title="Mean Bean Shop", beans=beans_list)