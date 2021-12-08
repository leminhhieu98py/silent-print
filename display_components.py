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
    kill()


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


def display_printers():
    global printer_1
    global printer_2
    global printer_3


    # SET SELECTION
    a4 = StringVar()
    if printer_1 in printer_list:
        a4.set(printer_1)
    else:
        printer_1 = config.get('CONFIG', 'printer_1').strip("\n")
        a4.set(printer_1)

    a5 = StringVar()
    if printer_2 in printer_list:
        a5.set(printer_2)
    else:
        printer_2 = config.get('CONFIG', 'printer_2').strip("\n")
        a5.set(printer_2)

    a6 = StringVar()
    if printer_3 in printer_list:
        a6.set(printer_3)
    else:
        printer_3 = config.get('CONFIG', 'printer_3').strip("\n")
        a6.set(printer_3)


    # DISPLAY SELECT BOX
    optionmenu = ttk.OptionMenu(directory_frame, a4, *printer_list, command=select_printer_1)
    optionmenu.place(x=90, y=10, width=340)

    optionmenu = ttk.OptionMenu(directory_frame, a5, *printer_list, command=select_printer_2)
    optionmenu.place(x=90, y=60, width=340)

    optionmenu = ttk.OptionMenu(directory_frame, a6, *printer_list, command=select_printer_3)
    optionmenu.place(x=90, y=110, width=340)


def display_guide_labels():
    a4_label = Label(directory_frame, text='A4 printer: ')
    a4_label.place(x=10, y=15)

    a5_label = Label(directory_frame, text='A5 printer: ')
    a5_label.place(x=10, y=65)

    a6_label = Label(directory_frame, text='A6 printer: ')
    a6_label.place(x=10, y=115)


win.protocol('WM_DELETE_WINDOW', hide_window)
