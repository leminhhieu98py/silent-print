from pyhtml2pdf import converter
import os
from os import path
import string
import random
import time
from threading import Thread
import win32print
import subprocess


from global_variables import *
from const import *


def create_pdf_folder(pdf_folder):
    if not path.exists(pdf_folder):
        os.mkdir(pdf_folder)


def filename_generator(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def save_to_pdf(url, pdf_folder):
    filename = filename_generator()
    filename_with_ext = filename + ".pdf"
    filepath = os.path.join(pdf_folder, filename_with_ext)
    converter.convert(url, filepath)

    return filepath


def print_pdf(printer, pdf_folder, filepath):
    win32print.SetDefaultPrinter(printer)
    try:
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        print_cmd = '"{}" /t "{}" "{}"'.format(FOXIT_EXE, filepath, printer)
        my_pro = subprocess.Popen(print_cmd,    #subprocess not working when exporting to exe file
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        startupinfo=si)
        # my_pro.communicate()


        print("Printing...")
        time.sleep(10)
        print("Removing...")
        remove_pdf(pdf_folder ,filepath)

    except Exception as e:
        print(e)
        notify_message("In lỗi: " + printer)
        pass
    except RuntimeError as e:
        print(e)
        pass
    except ValueError as e:
        print(e)
        pass



def remove_pdf(pdf_folder,filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        if pdf_folder == PAPER_FOLDER["A4"]:
            display_files_left(display_status_a4, PAPER_FOLDER["A4"])
        elif pdf_folder == PAPER_FOLDER["A5"]:
            display_files_left(display_status_a5, PAPER_FOLDER["A5"])
        elif pdf_folder == PAPER_FOLDER["A6"]:
            display_files_left(display_status_a6, PAPER_FOLDER["A6"])



def print_A4(url):
    global printer_a4
    if printer_a4 == "":
        printer_a4 = get_printer_name("printer_a4")
    if printer_a4 != "":
        create_pdf_folder(PAPER_FOLDER["A4"])
        filepath = save_to_pdf(url, PAPER_FOLDER["A4"])
        display_files_left(display_status_a4, PAPER_FOLDER["A4"])
        print_pdf(printer_a4, PAPER_FOLDER["A4"], filepath)
    else:
        notify_message("Vui lòng chọn máy in")


def print_A5(url):
    global printer_a5
    if printer_a5 == "":
        printer_a5 = get_printer_name("printer_a5")
    if printer_a5 != "":
        create_pdf_folder(PAPER_FOLDER["A5"])
        filepath = save_to_pdf(url, PAPER_FOLDER["A5"])
        display_files_left(display_status_a5, PAPER_FOLDER["A5"])
        print_pdf(printer_a5, PAPER_FOLDER["A5"], filepath)
    else:
        notify_message("Vui lòng chọn máy in")


def print_A6(url):
    global printer_a6
    if printer_a6 == "":
        printer_a6 = get_printer_name("printer_a6")
    if printer_a6 != "":
        create_pdf_folder(PAPER_FOLDER["A6"])
        filepath = save_to_pdf(url, PAPER_FOLDER["A6"])
        display_files_left(display_status_a6, PAPER_FOLDER["A6"])
        print_pdf(printer_a6, PAPER_FOLDER["A6"], filepath)
    else:
        notify_message("Vui lòng chọn máy in")


def print_engine(url, paper_type):
    text = "Processing...          "
    if int(paper_type) == PAPER_TYPE["A4"]:
        display_status_a4(text)
        thread_a4 = Thread(target=print_A4, args=(url,))
        thread_a4.start()
    elif int(paper_type) == PAPER_TYPE["A5"]:
        display_status_a5(text)
        thread_a5 = Thread(target=print_A5, args=(url,))
        thread_a5.start()
    elif int(paper_type) == PAPER_TYPE["A6"]:
        display_status_a6(text)
        thread_a6 = Thread(target=print_A6, args=(url,))
        thread_a6.start()
    else:
        notify_message("Can not find paper type")
