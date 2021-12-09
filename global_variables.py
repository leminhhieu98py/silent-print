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
# printer_a4 = config.get('CONFIG', 'printer_a4').strip("\n")
# printer_a4 = printer_a4 if (printer_a4 != "0") else ""
# printer_a5 = config.get('CONFIG', 'printer_a5').strip("\n")
# printer_a5 = printer_a5 if (printer_a5 != "0") else ""
# printer_a6 = config.get('CONFIG', 'printer_a6').strip("\n")
# printer_a6 = printer_a6 if (printer_a6 != "0") else ""


FOXIT_EXE = "temp\\Foxit Reader\\FoxitReader.exe"
GHOSTSCRIPT_PATH = "temp\\GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = "temp\\GSPRINT\\gsprint.exe"


printer_list = ['']
auto_print_status = False
auto_print_thread_status = False

def get_list_printers():
    printers = win32print.EnumPrinters(2)
    NAME_INDEX = 2
    for printer in printers:
        printername = printer[NAME_INDEX]
        if printername != "":
            printer_list.append(printername)


def get_printer_name(printer):
    name = config.get('CONFIG', printer).strip("\n")
    name = name if (name != "0") else ""
    return name


printer_a4 = get_printer_name("printer_a4")
printer_a5 = get_printer_name("printer_a5")
printer_a6 = get_printer_name("printer_a6")

get_list_printers()