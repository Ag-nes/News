from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=2f0c2069133e4621a60e6e6f16d5e64e"
    r = requests.get(url).json()

    cases = {
        'articles': r['articles']
    }

    return render_template("index.html", case = cases)


if __name__ == "__main__":
    app.run(debug = True)
