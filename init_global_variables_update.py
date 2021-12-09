from tkinter import *
import configparser
import os
import requests
import json
import plyer
import time

from requests.api import request




win = Tk()
win.tk.call("source", "temp/azure.tcl")
win.tk.call("set_theme", "light")


config = configparser.ConfigParser()
config.read('temp/CONFIG.INI')
current_version = config.get('VERSION','version').strip("\n")
directory_frame = ""
request_url = "https://static.globex.vn/barcode-update/latest_version_silent_print"


current_folder = os.getcwd()


def notify_message(message):
    plyer.notification.notify(
        title="Silent Print",
        message = message,
        app_icon = "temp/print.ico",
        timeout = 1,
    )


def get_server_version():
    request = requests.get(request_url)
    version, url = "", ""
    if request.ok:
        data = request.json()
        data = json.dumps(data)
        data = json.loads(data)
        version = data["latest_version"] if data["latest_version"] else ""
        url = data["url"] if data["url"] else ""
    else:  # HTTP status code 4XX/5XX
        notify_message("Checking version failed: status code {}".format(request.status_code))
    return version, url

server_version, download_url = get_server_version()


have_new_version = current_version != server_version 