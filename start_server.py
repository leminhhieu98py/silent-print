from flask import Flask, render_template, request, jsonify, make_response
from threading import Thread
from multiprocessing import Process
import requests


from print import *
from notify import *


app = Flask(__name__)

@app.route("/print")
def printer():
    return render_template("index.html")


@app.route("/print/create-entry", methods=['POST'])
def create_entry():
    req = request.get_json(force = True)
    url = req["url"] if req["url"] else ""
    paper_type = req["paper_type"] if req["paper_type"] else ""
    if url != "" and paper_type != "":
        print_engine(url, paper_type)
    else:
        notify_message("Can not find Url or paper type")

    res = make_response(jsonify({"message": "JSON received"}), 200)
    res.headers["Content-Type"] = "application/json"
    return res


@app.post('/seriouslykill')
def seriouslykill():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutting down..."


def kill():
    requests.post('http://localhost:5000/seriouslykill')
    return "Shutting down..."


def start_server():
    app.run()


server = Thread(target=start_server)
server.start()