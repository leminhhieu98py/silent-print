from flask import Flask, render_template, request, jsonify, make_response
from threading import Thread


from print import *


app = Flask(__name__)

@app.route("/print")
def printer():
    return render_template("index.html")

@app.route("/print/create-entry", methods=['POST'])
def create_entry():
    req = request.get_json(force = True)
    url = req["url"] if req["url"] else ""
    if url != "":
        print_engine(url)

    res = make_response(jsonify({"message": "JSON received"}), 200)
    res.headers["Content-Type"] = "application/json"
    return res


def start_server():
    app.run()


server = Thread(target=start_server)
server.start()