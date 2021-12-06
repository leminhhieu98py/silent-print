from tkinter import *
from tkinter import ttk
import pystray
from pystray import MenuItem as item
import PIL.Image

from handle_buttons import *
from global_variables import *
from start_server import *


directory_frame = ""

def quit_window():
    icon.stop()
    win.destroy()


def show_window():
    win.after(0, win.deiconify())
    win.mainloop()


def hide_window():
    global icon
    win.withdraw()
    try:
        image = PIL.Image.open("temp/print.ico")
        menu = (item('Show application', show_window), item('Quit', quit_window))
        icon = pystray.Icon("name", image, "Silent print application", menu)
        icon.run()
    except Exception as e:
        pass


def display_frame():
    global directory_frame
    directory_frame = ttk.LabelFrame(win, text='Choose Printers', width=450, height=200)
    directory_frame.place(x=10, y=10)


def config_app_screen():
    windowWidth = 470
    windowHeight = 220
    screenWidth = win.winfo_screenwidth()
    screenHeight = win.winfo_screenheight()
    xCordinate = int((screenWidth/2) - (windowWidth/2))
    yCordinate = int((screenHeight/2) - (windowHeight/2))
    win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
    win.resizable(width=0, height=0)
    win.iconbitmap("temp/print.ico")
    win.title("Silent Print Application")


def display_printer():
    global printer
    e = StringVar()
    if printer in printer_list:
        e.set(printer)
    else:
        printer = config.get('CONFIG', 'printer').strip("\n")
        e.set(printer)
        win32print.SetDefaultPrinter(printer)

    optionmenu = ttk.OptionMenu(directory_frame, e, *printer_list, command=select_printer)
    optionmenu.place(x=90, y=10, width=340)

    optionmenu = ttk.OptionMenu(directory_frame, e, *printer_list, command=select_printer)
    optionmenu.place(x=90, y=60, width=340)

    optionmenu = ttk.OptionMenu(directory_frame, e, *printer_list, command=select_printer)
    optionmenu.place(x=90, y=110, width=340)




def display_guide_labels():
    a4_label = Label(directory_frame, text='A4 printer: ')
    a4_label.place(x=10, y=10)

    a5_label = Label(directory_frame, text='A5 printer: ')
    a5_label.place(x=10, y=60)

    a6_label = Label(directory_frame, text='A6 printer: ')
    a6_label.place(x=10, y=110)


win.protocol('WM_DELETE_WINDOW', hide_window)
