import os
import subprocess
import configparser
from tkinter import *
import win32print




os.environ['PYSTRAY_BACKEND'] = 'gtk'

win = Tk()
icon = None

win.tk.call("source", "temp/azure.tcl")
win.tk.call("set_theme", "light")

config = configparser.ConfigParser()
config.read('temp/CONFIG.INI')
printer = config.get('CONFIG', 'printer').strip("\n")
printer = printer if (printer != "0") else win32print.GetDefaultPrinter()


FOXIT_EXE = "temp\\Foxit Reader\\FoxitReader.exe"
printer_list = ['']
auto_print_status = False
auto_print_thread_status = False

def get_list_printers():
    global printer_list
    data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\r\r\n')
    data=data[1:] # To get rid of the first row

    for line in data:
        for printername in line.split("  "):
            if printername != "":
                printer_list.append(printername)
                break # To get the first column value only

get_list_printers()
