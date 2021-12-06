from pyhtml2pdf import converter
import win32print
import win32api
import os
from os import path
import string
import random
import time
from threading import Thread


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


def print_pdf(printer, pdf_folder):
    current_printer = win32print.SetDefaultPrinter(printer)
    current_printer = win32print.GetDefaultPrinter()
    pdf_folder_path = os.path.join(pdf_folder)
    try:
        for filename in os.listdir(pdf_folder_path):
            if filename.endswith(".pdf"):
                filepath = os.path.join(pdf_folder_path, filename)
                print_cmd = '"{}" /t "{}" "{}"'.format(FOXIT_EXE, filepath, current_printer)
                # subprocess.Popen(print_cmd)
                time.sleep(2)
                remove_pdf(filepath)
            else:
                continue
    except:
        print("Failed")
        pass


def remove_pdf(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


def print_A4(url):
    create_pdf_folder(PAPER_FOLDER["A4"])
    save_to_pdf(url, PAPER_FOLDER["A4"])
    print_pdf(printer_1, PAPER_FOLDER["A4"])


def print_A5(url):
    create_pdf_folder(PAPER_FOLDER["A5"])
    save_to_pdf(url, PAPER_FOLDER["A5"])
    print_pdf(printer_2, PAPER_FOLDER["A5"])


def print_A6(url):
    create_pdf_folder(PAPER_FOLDER["A6"])
    save_to_pdf(url, PAPER_FOLDER["A6"])
    print_pdf(printer_3, PAPER_FOLDER["A6"])


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
