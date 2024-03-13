from flask import Flask, render_template, request, redirect
from mongita import MongitaClientDisk
from bson import ObjectId

app = Flask(__name__)

# create a mongita client connection
client = MongitaClientDisk()

# open the quotes database
quotes_db = client.quotes_db


@app.route("/", methods=["GET"])
@app.route("/quotes", methods=["GET"])
def get_quotes():
    # data = [
    #     {"text": "I'm hungry. When's lunch?", "author": "Dorothy"},
    #     {"text": "You threw that ball. You go get it.", "author": "Suzy"},
    # ]
    # open the quotes collection
    quotes_collection = quotes_db.quotes_collection
    # load the data
    data = list(quotes_collection.find({}))
    for item in data:
        item["_id"] = str(item["_id"])
        item["object"] = ObjectId(item["_id"])
    # display the data
    return render_template("quotes.html", data=data)


@app.route("/add", methods=["GET"])
def get_add():
    return render_template("add_quote.html")

@app.route("/add", methods=["POST"])
def post_add():
    text = request.form.get("text", "")
    author = request.form.get("author", "")
    if text != "" and author != "":
        # open the quotes collection
        quotes_collection = quotes_db.quotes_collection
        #insert the quote
        quote_data = {
            "text":text,
            "author":author
        }
        quotes_collection.insert_one(quote_data)
    # usually do a redirect('....')
    return redirect("/quotes")

@app.route("/delete", methods=["GET"])
@app.route("/delete/<id>", methods=["GET"])
def get_delete(id=None):
    if id:
        # open the quotes collection
        quotes_collection = quotes_db.quotes_collection
        # delete the item
        quotes_collection.delete_one({"_id":ObjectId(id)})
    # return to the quotes page
    return redirect("/quotes")