from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello", method=["GET"])
def get_hello():
    data = {
        "name":None,
        "password":None
    }
    return render_template("hello.html", data=data)

@app.route("/hello", method=["POST"])
def get_hello():
    name = request.form.get("name", None) # defaults to none
    password = request.form.get("password", None) 
    print([name, password])
    data = {
        "name":name,
        "password":password
    }
    return render_template("hello.html", data=data)