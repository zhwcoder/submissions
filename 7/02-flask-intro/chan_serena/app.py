from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    text = "<h1><font color="blue">Home</font></h1>"
    return text

@app.route("/page2")
def page2():
    return render_template("page2.html")

if __name__== "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
        
