from flask import render_template
from app import app
from .models import Posts


@app.route("/")
@app.route("/index")
def index():
    # get all of the posts
    posts = Posts.query.filter_by().all()

    return render_template("index.html",
                           title='Home',
                           posts=posts)
