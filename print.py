from pyhtml2pdf import converter
import win32print
import win32api
import os
import string
import random
import time

from global_variables import *


def filename_generator(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def save_to_pdf(url):
    filename = filename_generator()
    filename_with_ext = filename + ".pdf"
    filepath = os.path.join("pdf", filename_with_ext)
    converter.convert(url, filepath)


def print_pdf(printer):
    current_printer = win32print.SetDefaultPrinter(printer)
    current_printer = win32print.GetDefaultPrinter()
    pdf_folder_path = os.path.join("pdf")
    try:
        for filename in os.listdir(pdf_folder_path):
            if filename.endswith(".pdf"):
                filepath = os.path.join(pdf_folder_path, filename)
                print_cmd = '"{}" /t "{}" "{}"'.format(FOXIT_EXE, filepath, current_printer)
                subprocess.Popen(print_cmd)
                time.sleep(1)
                remove_pdf(filepath)
            else:
                continue
    except:
        print("Failed")
        pass


def remove_pdf(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


def print_engine():
    url = "https://devlabel.globex.vn/itemsOrderExpress/label/printbill?orderNumber=GB00000224232"
    save_to_pdf(url)
    print_pdf(printer)


print_engine()