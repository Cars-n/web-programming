# flask allows for dynamically created webpages
# run with flask --app hello run   
from flask import Flask, jsonify #jsonify is a lib from flask thay turns strutures into json
app = Flask(__name__)

@app.route('/') # this is called a decorator
def get_index():
    return  f"Hello, from the World!"

@app.route('hello/')
def get_hello():
    me = "Carson"
    return  f"Hello, {me} from the World!"

@app.route('/goodbye')
def get_goodbye():
    me = "Carson"
    return  f"Goodbye, {me} from the World!"

@app.route("data")
def get_data():
    data = [
        {"name":"suzy","type":"dog"},
        {"name":"sandy","type":"cat"}
    ]
    return jsonify(data)

@app.route("/api/status")
def get_status():
    data = [
        {"name":"suzy","status":"sleeping"},
        {"name":"dorthy","status":"hungry"}
    ]
    return jsonify(data)

@app.route("/<path:path>")
def serve_static():
    return send_from_directory('.', path)