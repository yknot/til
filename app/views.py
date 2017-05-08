from flask import render_template
from app import app
from .models import Post


@app.route("/")
@app.route("/index")
def index():
    # get all of the posts
    posts = Post.query.filter_by().all()
    return render_template("index.html",
                           title='Home',
                           posts=posts)
