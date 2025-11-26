from flask import Flask, g, make_response, render_template, request

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.debug = True


@app.route("/")
def index():
    return "Hello, World!!"


@app.route("/test")
def test():
    return render_template("growing-unit/index.html")


@app.route("/warehouse")
def warehouse():
    return render_template("warehouse/index.html")
