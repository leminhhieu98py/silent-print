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
printer_1 = config.get('CONFIG', 'printer_1').strip("\n")
printer_1 = printer_1 if (printer_1 != "0") else ""
printer_2 = config.get('CONFIG', 'printer_2').strip("\n")
printer_2 = printer_2 if (printer_2 != "0") else ""
printer_3 = config.get('CONFIG', 'printer_3').strip("\n")
printer_3 = printer_3 if (printer_3 != "0") else ""


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


get_list_printers()