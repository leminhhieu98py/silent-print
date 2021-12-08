from pyhtml2pdf import converter
import os
from os import path
import string
import random
import time
from threading import Thread
import win32api
import win32print


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
    converter.convert(url, filepath)


def print_pdf(printer, pdf_folder):
    pdf_folder_path = os.path.join(pdf_folder)
    if(printer != ""):
        win32print.SetDefaultPrinter(printer)
        try:
            for filename in os.listdir(pdf_folder_path):
                if filename.endswith(".pdf"):
                    filepath = os.path.join(pdf_folder_path, filename)
                    print(filepath)

                    # win32api.ShellExecute(0, 'open', FOXIT_EXE, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+win32print.GetDefaultPrinter()+'" "' + filepath + '"', '.', 0) --> default pdf reader  --> mất nội dung 2 bên cạnh

                    # win32api.ShellExecute(0,"print",filepath,'"%s"' % win32print.GetDefaultPrinter(),".",0)   --> default pdf reader  --> mất nội dung 2 bên cạnh

                    si = subprocess.STARTUPINFO()
                    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

                    print_cmd = '"{}" /t "{}" "{}"'.format(FOXIT_EXE, filepath, printer)
                    my_pro = subprocess.Popen(print_cmd,    #subprocess not working when exporting to exe file
                    stdin=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    startupinfo=si)
                    my_pro.communicate()


                    print("Printing...")
                    time.sleep(4)
                    print("Removing...")
                    # remove_pdf(filepath)

                else:
                    continue
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
    global printer_1
    if printer_1 == "":
        printer_1 = config.get('CONFIG', 'printer_1').strip("\n")
        printer_1 = printer_1 if (printer_1 != "0") else ""
    create_pdf_folder(PAPER_FOLDER["A4"])
    save_to_pdf(url, PAPER_FOLDER["A4"])
    print_pdf(printer_1, PAPER_FOLDER["A4"])


def print_A5(url):
    global printer_2
    if printer_2 == "":
        printer_2 = config.get('CONFIG', 'printer_2').strip("\n")
        printer_2 = printer_2 if (printer_2 != "0") else ""
    create_pdf_folder(PAPER_FOLDER["A5"])
    save_to_pdf(url, PAPER_FOLDER["A5"])
    print_pdf(printer_2, PAPER_FOLDER["A5"])


def print_A6(url):
    global printer_3
    if printer_3 == "":
        printer_3 = config.get('CONFIG', 'printer_3').strip("\n")
        printer_3 = printer_3 if (printer_3 != "0") else ""
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
    else:
        notify_message("Can not find paper type")
