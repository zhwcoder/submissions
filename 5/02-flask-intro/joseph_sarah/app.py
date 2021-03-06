from flask import Flask, render_template
import random


app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/jokes")
def jokes():
    jokelist = ["Frozen yogurt.","Where do you go to make complicated ice cream dishes? \nSundae School!", "Why did the reporter talk to the ice cream? \nHe was looking for the scoop!", "Why did the carton have a tumble? \nIt was a rocky road.", "What do you get when you cross 90s hip hop and dessert? \nVanilla Ice cream!"]
    i=random.randint(0,len(jokelist)-1)
    joke=jokelist[i]
    return render_template("jokes.html", jokehere=joke)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1')
