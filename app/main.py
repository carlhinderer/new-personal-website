from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_view():
    return render_template('index.html')

@app.route("/blog")
def blog_view():
    return render_template('blog.html')
