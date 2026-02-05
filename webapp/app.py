from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    quote = "Une hirondelle ne fait pas le printemps"
    author = "Anonyme"
    return render_template("index.html", quote=quote, author=author)


app.run(host="0.0.0.0", port=5000)
