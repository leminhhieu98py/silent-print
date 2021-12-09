import os
import configparser
from tkinter import *
from tkinter import ttk
import win32print
import plyer


os.environ['PYSTRAY_BACKEND'] = 'gtk'


# NOTIFICATION --------------------------------------------------
def notify_message(message):
    plyer.notification.notify(
        title="Silent Print Application",
        message=message,
        app_icon="temp/print.ico",
        timeout=1,
    )


# CONFIG PRINTERS -----------------------------------------------
config = configparser.ConfigParser()
config.read('temp/CONFIG.INI')


FOXIT_EXE = "temp\\Foxit Reader\\FoxitReader.exe"


printer_list = ['']


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


#DISPLAYING GLOBAL USE -----------------------------------------
win = Tk()
icon = None

win.tk.call("source", "temp/azure.tcl")
win.tk.call("set_theme", "light")

directory_frame = ""


def display_frame():
    global directory_frame
    directory_frame = ttk.LabelFrame(win, text='Choose Printers', width=450, height=240)
    directory_frame.place(x=10, y=10)


display_frame()


def display_status_a4(display_text):
    a4_status = Label(directory_frame, text=display_text, font=('Arial', 8))
    a4_status.place(x=90, y=45)


def display_status_a5(display_text):
    a4_status = Label(directory_frame, text=display_text, font=('Arial', 8))
    a4_status.place(x=90, y=110)


def display_status_a6(display_text):
    a4_status = Label(directory_frame, text=display_text, font=('Arial', 8))
    a4_status.place(x=90, y=175)



# COUNT AND DISPLAY NUMBER OF PRINTING FILES LEFT IN FOLDER----
def count_files(pdf_folder):
    count = 0
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            count += 1

    return str(count)

def display_files_left(display_status_function, pdf_folder):
    count = count_files(pdf_folder)
    if count == "0":
        display_status_function("No file left            ") #thêm dấu cách ở cuối để label sau nó k bị dính/ đè với label trước
    elif count == "1":
        display_status_function(count + " file is printing...          ")
    else:
        display_status_function(count + " files are printing...      ")



# 