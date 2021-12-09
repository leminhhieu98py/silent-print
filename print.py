from pyhtml2pdf import converter
import os
from os import path
import string
import random
import time
from threading import Thread
import win32api
import win32print
# from weasyprint import HTML


from global_variables import *
from notify import *
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
    # HTML(url).write_pdf(filepath)
    converter.convert(url, filepath)

    return filepath


def print_pdf(printer, pdf_folder, filepath):
    pdf_folder_path = os.path.join(pdf_folder)
    if(printer != ""):
        win32print.SetDefaultPrinter(printer)
        try:
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            print_cmd = '"{}" /t "{}" "{}"'.format(FOXIT_EXE, filepath, printer)
            # my_pro = subprocess.Popen(print_cmd,    #subprocess not working when exporting to exe file
            # stdin=subprocess.PIPE,
            # stderr=subprocess.PIPE,
            # stdout=subprocess.PIPE,
            # startupinfo=si)
            # my_pro.communicate()


            print("Printing...")
            time.sleep(10)
            print("Removing...")
            remove_pdf(filepath)

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
    else:
        notify_message("Vui lòng chọn máy in")




def remove_pdf(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


def print_A4(url):
    global printer_a4
    if printer_a4 == "":
        printer_a4 = get_printer_name("printer_a4")
    create_pdf_folder(PAPER_FOLDER["A4"])
    filepath = save_to_pdf(url, PAPER_FOLDER["A4"])
    print_pdf(printer_a4, PAPER_FOLDER["A4"], filepath)


def print_A5(url):
    global printer_a5
    if printer_a5 == "":
        printer_a5 = get_printer_name("printer_a5")
    create_pdf_folder(PAPER_FOLDER["A5"])
    filepath = save_to_pdf(url, PAPER_FOLDER["A5"])
    print_pdf(printer_a5, PAPER_FOLDER["A5"], filepath)


def print_A6(url):
    global printer_a6
    if printer_a6 == "":
        printer_a6 = get_printer_name("printer_a6")
    create_pdf_folder(PAPER_FOLDER["A6"])
    filepath = save_to_pdf(url, PAPER_FOLDER["A6"])
    print_pdf(printer_a6, PAPER_FOLDER["A6"], filepath)



def print_engine(url, paper_type):
    if int(paper_type) == PAPER_TYPE["A4"]:
        thread_a4 = Thread(target=print_A4, args=(url,))
        thread_a4.start()
    elif int(paper_type) == PAPER_TYPE["A5"]:
        thread_a5 = Thread(target=print_A5, args=(url,))
        thread_a5.start()
    elif int(paper_type) == PAPER_TYPE["A6"]:
        thread_a6 = Thread(target=print_A6, args=(url,))
        thread_a6.start()
    else:
        notify_message("Can not find paper type")
