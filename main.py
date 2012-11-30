from flask import Flask, render_template
from tweets import best_movies

app = Flask(__name__)

@app.route("/")
def main():
    tweet_list = best_movies()
    return render_template("index.html", tweets=tweet_list)

if __name__ == "__main__":
    app.run()
